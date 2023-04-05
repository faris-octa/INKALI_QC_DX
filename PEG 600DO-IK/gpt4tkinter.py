import os
import datetime

import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
import openpyxl

app = tk.Tk()
app.title("Acidity Value Calculator")
app.geometry("850x400")

labels = [
    "LOT",
    "Operator",
    "Faktor buret",
    "Faktor NaOH",
    "Reaksi",
    "Berat sample",
    "Jumlah titran",
]

LOT = tk.StringVar()
Operator = tk.StringVar()
Faktor_buret = tk.DoubleVar()
Faktor_NaOH = tk.DoubleVar()
Reaksi = tk.StringVar()
Berat_sample = tk.DoubleVar()
Jumlah_titran = tk.DoubleVar()

entries = [
    ttk.Entry(app, textvariable=LOT),
    ttk.Entry(app, textvariable=Operator),
    ttk.Entry(app, textvariable=Faktor_buret),
    ttk.Entry(app, textvariable=Faktor_NaOH),
    ttk.Entry(app, textvariable=Reaksi),
    ttk.Entry(app, textvariable=Berat_sample),
    ttk.Entry(app, textvariable=Jumlah_titran),
]

for i, label in enumerate(labels):
    ttk.Label(app, text=label).grid(column=0, row=i, padx=(10, 0), pady=(10, 0), sticky="w")
    entries[i].grid(column=1, row=i, padx=(0, 10), pady=(10, 0), sticky="ew")

if os.path.exists("av.xlsx"):
    columns = pd.read_excel("av.xlsx", nrows=0).columns.tolist()
else:
    columns = [
        "LOT", "Step", "Waktu", "Operator QC", "Reaksi (°C)", "Berat Sample (gr)",
        "Jumlah Titran (mL)", "Faktor Buret", "Faktor NaOH", "AV", "Instruksi"
    ]

df = pd.DataFrame(columns=columns)

def determine_instruksi(reaksi):
    if reaksi == "10":
        return "good"
    elif reaksi == "11":
        return "bad"
    elif reaksi == "packing":
        return "OK"
    else:
        return ""

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

    new_data = pd.DataFrame([input_data], columns=columns)
    df = pd.concat([df, new_data], ignore_index=True)

    for index, row in new_data.iterrows():
        treeview.insert("", "end", values=list(row))

submit_button = ttk.Button(app, text="Submit", command=submit_data)
submit_button.grid(column=1, row=len(labels), padx=(0, 10), pady=(10, 0))

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

treeview.grid(column=2, columnspan=2, rowspan=len(labels)+2, padx=10, pady=(10, 0), row=0)

scrollbar = ttk.Scrollbar(app, orient="vertical", command=treeview.yview)
scrollbar.grid(column=4, row=0, sticky="ns", rowspan=len(labels)+2, pady=(10, 0))
treeview.configure(yscrollcommand=scrollbar.set)

def export_to_excel():
    try:
        if os.path.exists("av.xlsx"):
            df_existing = pd.read_excel("av.xlsx")
            df_combined = pd.concat([df_existing, df], ignore_index=True)
        else:
            df_combined = df

        df_combined.to_excel("av.xlsx", index=False)
        messagebox.showinfo("Success", "Data has been exported to av.xlsx.")
        app.quit()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while exporting data: {e}")

export_button = ttk.Button(app, text="Export", command=export_to_excel)
export_button.grid(column=2, columnspan=2, row=len(labels)+1, pady=(0, 10))

app.mainloop()

