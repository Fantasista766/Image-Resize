# Image Processing Program

This program processes images by resizing and cropping them to specified dimensions. It can be useful for batch 
processing images for various purposes such as creating thumbnails or preparing images for a website.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

## Usage

1. Place the images you want to process in the `INPUT` directory. Only JPG/JPEG format images are supported.
2. Run the program.
3. The processed images will be saved in the `OUTPUT\RESIZED` and `OUTPUT\CROPPED` directories.

## Features

- **Resize Image**: Resizes the input image to the specified dimensions and saves it.
- **Crop Image**: Crops the input image to the specified dimensions from the center and saves it.

## Configuration

You can configure the following parameters in the `main.py` file:

- **Input Directory**: Directory where input images are located (`DIRECTORY_IN`).
- **Output Directories**: Directories where processed images will be saved (`DIRECTORY_RESIZE_OUT`, `DIRECTORY_CROP_OUT`).
- **Output Dimensions**: Dimensions for resized and cropped images (`OUT_RESIZE_WIDTH`, `OUT_RESIZE_HEIGHT`, `OUT_CROP_WIDTH`, `OUT_CROP_HEIGHT`).

## How to Run

Run the program by executing the following command:

```bash
python main.py
