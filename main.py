import tkinter as tk
import time
import random

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")
        # get the window dimensions
        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()
        # calculate the center point
        center_x = int(window_width/2 - 250)
        center_y = int(window_height/2 - 250)
        # set the window position and dimensions
        self.master.geometry("500x500+{}+{}".format(center_x, center_y))
        
        self.gifs = [
            tk.PhotoImage(file="work.gif"),
            tk.PhotoImage(file="work2.gif"),
            tk.PhotoImage(file="work4.gif")
        ]
        
        # Create the label for the GIFs
        self.gif_label = tk.Label(master, width=window_width, height=window_height)
        self.gif_label.pack()

        # Start the animation loop
        self.animate()
        # Create input fields for work and rest times
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
        
        # Add a button to start the timer
        self.start_button = tk.Button(master, text="Start", command=self.start_timer, font=("Arial", 8))
        self.start_button.pack()
        self.start_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        
        # Add a label to display the countdown
        self.countdown_label = tk.Label(master, text="", font=("Arial", 14))
        self.countdown_label.pack()
        self.countdown_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    
    def animate(self):
        # Choose a random GIF
        gif = random.choice(self.gifs)

        # Update the label with the new GIF
        self.gif_label.config(image=gif)

        # Schedule the next animation after 2 seconds
        self.master.after(2000, self.animate)
  
    def start_timer(self):
        # Get the work and rest times from the input fields
        work_time = int(self.work_entry.get())
        rest_time = int(self.rest_entry.get())
        
        # Convert the times from minutes to seconds
        work_seconds = work_time * 60
        rest_seconds = rest_time * 60
        
        # Start the timer
        running = True
        while running:
            # Work time
            self.countdown(work_seconds, "Work")
            # Rest time
            self.countdown(rest_seconds, "Rest")
            
    def countdown(self, t, label):
        while t:
            min, sec = divmod(t, 60)
            countdown_text = f"{label}: {min:02d}:{sec:02d}"
            self.countdown_label.config(text=countdown_text)
            self.master.update()
            time.sleep(1) 
            t -= 1
            if label == "Rest" and t == 0 or label == "Work" and t == 0:
                self.countdown_label.config(text="Drink some water")
                self.master.update()
                time.sleep(5)
                self.countdown_label.config(text="Drink some water NOW")
                self.master.update()

# Create the main window
root = tk.Tk()
# Create an instance of the PomodoroTimer class
timer = PomodoroTimer(root)
background = PomodoroTimer(root)

# Start the event loop
root.mainloop()
