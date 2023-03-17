import PySimpleGUI as sg

# Data awal untuk tabel
data = [
    [0.4028, 6.984, 1.0045, 1, 0],
    [1.0765, 4.73, 1.0045, 1, 0],
    [1.211, 3.279, 1.0045, 1, 0]
]

# Header untuk tabel
header = ['Berat Sample', 'Jumlah Titran', 'Faktor Buret', 'Faktor NaOH', 'AV']

# Layout GUI
header_column = [
    [sg.Text('Acid Value Form')],
    [sg.Text('INKALI QC')]
]

input_column = sg.Column([
    [sg.Frame('Input Sample:',[[sg.Text('Berat Sample:', size=10), sg.InputText(key='-BERAT-SAMPLE-', size=(20,1))],
                               [sg.Text('Jumlah Titran:', size=10), sg.InputText(key='-JUMLAH-TITRAN-', size=(20,1))],
                               [sg.Text('Faktor Buret:', size=10), sg.InputText(key='-FAKTOR-BURET-', size=(20,1))],
                               [sg.Text('Faktor NaOH:', size=10), sg.InputText(key='-FAKTOR-NaOH-', size=(20,1))]
                               ], pad=(0,0))],
    [sg.Button('Clear'), sg.Button('Add', size=5 ,pad=(0,0))]
], pad=(0,0))

table_column = [
    [sg.Table(values=data, headings=header, max_col_width=25,
              auto_size_columns=True, justification='center',
              num_rows=7, key='-TABLE-')]  #num_rows=min(25, len(data))
]


layout = [
    [sg.Column(header_column)],
    [sg.HSeparator()],
    [
        input_column,
        sg.VSeperator(),
        sg.Column(table_column),
    ],
    [sg.Sizegrip()]
]

# Membuat Window
window = sg.Window('Acid Value Form', layout, keep_on_top=True, finalize=True, resizable=True)
window.set_min_size(window.size)

# Loop event
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Add':
        # Ambil input dari user
        berat_sample = round(float(values['-BERAT-SAMPLE-']),2)
        jumlah_titran = float(values['-JUMLAH-TITRAN-'])
        faktor_buret = float(values['-FAKTOR-BURET-'])
        faktor_NaOH = float(values['-FAKTOR-NaOH-'])
        AV = (jumlah_titran * faktor_buret * faktor_buret * faktor_NaOH * 5.61) / berat_sample
        # Tambahkan baris baru ke tabel
        data.append([berat_sample, jumlah_titran, faktor_buret, faktor_NaOH, AV])
        # Update tampilan tabel
        window['-TABLE-'].update(values=data)

# Keluar
window.close()