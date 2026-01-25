# Draw a line on map
def draw_line_from_coordinates(first_coordinate, second_coordinate, command, drawing_image):
    coordinates = [first_coordinate, second_coordinate]
    origin_coordinate = first_coordinate
    destination_coordinate = second_coordinate
    if command.succeed == True:
        fill = "black"
    else:
        fill = "red"
    upper_coordinates, lower_coordinates = get_arrow_coordinates(origin_coordinate, destination_coordinate)
    drawing_image.line(coordinates, fill, width = 2)
    drawing_image.line(upper_coordinates, fill, width = 2)
    drawing_image.line(lower_coordinates, fill, width = 2)