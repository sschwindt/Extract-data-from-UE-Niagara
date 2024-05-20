import os
import shutil


def copy_shot_images(input_folder, output_folder, batch_size):
    # Check if target folder exists, and create if not yet existent.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate list of all multiples of batch_size
    multiples = [batch_size * i for i in range(1, 46)]  # 45 multiples of 4800 to 206400

    # Copy each image according to the multiples of batch_size
    for idx, multiple in enumerate(multiples, start=1):
        input_path = os.path.join(input_folder, f"Shot.{multiple}.jpeg")
        output_path = os.path.join(output_folder, f"Shot.{multiple}.jpeg")

        if os.path.exists(input_path):
            shutil.copyfile(input_path, output_path)
            print(f"Bild Shot.{multiple}.jpeg wurde kopiert.")
        else:
            print(f"Bild Shot.{multiple}.jpeg wurde nicht gefunden.")

    print(f"Es wurden insgesamt {idx} Bilder kopiert.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:  # make sure input is provided
        try:
            copy_shot_images(
                input_folder=str(sys.argv[1]),
                output_folder=str(sys.argv[2]),
                batch_size=int(sys.argv[3])
            )
        except KeyError or TypeError or ValueError:
            print("Wrong input arguments. Script requires 3 input arguments:\n" + str(dir(copy_shot_range)))
    else:
        print("Working with in-script variable definitions...")
        # Paths to the folders
        input_folder = "/home/IWS/kemmler/Documents/NewPics"
        output_folder = "/home/IWS/kemmler/Documents/FinalPics"
        batch_size = 4800

        # Call function for copying images
        copy_shot_images(input_folder, output_folder, batch_size)
