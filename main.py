# Floating App Controller
# Copyright (c) 2025 Ahmad Haikal Rizal
# All rights reserved.

import tkinter as tk
from tkinter import ttk, messagebox
import win32gui
import win32con
import keyboard

window_titles = []

def enum_windows():
    window_titles.clear()
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                window_titles.append(title)
    win32gui.EnumWindows(callback, None)

def refresh_listbox():
    enum_windows()
    listbox.delete(0, tk.END)
    for title in window_titles:
        listbox.insert(tk.END, title)

def set_topmost(title, topmost=True):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd:
        flag = win32con.HWND_TOPMOST if topmost else win32con.HWND_NOTOPMOST
        win32gui.SetWindowPos(hwnd, flag, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def on_float_selected(topmost=True):
    selected = listbox.curselection()
    if selected:
        title = listbox.get(selected[0])
        set_topmost(title, topmost)
        status = "always-on-top" if topmost else "normal"
        messagebox.showinfo("Sukses", f"'{title}' sekarang {status}.")

def auto_float_by_keyword(topmost=True):
    keyword = keyword_entry.get().lower()
    matched = []
    for title in window_titles:
        if keyword in title.lower():
            set_topmost(title, topmost)
            matched.append(title)
    if matched:
        status = "di-float" if topmost else "di-unfloat"
        messagebox.showinfo("Auto-Float", f"Jendela berikut telah {status}:\n" + "\n".join(matched))
    else:
        messagebox.showwarning("Tidak Ditemukan", f"Tidak ada jendela dengan keyword: {keyword}")

def float_foreground_window():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        title = win32gui.GetWindowText(hwnd)
        if title:
            set_topmost(title)
            print(f"[HOTKEY] {title} sekarang always-on-top")

root = tk.Tk()
root.title("Floating App Controller")
root.geometry("460x500")
root.resizable(False, False)

# Set icon for the app
root.iconbitmap("favicon.ico")

style = ttk.Style(root)
style.theme_use('clam')

# Show copyright info at the beginning
messagebox.showinfo("Hak Cipta", "Copyright (c) 2025 Ahmad Haikal Rizal\nAll rights reserved.")

ttk.Label(root, text="🪟 Daftar Jendela Aktif:").pack(pady=(10, 0))
frame = ttk.Frame(root)
frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(frame, width=50, height=12)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

ttk.Button(root, text="🔄 Refresh Jendela", command=refresh_listbox).pack(pady=5)
ttk.Button(root, text="📌 Float (Always-on-Top)", command=lambda: on_float_selected(True)).pack()
ttk.Button(root, text="📎 Unfloat (Normal)", command=lambda: on_float_selected(False)).pack(pady=(0, 10))

ttk.Label(root, text="🔍 Auto-Float/Unfloat Berdasarkan Keyword:").pack()
keyword_entry = ttk.Entry(root, width=40)
keyword_entry.pack(pady=3)
frame2 = ttk.Frame(root)
frame2.pack()
ttk.Button(frame2, text="Auto-Float", command=lambda: auto_float_by_keyword(True)).pack(side=tk.LEFT, padx=5)
ttk.Button(frame2, text="Auto-Unfloat", command=lambda: auto_float_by_keyword(False)).pack(side=tk.LEFT, padx=5)

ttk.Label(root, text="🧷 Hotkey: Ctrl + Alt + F untuk float jendela aktif").pack(pady=(20, 5))

refresh_listbox()
keyboard.add_hotkey("ctrl+alt+f", float_foreground_window)

root.mainloop()
