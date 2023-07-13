import tkinter as tk
from PIL import Image, ImageTk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")
        self.master.geometry("500x500")
        
        self.work_image = Image.open("working.png")
        self.rest_image = Image.open("resting.png")
        
        self.work_image = self.resize_image(self.work_image)
        self.rest_image = self.resize_image(self.rest_image)
        
        self.gifs = [
            ImageTk.PhotoImage(self.work_image),
            ImageTk.PhotoImage(self.rest_image)
        ]

        self.work_seconds = 0
        self.rest_seconds = 0
        self.is_working = False
        
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.work_label = tk.Label(master, text="Work Time (min):", font=("Arial", 10))
        self.work_label.pack()
        self.work_entry = tk.Entry(master, font=("Arial", 10))
        self.work_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.work_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        
        self.rest_label = tk.Label(master, text="Rest Time (min):", font=("Arial", 10))
        self.rest_label.pack()
        self.rest_entry = tk.Entry(master, font=("Arial", 10))
        self.rest_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.rest_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.start_button = tk.Button(master, text="Start", command=self.start_timer, font=("Arial", 8))
        self.start_button.pack()
        self.start_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        
        self.countdown_label = tk.Label(master, text="", font=("Arial", 14))
        self.countdown_label.pack()
        self.countdown_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    def resize_image(self, image):
        window_width = 500
        window_height = 500

        image = image.resize((window_width, window_height), Image.BILINEAR)

        return image

    def update_image(self):
        if self.is_working:
            gif = self.gifs[0]  # Use working image
        else:
            gif = self.gifs[1]  # Use resting image

        self.canvas.delete("background")
        self.canvas.create_image(0, 0, image=gif, anchor=tk.NW, tags="background")

    def start_timer(self):
        work_time = int(self.work_entry.get())
        rest_time = int(self.rest_entry.get())

        self.work_seconds = work_time * 60
        self.rest_seconds = rest_time * 60
        self.is_working = True

        self.run_timer(self.work_seconds)  # Start with the work timer

    def run_timer(self, time_remaining):
        if time_remaining > 0:
            min, sec = divmod(time_remaining, 60)
            countdown_text = f"{min:02d}:{sec:02d}"
            self.countdown_label.config(text=countdown_text)

            self.update_image()

            time_remaining -= 1
            self.master.after(1000, self.run_timer, time_remaining)
        else:
            self.is_working = not self.is_working
            if self.is_working:
                self.countdown_label.config(text="Drink some water")
                self.update_image()
                self.master.after(5000, self.run_timer, self.rest_seconds)
            else:
                self.countdown_label.config(text="Drink some water NOW")
                self.update_image()
                self.master.after(5000, self.run_timer, self.work_seconds)

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()
