# Author: BurningHot687
# License: MIT
# Description: Converts a .obj 3D model file into a scratch list format (txt file).

import sys
import os

def make_scratch_list():
    open(txt_dir, 'w').close() # Create the file if it does not exist

# File path variables
obj_name = input("Name of obj file (without extension): ") # Input your .obj file name here without extension
obj_read = os.path.join(os.path.expanduser("~"), input("File path of obj from home/absolute directory: "), f"{obj_name}.obj")
txt_write = f"{input("Name of txt file to look/create: ")}.txt" # Output .txt file name, change if approaching 200,000 lines
txt_dir = os.path.join(os.path.expanduser("~"), input("File path to save scratch list (from home/absolute directory): "), txt_write)

# Handle the wonkiness of the output file path lol
if not os.path.exists(os.path.dirname(txt_dir)):
    make_scratch_list()
else:
    # Ask to append or delete file
    append_delete = input(f"The file {txt_dir} already exists. Type 'a' to append or 'd' to delete and create a new file: ").lower()
    if append_delete == 'd':
        try:
            os.remove(txt_dir) # Delete the file
        except FileNotFoundError:
            print("An unexpected error occurred while trying to delete the file. A new file is being created.")
            make_scratch_list()

# Model Variables
num_colors = 0 # Number of colors used in the model, set to 0 for default gray
colors = []

# Text Writing Variables
vertices = []
faces = []

with open(obj_read, "r") as obj_file:
    obj_lines = 1
    obj_lines += 1 if num_colors > 1 else 0
    txt_lines = 0
    for line in obj_file:
        if line.startswith("f "):
            obj_lines += 1 # Count number of faces for estimation
    try:
        with open(txt_write, "r") as txt_file:
            for line in txt_file:
                txt_lines += 1 # Count number of lines
    except FileNotFoundError:
        txt_lines = 0 # If file does not exist, set lines to 0
    print(f"Number of obj lines: {obj_lines}\nNumber of txt lines: {txt_lines}\nNumber of lines in total: {txt_lines + obj_lines}")
    print("List will fit the new scratch list file." if txt_lines + obj_lines < 200000 else "List will NOT fit the new scratch list file.")
    sys.exit(0) if txt_lines + obj_lines > 200000 else None

with open(obj_read, "r") as obj_file, open(txt_write, "a") as txt_file:
    txt_file.write(obj_name + "\n") # Write the model name as the first line
    txt_file.write(f"{num_colors}\n")# Write number of colors used
    for line in obj_file:
        if line.startswith("v "):
            parts = line.split()
            x, y, z = parts[1], parts[2], parts[3]
            vertices.append((x, y, z)) # Store vertices
        elif line.startswith("f "):
            parts = line.split()
            first, second, third = parts[1], parts[2], parts[3] # Faces are separated with spaces for some reason
            faces.append((int(first), int(second), int(third)))
    for face in faces:
        current_line = ""
        for index in face:
            current_line = f"{current_line}{vertices[index-1][0]} {vertices[index-1][1]} {vertices[index-1][2]} "
        txt_file.write(current_line + "\n") # Write the face vertices to the txt file 
os.startfile(txt_write)