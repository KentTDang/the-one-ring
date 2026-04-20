from pathlib import Path
import shutil

cleaned_folder = Path("data") / "Clean"

if cleaned_folder.exists() and cleaned_folder.is_dir():
    shutil.rmtree(cleaned_folder)
    print(f"Deleted: {cleaned_folder}")
else:
    print(f"Folder not found: {cleaned_folder}")