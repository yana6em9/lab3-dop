import tkinter as tk
from tkinter import messagebox
import random
import pygame

SIZE = 700
music_playing = False


def render_background(root):
    background_image = tk.PhotoImage(file="brawl_stars.png")

    background = tk.Label(root, image=background_image)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    root.background_image = background_image


def render_header(parent):
    title = tk.Label(
        parent,
        text="BRAWL STARS KEY GENERATOR",
        font=("Arial", 20, "bold"),
        bg="#263b59",
        fg="white"
    )
    title.pack(pady=15)


def render_input(parent):
    label = tk.Label(
        parent,
        text="Enter a 6-digit DEC number:",
        font=("Arial", 12),
        bg="#263b59",
        fg="white"
    )
    label.pack(pady=5)

    entry_number = tk.Entry(parent, font=("Arial", 16), justify=tk.CENTER)
    entry_number.pack(pady=5)

    return entry_number

def animate_stars(label):
    if label.cget("text") == "*  *  *  *  *":
        label.config(text="  *  *  *  *")
    else:
        label.config(text="*  *  *  *  *")

    label.after(500, lambda: animate_stars(label))

def start_music():
    global music_playing

    pygame.mixer.init()
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    music_playing = True


def toggle_music(button):
    global music_playing

    if music_playing:
        pygame.mixer.music.pause()
        music_playing = False
        button.config(text="MUSIC: OFF")
    else:
        pygame.mixer.music.unpause()
        music_playing = True
        button.config(text="MUSIC: ON")


def validate_input(entry_number):
    number = entry_number.get()

    if len(number) != 6:
        messagebox.showerror("Error", "The number must contain 6 digits!")
        return False

    if not number.isdigit():
        messagebox.showerror("Error", "Only digits are allowed!")
        return False

    return True


def generate_block(digits):
    digits_list = list(digits)
    random.shuffle(digits_list)

    number = int("".join(digits_list))

    letter1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    block = "".join(digits_list) + letter1 + letter2

    return block, number


def generate_key(entry_number, result_label):
    number = entry_number.get()

    first_digits = number[3:6]
    second_digits = number[0:3]

    block1, value1 = generate_block(first_digits)
    block2, value2 = generate_block(second_digits)

    block3 = str(value1 + value2).zfill(4)

    key = block1 + "-" + block2 + "-" + block3

    result_label.config(text=key)


def on_generate(entry_number, result_label):
    if validate_input(entry_number):
        generate_key(entry_number, result_label)


def render_frames(root):
    frame = tk.Frame(root, bg="#263b59")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    render_header(frame)
    stars_label = tk.Label(
        frame,
        text="*  *  *  *  *",
        font=("Arial", 20, "bold"),
        bg="#263b59",
        fg="yellow"
    )
    stars_label.pack(pady=5)

    animate_stars(stars_label)
    entry_number = render_input(frame)

    result_label = tk.Label(
        frame,
        text="Your key will appear here",
        font=("Arial", 14, "bold"),
        bg="#263b59",
        fg="white",
        pady=8
    )
    result_label.pack(pady=10)

    btn_generate = tk.Button(
        frame,
        text="GENERATE KEY",
        font=("Arial", 12, "bold"),
        command=lambda: on_generate(entry_number, result_label)
    )
    btn_generate.pack(pady=15)

    btn_music = tk.Button(
        frame,
        text="MUSIC: ON",
        font=("Arial", 10, "bold"),
        command=lambda: toggle_music(btn_music)
    )
    btn_music.pack(pady=5)

    return frame, entry_number


def main():
    root = tk.Tk()
    root.geometry(f"{SIZE}x{SIZE}")
    root.title("Brawl Stars Key Generator")

    render_background(root)
    render_frames(root)
    render_background(root)
    render_frames(root)
    start_music()

    root.mainloop()


if __name__ == "__main__":
    main()