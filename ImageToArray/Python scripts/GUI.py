import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from scripts.ImageToArray import Img2Arr
from scripts.ArrayToImage import Arr2Img
import os
import time

class ImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")

        # Set window size and center on screen
        window_width = 600
        window_height = 725
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

        # Create input and output frames
        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.TOP, padx=10, pady=10)

        # Create input label and drag and drop area
        input_label = tk.Label(input_frame, text="Put image here:")
        input_label.pack(side=tk.TOP)

        self.input_area = tk.Label(input_frame, width=400, height=300, bg="white")
        self.input_area.pack(side=tk.TOP, pady=10)

        # Create a label for loading indication
        self.loading_label = tk.Label(self.root, text="", fg="blue")
        self.loading_label.pack(side=tk.TOP, pady=5)

        # Bind drag and drop events to input area
        self.input_area.bind("<Enter>", lambda event: self.input_area.config(bg="#e6e6e6"))
        self.input_area.bind("<Leave>", lambda event: self.input_area.config(bg="white"))
        self.input_area.bind("<Button-1>", self.open_file)

    def open_file(self, event):
        # Open file dialog to select image file
        filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
        filename = filedialog.askopenfilename(title="Select image file", filetypes=filetypes)

        # Load image and display in input area
        if filename:
            self.image1 = Image.open(filename)
            self.process_image(self.image1)

    def ToArray_thread(self, image_path):
        index = 0  # or some other value depending on your logic
        color_converter = Img2Arr(image_path, index)  # pass image_path and index arguments
        self.JSON = color_converter.ColorsJSON()
        self.start_image_creation_thread()  # Start the image creation thread after JSON is created

    def start_image_creation_thread(self):
        # Start the image creation thread
        t2 = threading.Thread(target=self.ToImage_thread, args=(self.JSON, self.image1))
        t2.start()

    def ToImage_thread(self, JSON, image):
        # Get the dimensions of the image
        width, height = image.size  # Get the width and height from the image
        image_creator = Arr2Img(JSON, width, height)  # pass JSON, width, and height
        self.image = image_creator.ImageParse()  # Ensure self.image is set here

        # Update the GUI after image processing is done
        self.update_gui_with_image(self.image)

        # Indicate processing is done and open the image
        self.loading_label.config(text="Processing complete!")
        self.open_processed_image()

    def process_image(self, image):
        self.JSON = None  # Initialize self.JSON to avoid accessing before assignment

        # Indicate that processing has started
        self.loading_label.config(text="Processing image...")
        
        # Create and start the first thread
        t1 = threading.Thread(target=self.ToArray_thread, args=(image,))
        t1.start()

    def update_gui_with_image(self, image):
        # Convert the image to a format Tkinter can display
        tk_image = ImageTk.PhotoImage(image)

        # Display the processed image in the input area (you might want to change this to an output area)
        self.input_area.config(image=tk_image)
        self.input_area.image = tk_image  # Keep a reference to avoid garbage collection

    def open_processed_image(self):
        output_path = "MinecraftImage.png"  # Adjust the path as needed
        if os.path.exists(output_path):
            os.startfile(output_path)  # Open the image with the default image viewer
        else:
            messagebox.showerror("Error", "Processed image not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessor(root)
    root.mainloop()
