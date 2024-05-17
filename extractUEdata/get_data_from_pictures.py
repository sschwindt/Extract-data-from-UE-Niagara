import cv2
import numpy as np
import os
import pytesseract

# if you do not have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def convert_red_to_white(image):
    # Convert image in HSV color code
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the color range for red in the HSV color space
    lower_red = np.array([0, 50, 50])  # Lower limit for red in HSV code
    upper_red = np.array([10, 255, 255])  # Upper limit for red in HSV code

    # Create mask for red pixels
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Replace red pixels with white pixels in the original image
    image[red_mask > 0] = [255, 255, 255]

    return image


def convert_yellow_to_white(image):
    # Convert image in HSV color code
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the color range for yellow in the HSV color space
    lower_yellow = np.array([15, 50, 50])  # Lower limit for yellow in HSV code
    upper_yellow = np.array([30, 255, 255])  # Upper limit for yellow in HSV code

    # Create mask for yellow pixels
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    # Replace yellow pixels with white pixels in the original image
    image[yellow_mask > 0] = [255, 255, 255]

    return image


def convert_red_and_yellow_to_white(image):
    # Convert red to white
    image_with_red_converted = convert_red_to_white(image.copy())

    # Convert yellow to white
    image_with_red_and_yellow_converted = convert_yellow_to_white(image_with_red_converted.copy())

    return image_with_red_and_yellow_converted


def read_text_from_image(image_path):
    # Read text from the image with Tesseract
    text = pytesseract.image_to_string(cv2.imread(image_path), lang='eng')
    return text.strip()


def process_images_in_folder(input_folder, output_folder):
    # Ensure that the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Flag to check whether the minimum image number has been reached
    reached_min_number = False

    # Iterate through all files in the input folder
    for file_name in sorted(os.listdir(input_folder)):  # Sort files by file name
        # Create complete path to current file
        input_image_path = os.path.join(input_folder, file_name)

        # Only process image files (e.g. jpg, png)
        if os.path.isfile(input_image_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Check whether the current file is larger than or equal to Shot.172800.jpeg
            if int(file_name.split('.')[1]) >= 172800:
                # Load image
                image = cv2.imread(input_image_path)

                # Process image and save in output folder
                processed_image = convert_red_and_yellow_to_white(image)
                output_image_path = os.path.join(output_folder, file_name)
                cv2.imwrite(output_image_path, processed_image)
                print(f"'{file_name}' was successfully edited and saved in '{output_image_path}'")

                # Read text from the edited image
                text = read_text_from_image(output_image_path)

                # Save text to text file
                txt_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.txt")
                with open(txt_file_path, "w") as txt_file:
                    txt_file.write(text)

                print(f"Successfully extracted text from image '{file_name}' and saved in '{txt_file_path}'")

                # Convert dots to commas and vice versa in the text file
                with open(txt_file_path, "r") as txt_file:
                    content = txt_file.read()

                content = content.replace('.', 'temp')  # Replace temporary dot with another character
                content = content.replace(',', '.')  # Replace comma with period
                content = content.replace('temp', ',')  # Replace temporary character with comma

                with open(txt_file_path, "w") as txt_file:
                    txt_file.write(content)


def main():
    # Define input folder and output folder
    input_folder = "C:/Users/Das_Viech_3000/Documents/UE5.3/CorrectFlow/Saved/MovieRenders/5cm/PR0,4PF0,95/SP10000FPS120"
    output_folder = "C:/Users/Das_Viech_3000/Documents/TEST"

    # Processing the images in the input folder
    process_images_in_folder(input_folder, output_folder)


if __name__ == "__main__":
    main()
