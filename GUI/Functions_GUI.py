import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import sys


main_window = tk.Tk()

main_window.title('TGDP GUI')
main_window.geometry("600x600")
main_window.minsize(600, 600)
main_window.maxsize(1000, 1000)

# Close window button
# Button syntax: w = tk.Button (master, option = value)
button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
button.pack()

# image
map_image = Image.open("GUI/kamrans_map_png.png")
#map_pil_image.thumbnail((900, 900), Image.Resampling.LANCZOS)



# draw a line on map 
drawing_image = ImageDraw.Draw(map_image)
coordinates = [(0,0), (200, 200)]
drawing_image.line(coordinates, fill = "red")

# convert pil image to tkinter image object
map_image = ImageTk.PhotoImage(map_image)

# make image label
map_label = tk.Label(main_window, image = map_image)
map_label.pack (pady = 10)

# Display text or images
# Display box syntax: w = tk.Label (master, option = value)
display_box = tk.Label(main_window, text = "TGDP Display Box")
display_box.pack()

# Scroll bar
scrollbar = tk.Scrollbar(main_window)
scrollbar.pack(side = 'right', fill = 'y')
# Listbox 
# Displays list of items from which a user can select one or more
# Listbox syntax: w = Listbox (master, option = value)
listbox = tk.Listbox(main_window, yscrollcommand = scrollbar.set)
territory_file = "GUI/Data_Main_Names.csv"
opened_file = open(territory_file)
count = 1
for entry in opened_file:
    #print(entry)
    listbox.insert(count, str(entry))
    count += 1
listbox.pack()
"""
listbox.insert (1, "Edi")
listbox.insert (2, "Lvp")
listbox.insert (3, "Yor")
listbox.insert (4, "Nwg")
listbox.insert (5, "Wal")
listbox.insert (6, "Nao")
listbox.insert (7, "Mao")
listbox.insert (8, "Nth")
listbox.insert (9, "Fin")
listbox.insert (10, "Swe")
listbox.insert (11, "Den")
listbox.pack()
"""


scrollbar.config(command = listbox.yview)
map_label.image = map_image
main_window.mainloop()
