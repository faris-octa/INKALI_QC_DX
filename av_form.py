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
    [sg.Text('Ini Header')]
]

input_column = sg.Column([
    [sg.Frame('Input Sample:',[[sg.Text('Berat Sample:', size=10), sg.InputText(key='-BERAT-SAMPLE-', size=(20,1))],
                               [sg.Text('Jumlah Titran:', size=10), sg.InputText(key='-JUMLAH-TITRAN-', size=(20,1))],
                               [sg.Text('Faktor Buret:', size=10), sg.InputText(key='-FAKTOR-BURET-', size=(20,1))],
                               [sg.Text('Faktor NaOH:', size=10), sg.InputText(key='-FAKTOR-NaOH-', size=(20,1))]
                               ], pad=(0,0))],
    [sg.Button('Clear'), sg.Button('Add', size=5 ,pad=(0,0))]
], pad=(0,0))

col1 = sg.Column([
    # Categories sg.Frame
    [sg.Frame('Categories:',[[ sg.Radio('Websites', 'radio1', default=True, key='-WEBSITES-', size=(10,1)),
                            sg.Radio('Software', 'radio1', key='-SOFTWARE-',  size=(10,1))]],)],
    # Information sg.Frame
    [sg.Frame('Information:', [[sg.Text(), sg.Column([[sg.Text('Account:')],
                             [sg.Input(key='-ACCOUNT-IN-', size=(19,1))],
                             [sg.Text('User Id:')],
                             [sg.Input(key='-USERID-IN-', size=(19,1)),
                              sg.Button('Copy', key='-USERID-')],
                             [sg.Text('Password:')],
                             [sg.Input(key='-PW-IN-', size=(19,1)),
                              sg.Button('Copy', key='-PASS-')],
                             [sg.Text('Location:')],
                             [sg.Input(key='-LOC-IN-', size=(19,1)),
                              sg.Button('Copy', key='-LOC-')],
                             [sg.Text('Notes:')],
                             [sg.Multiline(key='-NOTES-', size=(25,5))],
                             ], size=(235,350), pad=(0,0))]])], ], pad=(0,0))

# input_column = [
#     [sg.Text('Berat Sample:'), sg.InputText(key='-BERAT-SAMPLE-')],
#     [sg.Text('Jumlah Titran:'), sg.InputText(key='-JUMLAH-TITRAN-')],
#     [sg.Text('Faktor Buret:'), sg.InputText(key='-FAKTOR-BURET-')],
#     [sg.Button('Add'), sg.Button('Exit')]
# ]

table_column = [
    [sg.Table(values=data, headings=header, max_col_width=25,
              auto_size_columns=True, justification='center',
              num_rows=min(25, len(data)), key='-TABLE-')]
]


layout = [
    [sg.Column(header_column)],
    [
        input_column,
        sg.VSeperator(),
        sg.Column(table_column),
    ]
]

# Membuat Window
window = sg.Window('Acid Value Form', layout, keep_on_top=True, finalize=True)

# Loop event
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Add':
        # Ambil input dari user
        berat_sample = float(values['-BERAT-SAMPLE-'])
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