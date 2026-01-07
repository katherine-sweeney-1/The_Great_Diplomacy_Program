import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import cv2

# import commands to draw arrows
"""
import sys
sys.path.append("../The_Great_Diplomacy_Program/Run_TGDP")
from Main import commands
"""

coordinates = []
territory_file = "GUI/Data_Main_Names.csv"
coordinates_file = "GUI/Territory_Main_Coordinates.txt"
def get_coordinates(click):
    if click:
        x_coordinate = click.x
        y_coordinate = click.y
        coordinate = (x_coordinate, y_coordinate)
        coordinates.append(coordinate)
        #print(x_coordinate, y_coordinate)
        #print("Coordinates", coordinates)
        write_coordinates_file(territory_file, coordinates_file)
    #print(x_coordinate, y_coordinate)

def write_coordinates_file(territory_file, coordinates_file):
    with open(territory_file, "r") as file_input, open(coordinates_file, "a") as file_output:
        count = len(coordinates)
        #print(territory_file[count])
        territory_file_count = 0
        for line in file_input:
            if territory_file_count == count - 1:
                print(line)
                print("count", count)
                
                print(coordinates[count - 1], line, file = file_output)
            territory_file_count += 1

def create_territory_listbox(main_window, territory_file):
    # Listbox 
    listbox = tk.Listbox(main_window, yscrollcommand = scrollbar.set)
    opened_file = open(territory_file)
    count = 1
    for entry in opened_file:
        listbox.insert(count, str(entry)[0:3])
        count += 1
    listbox.place(x=700, y=700)
    listbox.pack()
    return listbox

# draw a line on map
def draw_line(map_image): 
    drawing_image = ImageDraw.Draw(map_image)
    coordinates = [(0,0), (200, 200)]
    drawing_image.line(coordinates, fill = "red")

territory_file = "GUI/Data_Main_Names.csv"
coordinates_file = "GUI/Territory_Main_Coordinates.txt"

main_window = tk.Tk()
main_window.title('TGDP GUI')
main_window.geometry("1000x1000")
#main_window.minsize(1000, 1000)
#main_window.maxsize(1000, 1000)

# Close window button
# Button syntax: w = tk.Button (master, option = value)
button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
button.pack()

# image
map_image = Image.open("GUI/kamrans_map_png.png")
map_width = map_image.width
map_height = map_image.height
map_image.thumbnail((map_width, map_height), Image.Resampling.LANCZOS)

# create canvas to click on 
canvas = tk.Canvas(main_window, width = map_width, height = map_height, cursor = "cross")
canvas.pack(fill = tk.BOTH)

#draw_line(map_image)

# convert pil image to tkinter image object
map_image = ImageTk.PhotoImage(map_image)

# create canvas on image
canvas.create_image(0, 0, anchor = tk.NW, image = map_image)

"""
# make image label
map_label = tk.Label(main_window, image = map_image)
map_label.pack (pady = 10)
"""

# Display text or images
display_box = tk.Label(main_window, text = "TGDP Display Box")
display_box.pack()

# Scroll bar
scrollbar = tk.Scrollbar(main_window)
scrollbar.pack(side = 'right', fill = 'y')

# bind image for clicks
coords = main_window.bind("<Button-1>", get_coordinates)
# create listbox
listbox = create_territory_listbox(main_window, territory_file)
#write_coordinates_file(territory_file, coordinates_file)
scrollbar.config(command = listbox.yview)
canvas.image = map_image
main_window.mainloop()