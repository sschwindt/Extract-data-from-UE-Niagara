import os
import shutil


def copy_shot_range(
        input_folder,
        output_folder,
        start_num,
        end_num
):
    """
    Copy range of enumerated image name from input_folder to output folder.

    :param input_folder: os.path of the input folder directory.
    :param output_folder: os.path of the output (target) folder directory
    :param start_num: int; smallest number of image range to copy
    :param end_num: int; highest number of image range to copy
    :return: None
    """

    # Check if target folder exists, and create if not yet existent.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Copy image range to target (output) folder
    for num in range(start_num, end_num + 1):
        input_path = os.path.join(input_folder, f"Shot.{num}.jpeg")
        output_path = os.path.join(output_folder, f"Shot.{num}.jpeg")

        if os.path.exists(input_path):
            shutil.copyfile(input_path, output_path)
            print(f"Copied Shot.{num}.jpeg")
        else:
            print(f"Could not find Shot.{num}.jpeg")

    print(f"Copied {end_num - start_num + 1} pictures.")

    return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:  # make sure input is provided
        try:
            copy_shot_range(
                input_folder=str(sys.argv[1]),
                output_folder=str(sys.argv[2]),
                start_num=int(sys.argv[3]),
                end_num=int(sys.argv[4])
            )
        except KeyError or TypeError or ValueError:
            print("Wrong input arguments. Script requires 4 input arguments:\n" + str(dir(copy_shot_range)))
    else:
        print("Working with in-script variable definitions...")

        # defined input and output (target) folders
        input_folder = r"D:\Games\MorePics"
        output_folder = r"D:\Games\NewPics"
        # define image number range to copy
        start_num = 152000
        end_num = 155000

        # copy range of images from input to output folder
        copy_shot_range(input_folder, output_folder, start_num, end_num)
