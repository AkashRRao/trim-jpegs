from PIL import ImageChops
from PIL import Image
import os
import argparse

def trim(im, border):
    ''' Function to trim a single image given an Image
        object and a border color.
        Returns a trimmed Image object'''
    bg = Image.new(im.mode, im.size, border)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    else:
        raise ValueError("cannot trim; image was empty")


def trim_and_replace(filenameArray = ""):
    ''' function to trim every jpeg file in the filenameArray,
        present in the media directory.
        '''
    for filename in filenameArray:
        filename = media_directory + '/' + filename
        im = Image.open(filename)
        trimmedIm = trim(im,'white')
        trimmedIm.save(filename,format=im.format)

parser = argparse.ArgumentParser(description='Trim all .jpegs files in the media_dir.')
parser.add_argument('--media_dir', help='directory where media (jpeg) files are stored')

args = parser.parse_args()

if not args.media_dir:
    exit("Please specify media_dir using --videoid /path/to/media_directory")
else:
    media_directory = args.media_dir

filenames = [] # list of all the jpeg filenames in the pwd.

for file in os.listdir(media_directory):
    if file.endswith(".jpg"):
        filenames.append(file)

# trim all the jpeg files in list 'filename'
trim_and_replace(filenames)
