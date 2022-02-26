import argparse
import os
from PIL import Image

"""This code converts all images in a directory from jpg to tif
    using Python Pillow (PIL) library"""

parser = argparse.ArgumentParser()
# Pass directory of images folder path to code from terminal
parser.add_argument("-j", "--jpgs", required=True)
args = parser.parse_args()
jpgs_folder = args.jpgs

# Iterate  over all images in the folder
for jpg_image in os.listdir(jpgs_folder):

    # Generate full path to jpg image
    jpg_path = jpgs_folder + "/" + jpg_image

    # Open image using PIL library
    image = Image.open(jpg_path)

    # Create tif image name
    tif_name = jpg_image[:-3] + "tif"

    # Create an empty folder in parent directory to save tif images
    tifs_folder_name = "Converted Tifs"

    # Path
    tifs_folder_path = os.path.join(jpgs_folder, tifs_folder_name)

    # Try to create the directory and pass if it already exists
    try:
        os.mkdir(tifs_folder_path)
    except OSError:
        pass

    # Generate full path to tif image
    tif_path = tifs_folder_path + "/" + tif_name

    # Save tif image in the same directory
    image.save(tif_path, 'TIFF')

    
