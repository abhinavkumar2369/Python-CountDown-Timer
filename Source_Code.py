import tkinter as tk
from tkinter import ttk
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("300x200")
        self.master.resizable(False, False)

        self.time_left = 0
        self.running = False

        self.label = ttk.Label(self.master, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=20)

        self.entry = ttk.Entry(self.master, width=10, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.insert(0, "00:00:00")

        self.start_button = ttk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = ttk.Button(self.master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.running:
            try:
                time_str = self.entry.get()
                h, m, s = map(int, time_str.split(':'))
                self.time_left = h * 3600 + m * 60 + s
                self.running = True
                self.update_timer()
            except ValueError:
                self.label.config(text="Invalid Time")

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.label.config(text="00:00:00")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "00:00:00")

    def update_timer(self):
        if self.running and self.time_left > 0:
            hours, remainder = divmod(self.time_left, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.label.config(text=time_str)
            self.time_left -= 1
            self.master.after(1000, self.update_timer)
        elif self.running and self.time_left <= 0:
            self.label.config(text="Time's up!")
            self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    timer = CountdownTimer(root)
    root.mainloop()
