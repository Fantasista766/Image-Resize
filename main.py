from PIL import Image
import os

# Input and output directories for processing images
DIRECTORY_IN = r'INPUT'
DIRECTORY_CROP_OUT = r'OUTPUT\CROPPED'
DIRECTORY_RESIZE_OUT = r'OUTPUT\RESIZED'

# Dimensions for cropped image, I use 16:9 ratio
OUT_CROP_WIDTH = 16 * 40
OUT_CROP_HEIGHT = 9 * 40

# Dimensions for resized image, I use 16:9 ratio
OUT_RESIZE_WIDTH = 2540
OUT_RESIZE_HEIGHT = 1440


def crop_image(image: Image, new_filename: str):
    """Crops the image to the specified dimensions and saves it.

    Args:
        image: Image to crop.
        new_filename: New filename for saving.
    """
    original_width, original_height = image.size

    # crop from the center
    out_start_width = (original_width - OUT_CROP_WIDTH) // 2
    out_start_height = (original_height - OUT_CROP_HEIGHT) // 2

    # cropped image coordinates
    box = (
        out_start_width,
        out_start_height,
        out_start_width + OUT_CROP_WIDTH,
        out_start_height + OUT_CROP_HEIGHT
    )

    new_image = image.crop(box)
    new_image.save(f'{new_filename}_cropped.jpg')


def resize_image(image: Image, new_filename: str):
    """Resizes the image to the specified dimensions and saves it.

    Args:
        image: Image to resize.
        new_filename: New filename for saving.
    """
    new_image = image.resize((OUT_RESIZE_WIDTH, OUT_RESIZE_HEIGHT))
    new_image.save(f'{new_filename}_resized.jpg')


def main():
    # Processing each file in the input directory
    for i, file in enumerate(os.listdir(DIRECTORY_IN), start=1):
        # Constructing paths to the files for saving the modified images
        filename_clear = ''.join(file.title().split('.')[:-1])  # cut out the extension
        filename = DIRECTORY_IN + '\\' + file.title()
        filename_cropped = DIRECTORY_CROP_OUT + '\\' + f'{filename_clear}'
        filename_resized = DIRECTORY_RESIZE_OUT + '\\' + f'{filename_clear}'

        print(f'Processing image {filename_clear}...')

        # Opening the image
        image = Image.open(filename)

        # Resizing the image and saving it
        resize_image(image, filename_resized)

        # Cropping the image and saving it
        crop_image(image, filename_cropped)

    print('\nDone!')


if __name__ == '__main__':
    main()
