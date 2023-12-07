import tkinter as tk
from PIL import Image, ImageTk
import fetching as ft
import pyscreenshot as ImageGrab

def fetch_and_update(text_area):
    new_text = ft.fetch_random_arabic_hadith()
    text_area.config(text=new_text)

def save_as_png(canvas, width, height):
    # Get the coordinates of the canvas
    x, y, x1, y1 = canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + width, canvas.winfo_rooty() + height
    
    # Capture the content of the canvas using pyscreenshot
    screenshot = ImageGrab.grab(bbox=(x, y, x1 * 2, y1 * 2))
    screenshot = screenshot.resize((width, height), Image.ANTIALIAS)
    
    # Save the captured content as a PNG file with increased DPI
    screenshot.save("output.png", "PNG", dpi=(300, 300))

def main():
    def on_plus_button_click():
        fetch_and_update(text_area)

    # Create the main window
    root = tk.Tk()
    root.title("Tazkera")  # Set the title of the window

    # Load the background image
    background_image = Image.open("background.jpeg")
    background_photo = ImageTk.PhotoImage(background_image)

    # Load the new logo image (rsz_tazkera.png)
    logo_image = Image.open("rsz_tazkera.png")
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Set the window size to match the image size
    width, height = background_image.size
    root.geometry(f"{width}x{height}")

    # Make the window non-resizable
    root.resizable(False, False)

    # Create a canvas with the background image
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    # Add a transparent text area in the center using a Label widget
    text = ft.fetch_random_arabic_hadith()
    text_area = tk.Label(canvas, text=text, font=("Helvetica", 16), bd=0, bg="white", fg="black", justify="center", wraplength=360, pady=10)
    text_area.place(relx=0.5, rely=0.5, anchor="center")

    # Set margin and dimensions for the text area
    margin = 50
    text_area.place(x=-20 + margin, y=-55 + margin, width=400, height=230)

    # Add the Tazkera logo above the text with the same left, right, and top margin
    logo_margin = 50
    logo_label = tk.Label(canvas, image=logo_photo, bd=0, bg="white")
    logo_label.place(relx=0.5, rely=0.1, anchor="center", x=logo_margin, y=logo_margin)

    # Add the "+" button in the left-down corner with a margin of 17 to the left and 2 down
    plus_button = tk.Button(canvas, text="+", font=("Helvetica", 12), command=on_plus_button_click, bd=2, width=2, height=2 ,bg="white", fg="black", relief="flat")
    plus_button.place(x=23, rely=0.96, anchor="sw", y=-2)

    root.mainloop()

if __name__ == "__main__":
    main()
