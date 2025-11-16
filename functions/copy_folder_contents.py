
from pathlib import Path
import os
from copy_file_basic import *
from copy_dir_basic import *
from WritingDebug import *
def copy_folder_contents(source_folder, destination_folder, recursive=False):
    source = Path(source_folder)
    destination = Path(destination_folder)
    destination.mkdir(parents=True, exist_ok=True)
    WritingDebug(source_folder)
    for item in source.iterdir():
        # Skip directories if not recursive
        if item.is_dir() and not recursive:
            continue

        # Copy file
        if item.is_file():
            target = destination / item.name
            copy_file_basic(item, target)

        # Copy directories (only if recursive)
        elif item.is_dir() and recursive:
            copy_dir_basic(item, destination / item.name)


