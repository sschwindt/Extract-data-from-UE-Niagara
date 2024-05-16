import os
import shutil


def copy_shot_images(input_folder, output_folder, batch_size):
    # ÃœberprÃ¼fe, ob der Ausgabeordner vorhanden ist, andernfalls erstelle ihn
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Liste aller Vielfachen von batch_size generieren
    multiples = [batch_size * i for i in range(1, 43)]  # 43 Vielfache von 4800 bis 206400

    # Kopiere jedes Bild entsprechend der Vielfachen von batch_size
    for idx, multiple in enumerate(multiples, start=1):
        input_path = os.path.join(input_folder, f"Shot.{multiple}.jpeg")
        output_path = os.path.join(output_folder, f"Shot.{multiple}.jpeg")

        if os.path.exists(input_path):
            shutil.copyfile(input_path, output_path)
            print(f"Bild Shot.{multiple}.jpeg wurde kopiert.")
        else:
            print(f"Bild Shot.{multiple}.jpeg wurde nicht gefunden.")

    print(f"Es wurden insgesamt {idx} Bilder kopiert.")


# Pfade zu den Ordnern
input_folder = "/home/IWS/kemmler/Documents/NewPics"
output_folder = "/home/IWS/kemmler/Documents/FinalPics"
batch_size = 4800

# Aufruf der Funktion zum Kopieren der Bilder
copy_shot_images(input_folder, output_folder, batch_size)
