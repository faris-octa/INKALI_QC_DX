# from pathlib import Path
from datetime import datetime
import os
import PySimpleGUI as sg
import pandas as pd
# import openpyxl

# Connect to Excel
# current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
# EXCEL_FILE = current_dir / 'av.xlsx'
# EXCEL_FILE = os.path.abspath('C:/Users/INKALI-PC/project/INKALI_QC_DX/av.xlsx')
EXCEL_FILE = os.path.abspath('//192.168.0.47/0_server/Devtec/Production Engineering/08 OTHER/INDIVIDU/FARIS/Project/QC DX/avS1200.xlsx')
# file:///\\192.168.0.47\0_server\Devtec\Production Engineering\LAPORAN TEST LABORATORIUM\KAIZEN, OPTIMASI PROSES, COST-DOWN\2022\PRESENT POLYSOFTER AQ-09 - OPTIMALISASI (ANANTA)-1.docx
df = pd.read_excel(EXCEL_FILE, sheet_name='S1200-IK', header=0)
# workbook = openpyxl.load_workbook(EXCEL_FILE)
# sheet = workbook['S1200-IK']
# header = [cell.value for cell in sheet[1]]
header = df.columns.tolist()
data = []

# edit this to change theme
sg.theme('DarkGreen7')

# AV Standard
bottom_std = 20.5
top_std = 22.0

#### Layout ####
header_row = [
    [sg.Text('S1200-IK Acid Value Form', font=('Arial', 20), justification='center')],
    [sg.Text('INKALI QC', font=('Arial', 15), justification='center')]
]

table_column = [
    # LOT, Step, Waktu, Operator QC, Reaksi (°C), Berat Sample (gr), Jumlah Titran (mL) ,Faktor Buret,
    # Faktor NaOH, AV, Instruksi
    [sg.Table(values=data, headings=header, 
              col_widths=[5,5,10,10,10,14,14,10,10,10,25], 
              auto_size_columns = False,
              visible_column_map=[False, True, True, False, True, True, True, False, False, True, True],
              justification = 'center',
              background_color = 'black',
              key='-TABLE-')],
    [sg.Submit(pad=(300, 5))]
]

input_column = [
    [sg.Frame('Input Sample',[
    [sg.Text('Lot:', size=14), sg.InputText(key='-LOT-', size=(12,1))],
    [sg.Text('Operator QC:', size=14), sg.InputText(key='-OPERATOR-', size=(12,1))],
    [sg.Text('Faktor Buret:', size=14), sg.InputText(key='-FAKTOR-BURET-', size=(12,1))],
    [sg.Text('Faktor NaOH:', size=14), sg.InputText(key='-FAKTOR-NaOH-', size=(12,1),)],
    ])],
    [sg.Text('Reaksi (\xb0C):', size=15), sg.Combo(values=('', 'Packing'), default_value='', readonly=False, size=(10,1), k='-REAKSI-')],
    [sg.Text('Berat Sample (gr):', size=15), sg.InputText(key='-BERAT-SAMPLE-', size=(12,1))],
    [sg.Text('Jumlah Titran (mL):', size=15), sg.InputText(key='-JUMLAH-TITRAN-', size=(12,1))],
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

#### functions ####
def add_row():
    new_row = [lot, step, waktu, operator, reaksi, berat_sample, 
                jumlah_titran, faktor_buret, faktor_NaOH, AV, instruksi]
    data.append(new_row)
    window['-REAKSI-']('')
    window['-BERAT-SAMPLE-']('')
    window['-JUMLAH-TITRAN-']('')

#### Window ####
window = sg.Window('Acid Value Form (S1200-IK)', layout, keep_on_top=False, finalize=True, resizable=True)
window.set_min_size(window.size)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, None):
        break
    
    if event == 'Submit':
        new_df = pd.DataFrame(data, columns=header)
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_excel(EXCEL_FILE, sheet_name='S1200-IK', index=False)
        sg.popup('Data saved!')
        for key in values:
            window[key]('')
        window.close()
    
    if event == 'Clear':
        for key in values:
            if key != '-TABLE-':
                window[key]('')
    
    if event == 'Add':
        try:
            lot = values['-LOT-']
            step = len(data) + 1
            waktu = str(datetime.now().strftime("%H:%M"))
            operator = values['-OPERATOR-']
            reaksi = values['-REAKSI-']
            berat_sample = round(float(values['-BERAT-SAMPLE-']),2)
            jumlah_titran = float(values['-JUMLAH-TITRAN-'])
            faktor_buret = float(values['-FAKTOR-BURET-'])
            faktor_NaOH = float(values['-FAKTOR-NaOH-'])
            AV = round((jumlah_titran * faktor_buret * faktor_NaOH * 5.61) / berat_sample, 4)
            # instruksi = 'testing purposes'
            
            if reaksi.lower() == 'packing':
                if  bottom_std <= AV <= top_std:
                    instruksi = 'OK'
                else:
                    instruksi = 'NG'
                add_row()

            elif 30 < float(reaksi) < 100:
                instruksi = 'lakukan pemanasan hingga 240\xb0C'
                add_row()

            elif 100 <= float(reaksi) < 200:
                if AV < bottom_std:
                    instruksi = 'Tambah Oleic Acid'
                elif  bottom_std <= AV <= top_std:
                    instruksi = 'Packing'
                else:
                    instruksi = 'Hubungi atasan'
                add_row()

            elif 200 <= float(reaksi) < 260:
                if AV > top_std:
                    instruksi = 'Tambah waktu pemanasan'
                else:
                    instruksi = 'Lakukan cooling hingga 120\xb0C'
                add_row()
            
            window['-TABLE-'].update(values=data)
        except ValueError as e:
            sg.PopupError(str('Mohon input data dengan benar'))

window.close()