This project is a simple yet practical file organization tool built in Python.
It automatically scans a target directory and sorts files into subfolders based on their file extension.

The goal of this project is to demonstrate file system automation using Python’s standard libraries, focusing on clarity, correctness, and real-world usability.

Features

- Iterates through all files in a target directory

- Detects file extensions using os.path.splitext

- Automatically moves files into extension-based folders

- Uses safe file operations with shutil.move

- Easily extendable to support additional file types

Supported extensions in this example:

| File Extension | Destination Folder |
|----------------|--------------------|
| .py            | python/            |
| .csv           | csv/               |
| .jpg           | jpg/               |
| .yml           | yml/               |



Example

- before_structure.png shows all files mixed in a single directory

- after_structure.png shows the same directory after execution, with files organized by extension

Requirements

- Python 3.x

- Standard libraries only (os, shutil)

No external dependencies required.

Usage

Place the script inside or point it to the directory you want to organize

Ensure the destination folders exist (or create them beforehand)

Run the script:

python organizer.py


The files will be moved automatically to their corresponding folders.

Notes

This script was designed for educational and automation purposes.
It can be easily extended to:

- create folders dynamically

- handle unknown extensions

- add logging or dry-run functionality
