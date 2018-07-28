# trim-jpegs
## About 
trim-jpegs is a script that conveniently trims white backgrounds of all jpeg files in a given media directory.

## Setup
To run the main program you will need to install the Python Imaging Library Pillow. Ensure that you have **pip** as well as **Python** (2 or 3) installed. It is recommended that you install the following libraries using a [virtualenv](https://virtualenv.pypa.io/en/stable/) to prevent interfence with any existing packages.

`pip install Pillow`

## Running the Code
Run `python main.py --media_dir {path to your media directory}` to trim and replace all jpeg files.
