import shutil
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from scripts.ImageToArray import Img2Arr
from scripts.ArrayToImage import Arr2Img
import os
import time
import json

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
        input_label = tk.Label(input_frame, text="Put image or folder here:")
        input_label.pack(side=tk.TOP)

        self.input_area = tk.Label(input_frame, width=400, height=300, bg="white")
        self.input_area.pack(side=tk.TOP, pady=10)

        # Create a label for loading indication
        self.loading_label = tk.Label(self.root, text="", fg="blue")
        self.loading_label.pack(side=tk.TOP, pady=5)

        # Bind drag and drop events to input area
        self.input_area.bind("<Enter>", lambda event: self.input_area.config(bg="#e6e6e6"))
        self.input_area.bind("<Leave>", lambda event: self.input_area.config(bg="white"))
        self.input_area.bind("<Button-1>", self.open_file_or_folder)


    def count_unique_colors(self, image):
        # Convert the image to RGB mode and get the colors
        image = image.convert("RGB")
        colors = image.getcolors(maxcolors=1000000)  # Get all colors
        if colors is not None:
            return len(colors)  # Return the count of unique colors
        return 0  # If there are no colors, return 0
        
    def open_file_or_folder(self, event):
        # Ask the user if they want to select a folder or a single file
        choice = messagebox.askyesno("Select Folder", "Would you like to select a folder?")

        if choice:
            # Folder selection
            folder_name = filedialog.askdirectory(title="Select folder")
            if folder_name:
                self.process_folder(folder_name)
        else:
            # Single file selection
            self.open_file()

    def open_file(self):
        # Open file dialog to select image file
        filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
        filename = filedialog.askopenfilename(title="Select image file", filetypes=filetypes)

        # Load image and display in input area
        if filename:
            self.image1 = Image.open(filename)
            self.process_image(self.image1)

    def process_folder(self, folder_name):
        # Process all image files in the folder
        image_files = [f for f in os.listdir(folder_name) if f.endswith(('.png', '.jpg'))]
        imagesLength = len(image_files)

        if image_files:
            for index, image_file in enumerate(image_files):
                image_path = os.path.join(folder_name, image_file)
                self.image1 = Image.open(image_path)
                self.process_image(self.image1, index, imagesLength)
        else:
            messagebox.showerror("Error", "No images found in the selected folder.")


    def ToArray_thread(self, image_path, index, imagesLength):
        color_converter = Img2Arr(image_path, index)  # pass image_path and index arguments
        self.JSON = color_converter.ColorsJSON()
        
        # Check if self.JSON is not None
        if self.JSON is None:
            print("Error: self.JSON is not set. Exiting thread.")
            return  # Exit the thread if JSON path is not set
        
        self.start_image_creation_thread(index)  # Start the image creation thread after JSON is created

        # Path where status.json will be saved
        json_directory = os.path.dirname(self.JSON)  # Assuming self.JSON contains the path of the generated JSON
        status_file_path = os.path.join(json_directory, "status.json")
        

        # Ensure the directory exists
        os.makedirs(json_directory, exist_ok=True)

        

        # Prepare data for status.json
        status_data = {
            "toBeProcessed": [f"canvas{i}.json" for i in range(imagesLength)],  # Adjust as needed
            "alreadyProcessed": []
        }

        # Write status.json
        with open(status_file_path, "w") as status_file:
            json.dump(status_data, status_file, indent=4)
        

    def start_image_creation_thread(self, index):
        # Start the image creation thread
        t2 = threading.Thread(target=self.ToImage_thread, args=(self.JSON, self.image1, index))
        t2.start()

    def ToImage_thread(self, JSON, image, index):
        # Get the dimensions of the image
        width, height = image.size  # Get the width and height from the image
        image_creator = Arr2Img(JSON, width, height)  # pass JSON, width, and height
        self.image = image_creator.ImageParse()  # Ensure self.image is set here

        # Save the image with a unique name based on index
        self.save_processed_image(index)

        # Update the GUI after image processing is done
        self.update_gui_with_image(self.image)

        # Indicate processing is done
        self.loading_label.config(text=f"Processing canvas{index}.json complete!")
        
        # Count unique colors in the processed image
        processed_color_count = self.count_unique_colors(self.image)  # Corrected reference

        # Update the GUI after image processing is done
        self.update_gui_with_image(self.image)  # Corrected reference

        # Indicate processing is done
        self.loading_label.config(text=f"Processing canvas{index}.json complete!\n"
                                       f"Processed unique colors: {processed_color_count}")

    def process_image(self, image, index=0, imagesLength=1):
            self.JSON = None  # Initialize self.JSON to avoid accessing before assignment

            # Count unique colors in the original image
            original_color_count = self.count_unique_colors(image)
            
            # Indicate that processing has started
            self.loading_label.config(text=f"Processing image for canvas{index}.json...\n"
                                           f"Original unique colors: {original_color_count}")

            # Create and start the first thread
            t1 = threading.Thread(target=self.ToArray_thread, args=(image, index, imagesLength))
            t1.start()

    def update_gui_with_image(self, image):
        # Convert the image to a format Tkinter can display
        tk_image = ImageTk.PhotoImage(image)

        # Display the processed image in the input area (you might want to change this to an output area)
        self.input_area.config(image=tk_image)
        self.input_area.image = tk_image  # Keep a reference to avoid garbage collection

    def save_processed_image(self, index):
        # Get the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the target directory in the same place as the script
        target_dir = os.path.join(script_dir, "processed_images")

        # Create the target directory if it does not exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # Define the output path for the image
        output_path = f"canvas{index}.png"  # Save image with an indexed name
        target = os.path.join(target_dir, output_path)

        # Save the processed image to the target directory
        self.image.save(target)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessor(root)
    root.mainloop()
