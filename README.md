Collection of scripts for managing my media folder

# Usage

```
usage: media [-h] {rename,install,offset} ...

Manage media files

positional arguments:
  {rename,install,offset}
    rename              Rename media files based on their metadata
    install             Install media scripts to a location in $PATH
    offset              Change the DateTimeOriginal attribute of a media file
                        by adding / subtracting a time offset

options:
  -h, --help            show this help message and exit
```

# Install

```bash
git clone git@github.com:m-rios/media-pipeline.git
cd media-pipeline
./media install
```
