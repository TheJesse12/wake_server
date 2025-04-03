import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkfont
from PIL import Image, ImageTk
from ping_logic import run_ping
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def build_gui():
    global output_box

    # Dark mode
    ctk.set_appearance_mode("System")
    # Button color
    ctk.set_default_color_theme("blue")

    # info at top
    root = ctk.CTk()
    root.title("Wake Minecraft Server")
    root.geometry("256x256")
    root.resizable(False, False)
    root.iconbitmap(resource_path("assets/sleep.ico"))

    # loading in kierbear image
    base_img = Image.open(resource_path("assets/sleep.png")).resize((64, 64))
    default_photo = ImageTk.PhotoImage(base_img)

    # corners ;)
    top_frame = ctk.CTkFrame(root, corner_radius=15)
    top_frame.pack(pady=10, fill="x", padx=10)

    img_label = tk.Label(top_frame, image=default_photo, bg="blue", bd=0)
    img_label.image = default_photo
    img_label.pack(side="left", padx=(0, 10))

    wake_button = ctk.CTkButton(
        top_frame,
        text="Wake Server",
        font=("Segoe UI", 16, "bold"),
        height=50,
        corner_radius=15,
        command=lambda: run_ping(output_box, img_label, base_img, default_photo)
    )
    wake_button.pack(side="left", fill="x", expand=True)

    output_box = ctk.CTkTextbox(
        root,
        font=("Segoe UI", 12),
        height=200,
        corner_radius=10
    )
    output_box.pack(padx=10, pady=10, fill="both", expand=True)

    root.mainloop()
