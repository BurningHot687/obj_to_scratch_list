# Author: BurningHot687
# License: MIT
# Description: Converts a .obj 3D model file into a scratch list format (txt file).

import sys
import os

# Create the file if it does not exist
def make_scratch_list():
    open(txt_dir, 'w').close()

# Initial setup of 2 things: what to read and what to make
obj_read = ""
while not os.path.exists(obj_read):
    obj_name = f"{input("Name of obj file (omit '.obj'): ")}.obj"
    obj_read = input("File path of obj: ")
    obj_read = os.path.join(os.path.expanduser("~"), obj_read, obj_name)
# Output .txt file name, change if approaching 200,000 lines
txt_write = f"{input("Name of txt file to edit/create (omit '.txt'): ")}.txt"
txt_dir = os.path.join(os.path.expanduser("~"), input("File path to save scratch list: "), txt_write)

# See if the file exists. If so, decide whether to replace or append to. If not, make a new file
try:
    open(txt_dir, 'r').close()
    print(f"The file '{txt_dir}' already exists.")
    append_delete = input("[ANY] - Append | [D] Delete: ").lower()
    if append_delete == 'd':
        try:
            os.remove(txt_dir)
        except FileNotFoundError:
            print("[ERR] Couldn't delete file. A new file will be created.")
        make_scratch_list()
except FileNotFoundError:
    make_scratch_list()

# Model Variables
num_colors = 0    # Number of colors used in the model, set to 0 for default color
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
            # Count number of faces for estimation
            obj_lines += 1
    try:
        with open(txt_dir, "r") as txt_file:
            for line in txt_file:
                txt_lines += 1
    except FileNotFoundError:
        # If file does not exist, set lines to 0
        txt_lines = 0
    print(f".obj lines: '{obj_lines}'\n.txt lines: '{txt_lines}'\nTotal lines: '{txt_lines + obj_lines}'")
    print("List will fit." if txt_lines + obj_lines < 200000 else "List will NOT fit.")
    sys.exit(0) if txt_lines + obj_lines > 200000 else None

with open(obj_read, "r") as obj_file, open(txt_dir, "a") as txt_file:
    txt_file.write(obj_name + "\n")
    txt_file.write(f"{num_colors}\n")
    for line in obj_file:
        if line.startswith("v "):
            parts = line.split()
            x, y, z = parts[1], parts[2], parts[3]
            vertices.append((x, y, z))
        elif line.startswith("f "):
            parts = line.split()
            first, second, third = parts[1], parts[2], parts[3]
            faces.append((int(first), int(second), int(third)))
    for face in faces:
        current_line = ""
        for index in face:
            # Faces separated with whitespace currently. Should only be a single space for fast Scratch parsing
            current_line = f"{current_line}{vertices[index-1][0]} {vertices[index-1][1]} {vertices[index-1][2]} "
        txt_file.write(current_line + "\n")
os.startfile(txt_dir)
