import tkinter as tk
from tkinter import filedialog
from time import strftime
from datetime import datetime
import os

class Notepad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("NightWriter")

        # PanedWindow for resizable panes
        self.paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill="both", expand=True)

        # File list frame (left side)
        self.file_list_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.file_list_frame)

        self.file_listbox = tk.Listbox(self.file_list_frame, width=20)
        self.file_listbox.pack(side="top", fill="y", expand=True)

        self.theme_button = tk.Button(self.file_list_frame, text=" Dark Mode", command=self.toggle_theme)
        self.theme_button.pack(side="bottom", anchor="w")

        # Text area frame (right side)
        self.text_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.text_frame)

        self.text = tk.Text(self.text_frame, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)

        # Footer frame (date and time)
        self.footer_frame = tk.Frame(self.text)
        self.footer_frame.pack(side="bottom", fill="x")

        self.clock_label = tk.Label(self.footer_frame, width=15)
        self.clock_label.pack(side="right")

        self.date_label = tk.Label(self.footer_frame, width=20)
        self.date_label.pack(side="right")

        # Menu bar
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)

        self.is_dark_mode = False
        self.current_file = None

        self.update_clock()
        self.load_file_list()  # Load saved files

    def new_file(self):
        self.text.delete("1.0", "end")
        self.title("NightWriter")
        self.current_file = None
        self.update_file_listbox()

    def open_file(self):
        file = filedialog.askopenfile(parent=self, mode="rb", title="Open a file")
        if file:
            contents = file.read()
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)
            file.close()
            self.title(file.name + " - NightWriter")
            self.current_file = file.name
            self.update_file_listbox()

    def save_file(self):
        if self.current_file is None:
            # Update this part to specify where users should save files
            file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
            if file:
                contents = self.text.get("1.0", "end")
                file.write(contents)
                file.close()
                self.current_file = file.name
                self.title(file.name + " - NightWriter")
                self.update_file_listbox()
                self.save_file_list()  # Save the updated file list
        else:
            with open(self.current_file, "w") as file:
                contents = self.text.get("1.0", "end")
                file.write(contents)
                self.title(self.current_file + " - NightWriter")
                self.update_file_listbox()
                self.save_file_list()  # Save the updated file list

    def update_file_listbox(self):
        self.file_listbox.delete(0, "end")
        if self.current_file:
            self.file_listbox.insert("end", self.current_file)

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def toggle_theme(self):
        if self.is_dark_mode:
            self.text.config(bg="#f0f0f0", fg="black")
            self.file_listbox.config(bg="#f0f0f0", fg="black")
            self.theme_button.config(text=" Dark Mode")
            self.clock_label.config(fg="black", bg="#f0f0f0")
            self.date_label.config(fg="black", bg="#f0f0f0")
        else:
            self.text.config(bg="#2d2d2d", fg="white")
            self.file_listbox.config(bg="#2d2d2d", fg="white")
            self.theme_button.config(text=" Light Mode")
            self.clock_label.config(fg="white", bg="#2d2d2d")
            self.date_label.config(fg="white", bg="#2d2d2d")
        self.is_dark_mode = not self.is_dark_mode

    def update_clock(self):
        time_string = strftime('%H:%M:%S')
        date_string = datetime.now().strftime("%B %d, %Y")
        self.clock_label.config(text=time_string)
        self.date_label.config(text=date_string)
        self.after(1000, self.update_clock)

    def save_file_list(self):
        """Save the list of files to a text file."""
        with open("saved_files.txt", "w") as f:
            for i in range(self.file_listbox.size()):
                f.write(self.file_listbox.get(i) + "\n")

    def load_file_list(self):
        """Load the list of files from the text file."""
        if os.path.exists("saved_files.txt"):
            with open("saved_files.txt", "r") as f:
                for line in f:
                    self.file_listbox.insert("end", line.strip())

if __name__ == "__main__":
    notepad = Notepad()
    notepad.mainloop()
