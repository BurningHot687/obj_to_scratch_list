# Turning .obj Files into Scratch Lists for Parsing and Rasterizing

## Purpose & Introduction
This is a script that probably won't be useful to most people. This is used by my parser for reading in .obj files to display in my edited @Elechimobi's 3d engine on Scratch. This is meant to store many extreme low-poly models so that I could animate my part in The Last Real Solar System Song MAP. The output is a txt file to import into Scratch.

## Usage
It will ask for the name and file path of an obj file, then for the name and file path of the txt file. Since the whole point of this is compression, it will ask you if you wish to append or delete the txt file if it exists. If not, it'll automatically create it. If the output txt file is shown to be larger than 200,000 items, the program automatically quits. Otherwise, it'll write in the data.

Example in linux:
```
Name of obj file (without extension): Triangle Test
File path of obj from home/absolute directory: Documents/objects
Name of txt file to look/create: scratch list one
File path to save scratch list (from home/absolute directory): Documents/scratch imports
The file /home/Example/Documents/scratch imports/scratch list one.txt already exists. 
Type anything (like enter) to append or 'd' to delete and create a new file: a
Number of obj lines: 3
Number of txt lines: 108
Number of lines in total: 111
List will fit the new scratch list file.
```

After this, it'll automatically open the txt file.

## Data Structure
There are three parts to the output:
- obj_name: Same name as the imported obj file
- num_colors (unused): How many colors are in the obj file. 0 means default color is used for compression. Used if many colors needed in Scratch model.
- faces: Each face in the obj has three pointers to vertices. For compression, all vertices of a face are included in one line, and all coordinates as well. This results in 9 coordinate points on each line.Unfortunately, shared points aren't supported to make parsing simpler.

```
...
obj_name
num_colors
face 1
face 2
...
```
-# The basic placement of data in the txt file

Continuing from the previous example:
```
...
Triangle Test
0
0 0 0 0 3.8723 0 0 0 1.2393
```