# File Organizer

This script is designed to organize files within a specified source directory into various destination directories based on their file types. It automatically detects newly modified files and moves them to appropriate folders according to their extensions, such as images, videos, audio files, and documents.

## Features

- **Automatic File Organization**: The script automatically sorts files into designated destination directories based on their file types.
- **Real-time Monitoring**: It continuously monitors the specified source directory for any modifications and promptly organizes newly added files.
- **Customizable Destination Directories**: You can customize the destination directories for different file types according to your preference.
- **Supports Multiple File Types**: It supports various file types, including images, videos, audio files, and documents, allowing for comprehensive file organization.

## Prerequisites

- Python 3.x installed on your system.
- Required Python packages can be installed using `pip`. You can install them by running:

## Usage

1. **Configuration**:
 - Replace the placeholder values for `source_dir`, `dest_dir_music`, `dest_dir_videos`, `dest_dir_images`, and `dest_dir_docs` with the actual directory paths where you want to organize your files.
 - Customize the list of supported file extensions for images, videos, audio files, and documents according to your requirements.

2. **Execution**:
 - Run the script using Python:
   ```
   python file_organizer.py
   ```

3. **Operation**:
 - Once the script is running, it will continuously monitor the specified source directory for any modifications.
 - Newly added or modified files will be automatically moved to the appropriate destination directories based on their file types.
 - The script will log the movement of files for tracking purposes.

4. **Termination**:
 - To stop the script, press `Ctrl + C` in the terminal where it is running.

## Customization

- You can customize the behavior of the script by modifying the following parameters:
- `source_dir`: The directory path where files are monitored for organization.
- `dest_dir_music`, `dest_dir_videos`, `dest_dir_images`, `dest_dir_docs`: Destination directories for different types of files.
- Supported file extensions for images, videos, audio files, and documents can be modified as per your requirements.



