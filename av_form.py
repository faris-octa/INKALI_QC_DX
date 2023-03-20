import PySimpleGUI as sg

# Data awal untuk tabel
data = [
    [70, 0.4028, 6.984, 1.0045, 1, 0, 'Lakukan pemanasan'],
    [240, 1.0765, 4.73, 1.0045, 1, 0, 'Tambah waktu mixing'],
    [240, 1.211, 3.279, 1.0045, 1, 0, 'Tambah waktu mixing']
]

# Header untuk tabel
header = ['Suhu (\xb0C)', 'Berat Sample (gr)', 'Jumlah Titran (mL)', 'Faktor Buret', 'Faktor NaOH', 'AV', 'Instruksi']

# AV Standard
bottom_std = 20.5
top_std = 22.0

### improvement feature ###
# df = pd.read_csv('C:/Data/dummydata.csv')
# data = df.values.tolist()
# headings = df.columns.tolist()

# Layout GUI
header_column = [
    [sg.Text('S 1200-IK Acid Value Form', font=('Arial', 20), justification='center')],
    [sg.Text('INKALI QC', font=('Arial', 15), justification='center')]
]

input_column = sg.Column([
    [sg.Text('Lot:', size=10), sg.InputText(key='-LOT-', size=(12,1))],
    [sg.Text('Operator QC:', size=10), sg.InputText(key='-OPERATOR-', size=(12,1))],
    [sg.Text('Faktor Buret:', size=10), sg.InputText(key='-FAKTOR-BURET-', size=(12,1))],
    [sg.Text('Faktor NaOH:', size=10), sg.InputText(key='-FAKTOR-NaOH-', size=(12,1))],
    [sg.Frame('Input Sample:',[[sg.Text('Suhu (\xb0C):', size=10), sg.InputText(key='-SUHU-', size=(12,1))],
                               [sg.Text('Berat Sample (gr):', size=10), sg.InputText(key='-BERAT-SAMPLE-', size=(12,1))],
                               [sg.Text('Jumlah Titran (mL):', size=10), sg.InputText(key='-JUMLAH-TITRAN-', size=(12,1))]
                               ], pad=(0,0))],
    [sg.Button('Clear'), sg.Button('Add', size=5 ,pad=(0,0))]
], pad=(0,0))

table_column = [
    [sg.Table(values=data, headings=header, col_widths=[8,14,14,12,12,10,20] , max_col_width=25,
              auto_size_columns=False, justification='center',
              num_rows=7, display_row_numbers=True, background_color='black', key='-TABLE-',)],   #num_rows=min(25, len(data))
    [sg.Submit(pad=(300, 5))]
]


layout = [
    [sg.Column(header_column)],
    [sg.HSeparator()],
    [
        input_column,
        sg.VSeperator(),
        sg.Column(table_column, vertical_alignment='Top'),
    ],
    # [sg.Sizegrip()]
]

# Membuat Window
sg.theme('DarkGreen7')
window = sg.Window('Acid Value Form', layout, keep_on_top=False, finalize=True, resizable=True)
window.set_min_size(window.size)


# functions


# Loop event
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, None):
        break
    if event == 'Add':
        # Ambil input dari user
        try:
            suhu = float(values['-SUHU-'])
            berat_sample = round(float(values['-BERAT-SAMPLE-']),2)
            jumlah_titran = float(values['-JUMLAH-TITRAN-'])
            faktor_buret = float(values['-FAKTOR-BURET-'])
            faktor_NaOH = float(values['-FAKTOR-NaOH-'])
            AV = round((jumlah_titran * faktor_buret * faktor_buret * faktor_NaOH * 5.61) / berat_sample, 4)

        # Logika
            if suhu < 100:
                instruksi = 'Lakukan pemanasan'
                data.append([suhu, berat_sample, jumlah_titran, faktor_buret, faktor_NaOH, AV, instruksi])

            elif 100 <= suhu < 200:
                if AV < bottom_std:
                    instruksi = 'Tambah Oleic Acid'
                elif  bottom_std <= AV <= top_std:
                    instruksi = 'Packing'
                else:
                    instruksi = 'Hubungi atasan'
                data.append([suhu, berat_sample, jumlah_titran, faktor_buret, faktor_NaOH, AV, instruksi])

            elif 200 <= suhu < 300:
                if AV > top_std:
                    instruksi = 'Tambah waktu pemanasan'
                else:
                    instruksi = 'Lakukan cooling'
                data.append([suhu, berat_sample, jumlah_titran, faktor_buret, faktor_NaOH, AV, instruksi])
            window['-TABLE-'].update(values=data)
            window['-SUHU-']('')
            window['-BERAT-SAMPLE-']('')
            window['-JUMLAH-TITRAN-']('')
        except ValueError as e:
            sg.PopupError(str('Mohon input data dengan benar'))
    if event == 'Clear':
        for key in values:
            if key != '-TABLE-':
                window[key]('')

# Keluar
window.close()