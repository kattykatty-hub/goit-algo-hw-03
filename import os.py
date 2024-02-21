import os
import shutil
import argparse
from pathlib import Path

def copy_files(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isdir(item_path):
                copy_files(item_path, dest_dir)
            elif os.path.isfile(item_path):
                file_extension = item.split('.')[-1]
                subdir_path = os.path.join(dest_dir, file_extension)
                os.makedirs(subdir_path, exist_ok=True)
                shutil.copy2(item_path, subdir_path)
    except Exception as e:
        print(f'An error occurred while copying files: {e}')

def main():
    parser = argparse.ArgumentParser(description='Copy files recursively and sort them by extension.')
    parser.add_argument('src_dir', type=str, help='Source directory path')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Destination directory path (default: dist)')
    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    try:
        copy_files(src_dir, dest_dir)
        print('Files copied successfully.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
