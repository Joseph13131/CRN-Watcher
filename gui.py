import tkinter as tk
from tkinter import ttk
from monitor_crn import st
import threading

root = tk.Tk()
root.title("Monitor CRNs")
root.geometry("300x160")

ttk.Label(root, text="Monitor CRNs (CRN/LessonID):").pack(pady=5)
crn_text = tk.Text(root, height=4, width=30)
crn_text.pack(pady=5)

def submit():
    crns = crn_text.get("1.0", tk.END).strip().split(",")
    l = []
    for a in crns:
        l.append(threading.Thread(target=st, args=(a,)))
    for t in l:
        t.start()
    root.destroy()

ttk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()