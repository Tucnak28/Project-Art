# Import the Pillow library
from PIL import ImageColor

# Open the ACO file in text mode
with open("colors.aco", "r") as f:
    # Read the number of colors in the file
    num_colors = int(f.readline().strip())
    # Loop through the colors
    for i in range(num_colors):
        # Read the color data
        line = f.readline().strip()
        # Check if the color is in RGB or CMYK format
        if line[0] == "R":  # RGB color
            # Split the line into R, G, and B values
            r, g, b = map(int, line[3:].split())
            print(f"Color {i+1}: RGB({r}, {g}, {b})")
        elif line[0] == "C":  # CMYK color
            # Split the line into C, M, Y, and K values
            c, m, y, k = map(int, line[4:].split())
            # Convert the CMYK values to RGB using the Pillow library
            r, g, b = ImageColor.getcolor("CMYK({}, {}, {}, {})".format(c, m, y, k),
            "RGB")
            print(f"Color {i+1}: CMYK({c}, {m}, {y}, {k}) = RGB({r}, {g}, {b})")
        else:
            print(f"Error: Unknown color format ({line})")
exit()