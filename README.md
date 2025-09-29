# Remnizer - Simple File Organizer 🧹

A simple Python script to automatically organize files in any directory into clean, categorized folders. 

## ✨ Features

- **Automatic**: Scans the folder it's in and sorts everything automatically.
- **Customizable**: Easily add new file types and categories by editing the script.
- **Safe**: Prevents data loss by renaming files if a file with the same name already exists in the destination. Includes a confirmation prompt before running.
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux.
- **Report Generation**: Creates a detailed `organization_report.txt` file summarizing all actions taken.

## 🚀 How to Use

1.  **Download**: Download the `remnizer.py` script.
2.  **Place**: Move the `remnizer.py` file into the folder you want to organize (e.g., your `Downloads` folder).
3.  **Run**: Open a terminal or command prompt, navigate to that folder, and run the script with Python:
    ```sh
    python remnizer.py
    ```
    The script will ask for confirmation before moving any files.

That's it! Your files will be moved into folders like `Photos`, `Videos`, `Documents`, etc.

## 🔧 Customization

You can easily customize the file categories. Open `remnizer.py` and edit the `EXTENSIONS` dictionary at the top of the file:

```python
# Easily add or remove extensions for each category.
EXTENSIONS = {
    'Photos': {'.jpg', '.jpeg', '.png', ...},
    'Videos': {'.mp4', '.avi', ...},
    # Add a new category like this:
    'Ebooks': {'.epub', '.mobi', '.azw3'}
}
```

## 📄 License

This project is licensed under the MIT License.
