import tkinter as tk
from tkinter import messagebox
import sqlite3

# Initialize the main window
root = tk.Tk()
root.title("Sticky Notes")
root.geometry("400x400")

# Connect to SQLite database
conn = sqlite3.connect('notes.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS notes (title TEXT, content TEXT)''')
conn.commit()

# Functions
def save_note():
    title = title_entry.get()
    content = content_text.get("1.0", tk.END)
    if title and content.strip():
        c.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        messagebox.showinfo("Success", "Note saved successfully!")
        title_entry.delete(0, tk.END)
        content_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both title and content.")

def view_notes():
    c.execute("SELECT title, content FROM notes")
    notes = c.fetchall()
    notes_window = tk.Toplevel(root)
    notes_window.title("Saved Notes")
    for idx, (title, content) in enumerate(notes, start=1):
        tk.Label(notes_window, text=f"{idx}. {title}").pack()
        tk.Label(notes_window, text=content).pack()
        tk.Label(notes_window, text="-"*40).pack()

# UI Elements
tk.Label(root, text="Title:").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="Content:").pack()
content_text = tk.Text(root, height=10, width=50)
content_text.pack()

tk.Button(root, text="Save Note", command=save_note).pack(pady=5)
tk.Button(root, text="View Notes", command=view_notes).pack(pady=5)

root.mainloop()
