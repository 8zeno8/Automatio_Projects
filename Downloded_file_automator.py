from os import rename, scandir
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent


# *replace the source_dir, dest_dir_music, dest_dir_videos, dest_dir_images, dest_dir_docs with your own directories

source_dir = ""
dest_dir_music = ""
dest_dir_videos = ""
dest_dir_images = ""
dest_dir_docs = ""

# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi",
                    ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd",
                    ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps",
                    ".ico"]

#  supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

#  supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

# supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1

    # * If the file exists add a number to the end of the file

    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter = +1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        rename(old_name, new_name)

    move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    """
   This function  will trace any updates in the {source_dir}.
   .upper is for not missing out files with uppercase extensions
   """

    def on_modified(self, event: FileSystemEvent):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)

    def check_audio_files(self, entry, name):  # check all audio files

        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                move_file(dest_dir_music, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):

        for video_extension in video_extensions:

            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_videos, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # * Checks all Image Files
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_images, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # * Checks all Document Files
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_docs, entry, name)
                logging.info(f"Moved document file: {name}")


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',  # Corrected format
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
