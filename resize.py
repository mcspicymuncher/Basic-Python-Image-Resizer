import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to handle resizing of the selected image
def resize_image(image_path, width, height):
    try:
        # Open the image using PIL
        img = Image.open(image_path)
        # Resize the image
        resized_img = img.resize((width, height), Image.LANCZOS)
        return resized_img
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")
        return None

# Function to handle the 'Resize' button click
def resize_image_click():
    if selected_image_path:
        try:
            new_width = int(width_entry.get())
            new_height = int(height_entry.get())
            resized_img = resize_image(selected_image_path, new_width, new_height)
            if resized_img:
                # Get save location from user
                save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                          filetypes=[("PNG files", "*.png"),
                                                                     ("JPEG files", "*.jpg"),
                                                                     ("All files", "*.*")])
                if save_path:
                    # Save the resized image to the specified location
                    resized_img.save(save_path)
                    messagebox.showinfo("Success", "Image resized and saved successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid dimensions (integers).")

# Function to handle the 'Open Image' button click
def open_image_click():
    global selected_image_path
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if path:
        selected_image_path = path
        # Display the selected image
        img = Image.open(selected_image_path)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference

# Create the main application window
root = tk.Tk()
root.title("Image Resizer")

# Create and place widgets
open_button = tk.Button(root, text="Open Image", command=open_image_click)
open_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

width_label = tk.Label(root, text="New Width:")
width_label.pack()

width_entry = tk.Entry(root)
width_entry.pack(pady=5)

height_label = tk.Label(root, text="New Height:")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack(pady=5)

resize_button = tk.Button(root, text="Resize and Save", command=resize_image_click)
resize_button.pack(pady=10)

# Initialize global variable for selected image path
selected_image_path = None

# Start the main event loop
root.mainloop()
