# LazyLister: The File Name Extractor

## Overview

Are you too lazy to type `dir` in a terminal and manually copy the text? Do you need the names of some files but don't want to copy them one by one? Well, worry no more! **LazyLister** is here to save the day. This small Python script lists all filenames in a specified folder and writes them to a text file. Simple, effective, and just what you need!

## Features

- Lists all files in a specified subfolder.
- Saves the list to a text file automatically.
- Defaults to listing files from an `input` folder.
- Allows you to specify a different folder as an argument.
- Works on Windows, Mac, and Linux.

## Requirements

- Python 3.x

## How to Use

1. Place the script in your project directory.
2. Ensure you have a subfolder named `input` (or any other folder you want to list files from).
3. Run the script using:

```bash
   python lazy_lister.py
```

   This will list all files in the `input` subfolder and save them to `file_list.txt`.

### Listing Files from Another Folder

Want to list files from a different folder? Just pass the folder name as an argument:

```bash
python lazy_lister.py documents
```

This will scan the `documents` folder and save the file names to `file_list.txt`.

## Example Output

After running the script, you will get a `file_list.txt` file with content like:

```bash
file1.txt
image.png
notes.pdf
report.docx
```

## Why Use This?

- **Efficiency**: No more manually copying filenames.
- **Automation**: Use it in scripts to process file names easily.
- **Lazy Mode Activated**: Seriously, who wants to type out filenames one by one?

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed!
