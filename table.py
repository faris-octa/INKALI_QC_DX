from pathlib import Path

import PySimpleGUI as sg
import pandas as pd

#### Table ####
df = pd.DataFrame(columns=['Nama Item', 'Jumlah Item', 'Harga/Item'])
data = [['X', 4, 2000],
        ['Y', 10, 6500]]
#df = pd.concat([df, data], ignore_index=True)

def make_window(theme):
    sg.theme(theme)

    table_layout = [
        [sg.Text("Anything you would use to graph will display here!")],
        [sg.Table(values=data,
                  headings=df.columns.values.tolist()
)]
    ]

    window = sg.Window('My Table Learn', table_layout)
    return window

def main():
    window = make_window(sg.theme())

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()

if __name__ == '__main__':
    sg.theme('DarkTeal9')
    main()