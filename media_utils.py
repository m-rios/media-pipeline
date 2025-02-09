import datetime
import json
import os
import subprocess
import sys

def find_metadata_fields(metadata, fields):
    values = []
    for field in fields:
        value = str(metadata[field]) or ''
        if field == 'DateTimeOriginal':
            value = datetime.datetime.strptime(value, "%Y:%m:%d %H:%M:%S").strftime("%y%m%d_%H%M_%S")
        else:
            value = value.replace(" ", "")
        values.append(value)
    return values


def is_gopro(filename):
    return os.system(f"exiftool '{filename}' | grep -iq gopro") == 0


def get_exif_raw_data(filename, fields):
    result = subprocess.run(
        ['exiftool', '-json'] + ['-' + field for field in fields] + [filename],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error: could not get metadata for file `{filename}`")
        print(result.stderr)
        exit(1)

    return json.loads(result.stdout)[0]

def extract_exif_fields(filename, fields):
    exif_data = get_exif_raw_data(filename, fields)
    return find_metadata_fields(exif_data, fields)


def extract_extension(filename):
    return filename.split('.')[-1]


def parse_files(args):
    arg = args[1]
    files = []

    if len(args) > 2:
        files = args[1:-1]
    elif os.path.isdir(arg):
        files = os.listdir(arg)
    elif os.path.isfile(arg):
        files.append(arg)
    else:
        print("Error: argument is neither a file or a directory")
        sys.exit(1)

    return files
