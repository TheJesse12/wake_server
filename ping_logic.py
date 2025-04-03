from mcstatus import JavaServer
import threading
from PIL import Image, ImageTk
import tkinter as tk

MAX_RETRIES = 50
RETRY_DELAY = 3

result = (
    f"SERVER HAS AWOKEN!\n"
    f"If you're not on in 5 min it will go back to sleep\n"
)
update = (
    f"Server PC is off!\n"
    f"Yell at Jesse to start\n"
)

def run_ping(output_box, img_label, base_img, default_photo):
    output_box.delete('1.0', tk.END)
    threading.Thread(
        target=lambda: ping_with_retries(output_box, img_label, base_img, default_photo),
        daemon=True
    ).start()

def ping_with_retries(output_box, img_label, base_img, default_photo):
    address = "192.168.68.58:25565"
    retries = 0
    server_awoken = False
    angle = 0

    while retries < MAX_RETRIES:
        try:
            JavaServer.lookup(address).status()
            if not server_awoken:
                update_output(output_box, result)
                img_label.after(0, lambda: img_label.config(image=default_photo))
                img_label.image = default_photo
                server_awoken = True
            return
        except:
            # fun loading kierbear twirl
            rotated = ImageTk.PhotoImage(base_img.rotate(angle))
            angle = (angle + 90) % 360
            img_label.after(0, lambda img=rotated: img_label.config(image=img))
            img_label.image = rotated

            
            if retries > 15:
                update_output(output_box, "SERVER IS STILL EEEPY! HANG TIGHT POOKIE")
            else:
                update_output(output_box, "SERVER IS EEEPY!")

            retries + 1


    if not server_awoken:
        update_output(output_box, update)
        img_label.after(0, lambda: img_label.config(image=default_photo))
        img_label.image = default_photo

def update_output(output_box, text):
    output_box.after(0, lambda: (
        output_box.delete('1.0', tk.END),
        output_box.insert(tk.END, text)
    ))
