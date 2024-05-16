from extractUEdata import copy_shot_range

# defined input and output (target) folders
input_folder = r"D:\Games\MorePics"
output_folder = r"D:\Games\NewPics"
# define image number range to copy
start_num = 152000
end_num = 155000

# copy range of images from input to output folder
copy_shot_range(input_folder, output_folder, start_num, end_num)
