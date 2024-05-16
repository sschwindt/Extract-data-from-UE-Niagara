# Extract data from Unreal Engine and Niagara Fluids

This code extracts text and numbers from screenshots made with Unreal Engine and its Niagara Fluids plugin. The original code was developed by Benjamin Kemmler.

## Requirements

Programming language: Python + libraries listed in `requirements.txt`

Auxiliary software: [Tesseract (OCR)](https://tesseract-ocr.github.io/tessdoc/Installation.html) (on Debian derivates: `sudo apt install tesseract-ocr`)

## Installation
To get started with Python, take a look at [https://hydro-informatics.com/python-basics/pyinstall.html](https://hydro-informatics.com/python-basics/pyinstall.html). We recommend creating a new virtual environment:

```
python -m venv UEnv
```

Activate the environment:

```
source UEnv/bin/activate
```

Navigate (`cd`) to the directory where you cloned or downloaded (extracted) this repository, and pip-install the requirements:

```
pip install -r requirements.txt
```

This will install the following dependencies:

* numpy (`numpy`)
* opencv-python (`cv2`)
* pytesseract (`pytesseract`)
* pytest-shutil (`shutil`across versions)

## Usage

First, the image data on the server is used to determine the number of hours required for rendering.

## Extended Workflow
First, the image data on the server is used to determine how many hours it took to render. Subsequently, the `copy_files` script is used to transfer all images with a multiple of 4800 (i.e., every 4800th image) to an external folder. The script must be entered with the input folder location, which is typically under `PROJECT-NAME\Saved\MovieRenders\FOLDER`. This ensures that only images are copied every 40 seconds. Once the initial set of images has been copied, the remaining images can be deleted. Thus, after processing, 216,011 images reduce to 45.

The `get_data_from_pictures` script is key to extracting data from the imagery, wiht its `process_images_in_folder` function. Prior to initiating `process_images_in_folder`, it is essential to install [Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html), and define the input folder, which is the location of the 45 images. Once this is complete, the output folder must be specified. Next, each image is processed to convert both the red and yellow colors completely to white. This step is necessary to ensure that Tesseract can read the numbers despite poor image contrast. Subsequently, each image is read and the data saved in new text files, named according to the image file name. For instance, `Shot.4800.jpeg` is read into a *txt* file called `Shot.4800.txt`.

The text files serve are then transferred to an Excel file. The Excel file conversion is followed by a convergence check of extracted numbers. Thus, numeric changes shown on each image are expressed as deviations in percentages to determine whether the simulation is running consistently. If convergence is achieved, the results were deemed final. 

**However**, currently, copying the data from the .txt files is not supported due to the potential for errors when reading out the data, which could then be transferred to the Excel table. This is a safeguard to ensure that the values can be entered and evaluated correctly.

The final script is `copy_image_rang`, which is designed for specific scenarios, such as unstable explosions, to copy a fixed selection of images and then transfer them to a video for visual error checking on issues. Both the input and output folders must be set again here. Additionally, the selection numbers must be defined, indicating which image the selection is based on.
