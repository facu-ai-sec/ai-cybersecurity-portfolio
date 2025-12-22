# File Organizer Tool (Python)

This project is a simple yet practical file organization tool built in Python.  
It automatically scans a target directory and sorts files into subfolders based on their file extension.

The main goal of this project is to demonstrate file system automation using Python’s standard libraries, with an emphasis on clarity, correctness, and real-world usability.

---

## Features

- Iterates through all files in a target directory  
- Detects file extensions using `os.path.splitext`  
- Automatically moves files into extension-based folders  
- Uses safe file operations with `shutil.move`  
- Easily extendable to support additional file types  

---

## Supported Extensions (Example)

| File Extension | Destination Folder |
|---------------|--------------------|
| `.py`         | `python/`          |
| `.csv`        | `csv/`             |
| `.jpg`        | `jpg/`             |
| `.yml`        | `yml/`             |

---

## Example

- `before_structure.png` shows all files mixed in a single directory  
- `after_structure.png` shows the same directory after execution, with files organized by extension  

---

## Requirements

- Python 3.x  
- Standard libraries only (`os`, `shutil`)  

No external dependencies are required.

---

## Usage

1. Place the script inside the directory you want to organize, or configure it to point to the target directory.  
2. Ensure the destination folders exist (or create them beforehand).  
3. Run the script:

```bash
python organizer.py
