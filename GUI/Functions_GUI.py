import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import cv2
# import commands to draw arrows
"""
import sys
sys.path.append("../The_Great_Diplomacy_Program/Run_TGDP")
from Main import commands
"""


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

"""
# draw a line on map 
drawing_image = ImageDraw.Draw(map_image)
coordinates = [(0,0), (200, 200)]
drawing_image.line(coordinates, fill = "red")
"""


# convert pil image to tkinter image object
map_image = ImageTk.PhotoImage(map_image)

# create canvas on image
canvas.create_image(0, 0, anchor = tk.NW, image = map_image)

"""
# make image label
map_label = tk.Label(main_window, image = map_image)
map_label.pack (pady = 10)
"""
"""
# Display text or images
display_box = tk.Label(main_window, text = "TGDP Display Box")
display_box.pack()

# Scroll bar
scrollbar = tk.Scrollbar(main_window)
scrollbar.pack(side = 'right', fill = 'y')


# Listbox 
listbox = tk.Listbox(main_window, yscrollcommand = scrollbar.set)
territory_file = "GUI/Data_Main_Names.csv"
opened_file = open(territory_file)
count = 1
for entry in opened_file:
    listbox.insert(count, str(entry)[0:3])
    count += 1
listbox.place(x=700, y=700)
listbox.pack()
"""


#scrollbar.config(command = listbox.yview)
canvas.image = map_image
main_window.mainloop()
