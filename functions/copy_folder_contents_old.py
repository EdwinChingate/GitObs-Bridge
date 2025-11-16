
from pathlib import Path
import shutil

def copy_folder_contents(source_folder, destination_folder, recursive=False):
    destination = Path(destination_folder)
    source = Path(source_folder)
    if not source.exists():
        raise ValueError(f"Source folder does not exist: {source}")

    destination.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():
        # Only copy files if recursive=False
        if item.is_dir() and not recursive:
            continue

        if item.is_file():
            shutil.copy2(item, destination / item.name)
        elif item.is_dir() and recursive:
            shutil.copytree(
                item,
                destination / item.name,
                dirs_exist_ok=True,
            )


