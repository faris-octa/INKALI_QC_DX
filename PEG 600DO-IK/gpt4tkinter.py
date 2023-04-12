import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import datetime

app = tk.Tk()
app.title("AV Calculator")
app.configure(bg="#f0f0f0")

if os.path.exists("av.xlsx"):
    df = pd.read_excel("av.xlsx")
    columns = pd.read_excel("av.xlsx", nrows=0).columns.tolist()
else:
    columns = [
        "LOT", "Step", "Waktu", "Operator QC", "Reaksi (°C)", "Berat Sample (gr)",
        "Jumlah Titran (mL)", "Faktor Buret", "Faktor NaOH", "AV", "Instruksi"
    ]
    df = pd.DataFrame(columns=columns)

style = ttk.Style()
style.configure("my.TButton", background="#f0f0f0", foreground="#333")

LOT = tk.StringVar()
Operator = tk.StringVar()
Faktor_buret = tk.DoubleVar()
Faktor_NaOH = tk.DoubleVar()
Reaksi = tk.StringVar()
Berat_sample = tk.DoubleVar()
Jumlah_titran = tk.DoubleVar()

input_vars = [
    ("LOT", LOT),
    ("Operator", Operator),
    ("Faktor buret", Faktor_buret),
    ("Faktor NaOH", Faktor_NaOH),
    ("Reaksi", Reaksi),
    ("Berat sample", Berat_sample),
    ("Jumlah titran", Jumlah_titran),
]

title_label = ttk.Label(app, text="AV Calculation Application", font=("Helvetica", 16), background="#f0f0f0", foreground="#333")
title_label.grid(column=0, row=0, columnspan=2, padx=(10, 0), pady=(10, 0))

for i, (label_text, var) in enumerate(input_vars):
    label = ttk.Label(app, text=label_text, background="#f0f0f0", foreground="#333")
    label.grid(column=0, row=i+1, padx=(10, 0), pady=(10, 0), sticky="w")
    entry = ttk.Entry(app, textvariable=var, width=10)
    entry.grid(column=1, row=i+1, padx=(0, 10), pady=(10, 0), sticky="e")

def determine_instruksi(reaksi):
    if reaksi == "10":
        return "good"
    elif reaksi == "11":
        return "bad"
    elif reaksi == "packing":
        return "OK"
    else:
        return "Undefined"

def submit_data():
    global df
    AV = (Jumlah_titran.get() * Faktor_buret.get() * Faktor_NaOH.get() * 5.61) / Berat_sample.get()
    Instruksi = determine_instruksi(Reaksi.get())

    waktu = datetime.datetime.now()
    step = len(df) + 1

    input_data = {
        "LOT": LOT.get(),
        "Step": step,
        "Waktu": waktu,
        "Operator QC": Operator.get(),
        "Reaksi (°C)": Reaksi.get(),
        "Berat Sample (gr)": Berat_sample.get(),
        "Jumlah Titran (mL)": Jumlah_titran.get(),
        "Faktor Buret": Faktor_buret.get(),
        "Faktor NaOH": Faktor_NaOH.get(),
        "AV": AV,
        "Instruksi": Instruksi,
    }
    df = df.append(input_data, ignore_index=True)

    for i in treeview.get_children():
        treeview.delete(i)

    for index, row in df.iterrows():
        treeview.insert("", "end", values=(row["Step"], row["Waktu"], row["Reaksi (°C)"], row["Berat Sample (gr)"], row["Jumlah Titran (mL)"], row["AV"], row["Instruksi"]))

submit_button = ttk.Button(app, text="Submit", command=submit_data, style="my.TButton")
submit_button.grid(column=0, row=8, padx=(10, 0), pady=(10, 0))

displayed_columns = [
    "Step", "Waktu", "Reaksi (°C)", "Berat Sample (gr)",
    "Jumlah Titran (mL)", "AV", "Instruksi"
]

column_widths = {
    "Step": 50,
    "Waktu": 100,
    "Reaksi (°C)": 50,
    "Berat Sample (gr)": 60,
    "Jumlah Titran (mL)": 60,
    "AV": 50,
    "Instruksi": 50,
}

treeview = ttk.Treeview(app, columns=displayed_columns, show="headings", height=10)

for column in displayed_columns:
    treeview.heading(column, text=column)
    treeview.column(column, anchor="center", width=column_widths[column])

treeview.grid(column=2, row=1, rowspan=7, padx=(10, 0), pady=(10, 0), sticky="n")

def export_to_excel():
    global df
    if not df.empty:
        df.to_excel("av.xlsx", index=False)
        messagebox.showinfo("Success", "Data exported successfully to av.xlsx")
        app.quit()
    else:
        messagebox.showerror("Error", "There is no data to export")

export_button = ttk.Button(app, text="Export", command=export_to_excel, style="my.TButton")
export_button.grid(column=2, row=8, padx=(10, 0), pady=(10, 0), sticky="e")

app.mainloop()


