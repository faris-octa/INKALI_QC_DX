from pathlib import Path

import PySimpleGUI as sg
import pandas as pd

# Connect to Excel
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'av.xlsx'
df = pd.read_excel(EXCEL_FILE, sheet_name='s1200')
header = df.columns.tolist()
data = []

#### functions ####
# def add_row():
#     temp = [lot, step, operator, reaksi, 
#             berat, titran,f_buret, f_NaOH, AV, Instruksi]
#     pass

# edit this to change theme
sg.theme('DarkGreen7')

#### Layout ####

header_row = [
    [sg.Text('S1200-IK Acid Value Form', font=('Arial', 20), justification='center')],
    [sg.Text('INKALI QC', font=('Arial', 15), justification='center')]
]

table_column = [
    # LOT, Step, Operator QC, Reaksi (°C), Berat Sample (gr), Jumlah Titran (mL) ,Faktor Buret,
    # Faktor NaOH, AV, Instruksi
    [sg.Table(values=data, headings=header, 
              col_widths=[5,5,10,10,14,14,10,10,10,20], 
              auto_size_columns = False,
              visible_column_map=[True, True, True, True, True, True, True, True, True, True],
              justification = 'center',
              background_color = 'black',
              key='-TABLE-')],
    [sg.Submit(pad=(300, 5))]
]

input_column = [
    [sg.Text('Lot:', size=14), sg.InputText(key='-LOT-', size=(12,1))],
    [sg.Text('Operator QC:', size=14), sg.InputText(key='-OPERATOR-', size=(12,1))],
    [sg.Text('Faktor Buret:', size=14), sg.InputText(key='-FAKTOR-BURET-', size=(12,1))],
    [sg.Text('Faktor NaOH:', size=14), sg.InputText(key='-FAKTOR-NaOH-', size=(12,1),)],
    [sg.Frame('Input Sample:',[
    [sg.Text('Reaksi (\xb0C):', size=14), sg.Combo(values=('Initial', '240', '120', 'Packing'), default_value='Initial', readonly=False, size=(10,1), k='-REAKSI-')],
    [sg.Text('Berat Sample (gr):', size=14), sg.InputText(key='-BERAT-SAMPLE-', size=(12,1))],
    [sg.Text('Jumlah Titran (mL):', size=14), sg.InputText(key='-JUMLAH-TITRAN-', size=(12,1))]
    ])],
    [sg.Button('Clear'), sg.Button('Add')]
]

layout = [
    [sg.Column(header_row)],
    [sg.HSeparator()],
    [
        sg.Column(input_column),
        sg.VSeperator(),
        sg.Column(table_column, vertical_alignment='Top'),
    ]
]

#### Window ####
window = sg.Window('Acid Value Form (S1200-IK)', layout, keep_on_top=False, finalize=True, resizable=True)
window.set_min_size(window.size)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, None):
        break
    if event == 'Submit':
        pass
    if event == 'Clear':
        for key in values:
            if key != '-TABLE-':
                window[key]('')
    if event == 'Add':
        try:
            lot = values['-LOT-']
            operator = values['-OPERATOR-']
            reaksi = values['-REAKSI-']
            berat_sample = round(float(values['-BERAT-SAMPLE-']),2)
            jumlah_titran = float(values['-JUMLAH-TITRAN-'])
            faktor_buret = float(values['-FAKTOR-BURET-'])
            faktor_NaOH = float(values['-FAKTOR-NaOH-'])
            AV = round((jumlah_titran * faktor_buret * faktor_buret * faktor_NaOH * 5.61) / berat_sample, 4)
        except ValueError as e:
            sg.PopupError(str('Mohon input data dengan benar'))
        pass
        # RIP LOGIC

window.close()
