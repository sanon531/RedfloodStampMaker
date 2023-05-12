import tkinter as tk
from PIL import Image, ImageEnhance

# Define the input and output file paths
input_file = './fra_improved_infantry_weapons.png'
output_file = './your_output_file.png'

# Define a function to update the image and save the changes
def update_image(imagepath, contrast_value, brightness_value):
    img = Image.open(imagepath)
    r_original, g_original, b_original, a_original = img.split()
    # Apply the intensity and contrast adjustments to the RGB channels
    r = ImageEnhance.Contrast(r_original).enhance(contrast_value)
    r = ImageEnhance.Brightness(r).enhance(brightness_value)
    g = ImageEnhance.Contrast(g_original).enhance(contrast_value)
    g = ImageEnhance.Brightness(g).enhance(brightness_value)
    b = ImageEnhance.Contrast(b_original).enhance(contrast_value)
    b = ImageEnhance.Brightness(b).enhance(brightness_value)

    # Merge the adjusted RGB channels with the alpha channel
    img = Image.merge('RGBA', (r, g, b, a_original))

    # Save the result to the output file
    img.save(output_file)


# Load the PNG file and separate the alpha channel from the RGB channels
img = Image.open(input_file)
r_original, g_original, b_original, a_original = img.split()

# Create the GUI window
root = tk.Tk()
root.title("Image Adjuster")

# Create the contrast slider
contrast_slider = tk.Scale(root, from_=0.1, to=10.0, resolution=0.1, orient=tk.HORIZONTAL, label="Contrast", command=lambda value: update_image(contrast_slider.get(), brightness_slider.get()))
contrast_slider.set(1.0)
contrast_slider.pack()

# Create the brightness slider
brightness_slider = tk.Scale(root, from_=0.1, to=10.0, resolution=0.1, orient=tk.HORIZONTAL, label="Brightness", command=lambda value: update_image(contrast_slider.get(), brightness_slider.get()))
brightness_slider.set(1.0)
brightness_slider.pack()
# Show the GUI window
root.mainloop()