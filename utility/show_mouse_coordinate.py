import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer with Mouse Coordinates")
        
        self.canvas = tk.Canvas(root, width=1920, height=1080)
        self.canvas.pack()
        
        self.label = tk.Label(root, text="Mouse Coordinates: ")
        self.label.pack()
        
        self.canvas.bind("<Motion>", self.mouse_move)
        
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_image)
        
        self.image = None
        self.tk_image = None
    
    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
    
    def mouse_move(self, event):
        if self.image:
            x, y = event.x, event.y
            self.label.config(text=f"Mouse Coordinates: ({x}, {y})")

if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()