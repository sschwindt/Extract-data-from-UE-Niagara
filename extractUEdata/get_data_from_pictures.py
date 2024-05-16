import cv2
import numpy as np
import os
import pytesseract

# Speicherort von Tesseract setzen
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def convert_red_to_white(image):
    # Bild im HSV-Farbraum umwandeln
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Definieren des Farbbereichs fÃ¼r Rot im HSV-Farbraum
    lower_red = np.array([0, 50, 50])  # Untere Grenze fÃ¼r Rot im HSV-Farbraum
    upper_red = np.array([10, 255, 255])  # Obere Grenze fÃ¼r Rot im HSV-Farbraum

    # Erstellen der Maske fÃ¼r rote Pixel
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Ersetzen der roten Pixel durch weiÃŸe Pixel im Originalbild
    image[red_mask > 0] = [255, 255, 255]

    return image


def convert_yellow_to_white(image):
    # Bild im HSV-Farbraum umwandeln
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Definieren des Farbbereichs fÃ¼r Gelb im HSV-Farbraum
    lower_yellow = np.array([15, 50, 50])  # Untere Grenze fÃ¼r Gelb im HSV-Farbraum
    upper_yellow = np.array([30, 255, 255])  # Obere Grenze fÃ¼r Gelb im HSV-Farbraum

    # Erstellen der Maske fÃ¼r gelbe Pixel
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    # Ersetzen der gelben Pixel durch weiÃŸe Pixel im Originalbild
    image[yellow_mask > 0] = [255, 255, 255]

    return image


def convert_red_and_yellow_to_white(image):
    # Rot zu WeiÃŸ konvertieren
    image_with_red_converted = convert_red_to_white(image.copy())

    # Gelb zu WeiÃŸ konvertieren
    image_with_red_and_yellow_converted = convert_yellow_to_white(image_with_red_converted.copy())

    return image_with_red_and_yellow_converted


def read_text_from_image(image_path):
    # Text aus dem Bild mit Tesseract auslesen
    text = pytesseract.image_to_string(cv2.imread(image_path), lang='eng')  # Korrekte Verwendung von cv2.imread
    return text.strip()


def process_images_in_folder(input_folder, output_folder):
    # Sicherstellen, dass der Ausgabeordner vorhanden ist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Flag, um zu Ã¼berprÃ¼fen, ob die Mindestbildnummer erreicht wurde
    reached_min_number = False

    # Iterieren durch alle Dateien im Eingabeordner
    for file_name in sorted(os.listdir(input_folder)):  # Sortiere Dateien nach Dateinamen
        # VollstÃ¤ndigen Pfad zur aktuellen Datei erstellen
        input_image_path = os.path.join(input_folder, file_name)

        # Nur Bilddateien verarbeiten (z. B. jpg, png)
        if os.path.isfile(input_image_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            # ÃœberprÃ¼fen, ob die aktuelle Datei grÃ¶ÃŸer oder gleich Shot.172800.jpeg ist
            if int(file_name.split('.')[1]) >= 172800:
                # Bild laden
                image = cv2.imread(input_image_path)

                # Bild verarbeiten und im Ausgabeordner speichern
                processed_image = convert_red_and_yellow_to_white(image)
                output_image_path = os.path.join(output_folder, file_name)
                cv2.imwrite(output_image_path, processed_image)
                print(f"Bild '{file_name}' wurde erfolgreich bearbeitet und in '{output_image_path}' gespeichert.")

                # Text aus dem bearbeiteten Bild auslesen
                text = read_text_from_image(output_image_path)

                # Text in Textdatei speichern
                txt_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.txt")
                with open(txt_file_path, "w") as txt_file:
                    txt_file.write(text)

                print(f"Text aus Bild '{file_name}' wurde erfolgreich ausgelesen und in '{txt_file_path}' gespeichert.")

                # Umwandlung von Punkten zu Kommas und umgekehrt in der Textdatei durchfÃ¼hren
                with open(txt_file_path, "r") as txt_file:
                    content = txt_file.read()

                content = content.replace('.', 'temp')  # TemporÃ¤r Punkt durch anderes Zeichen ersetzen
                content = content.replace(',', '.')  # Komma durch Punkt ersetzen
                content = content.replace('temp', ',')  # TemporÃ¤res Zeichen durch Komma ersetzen

                with open(txt_file_path, "w") as txt_file:
                    txt_file.write(content)


def main():
    # Eingabeordner und Ausgabeordner definieren
    input_folder = "C:/Users/Das_Viech_3000/Documents/UE5.3/CorrectFlow/Saved/MovieRenders/5cm/PR0,4PF0,95/SP10000FPS120"
    output_folder = "C:/Users/Das_Viech_3000/Documents/TEST"

    # Verarbeiten der Bilder im Eingabeordner
    process_images_in_folder(input_folder, output_folder)


if __name__ == "__main__":
    main()
