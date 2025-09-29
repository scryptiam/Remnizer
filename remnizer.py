import os
import shutil
from pathlib import Path
from datetime import datetime

# Define file type categories
EXTENSIONS = {
    'Photos': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.raw'},
    'Videos': {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.3gp'},
    'Audios': {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.opus'},
    'Documents': {'.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', 
                  '.odt', '.ods', '.odp', '.rtf', '.csv', '.epub', '.mobi'},
    'Applications': {'.apk', '.exe', '.deb', '.rpm', '.app', '.msi'}
}

# Create a reverse mapping for instant extension lookups
EXT_TO_CATEGORY = {ext: category for category, exts in EXTENSIONS.items() for ext in exts}

def get_script_directory():
    """Get the directory where the script is located"""
    return Path(__file__).resolve().parent

def organize_files(script_dir):
    """Organize files into category folders"""
    report = {cat: [] for cat in list(EXTENSIONS.keys()) + ['Miscellaneous']}
    
    for item in script_dir.iterdir():
        # Skip directories, this script, and the report file
        if not item.is_file() or item.name == os.path.basename(__file__) or item.name == "organization_report.txt":
            continue

        ext = item.suffix.lower()
        
        # Use the efficient reverse mapping for O(1) lookup
        target_cat = EXT_TO_CATEGORY.get(ext, 'Miscellaneous')
        
        # Create destination directory if it doesn't exist
        dest_dir = script_dir / target_cat
        dest_dir.mkdir(exist_ok=True)
        
        # Handle potential file name collisions
        dest_path = dest_dir / item.name
        counter = 1
        while dest_path.exists():
            new_name = f"{item.stem}_{counter}{item.suffix}"
            dest_path = dest_dir / new_name
            counter += 1
            
        # Move the file and update the report
        shutil.move(str(item), str(dest_path))
        report[target_cat].append(dest_path.name) # Log the final name
    
    return report

def generate_report(report_data, script_dir):
    """Generate and save the operation report"""
    report_path = script_dir / "organization_report.txt"
    total_moved = sum(len(files) for files in report_data.values())
    
    with open(report_path, 'w') as f:
        f.write("📂 File Organization Report 📂\n")
        f.write("=" * 30 + "\n")
        f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Directory Organized: {script_dir}\n")
        f.write(f"Total Files Moved: {total_moved}\n")
        f.write("=" * 30 + "\n\n")
        
        for category, files in report_data.items():
            if not files: # Skip empty categories
                continue
                
            f.write(f"--- {category} ({len(files)} files) ---\n")
            for filename in files:
                f.write(f"    - {filename}\n")
            f.write("\n")
        
        f.write("Organization completed successfully!")
    
    return report_path

def main():
    script_dir = get_script_directory()
    print(f"Target directory: {script_dir}")
    
    consent = input("This script will move files in this directory. Are you sure you want to continue? (y/n): ")
    if consent.lower() != 'y':
        print("Organization cancelled by user.")
        return
        
    report_data = organize_files(script_dir)
    report_path = generate_report(report_data, script_dir)
    
    print("\n✅ File organization completed!")
    print(f"Report saved at: {report_path}")

if __name__ == "__main__":
    main()
