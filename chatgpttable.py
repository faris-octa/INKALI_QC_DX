import PySimpleGUI as sg

# Data awal untuk tabel
data = [
    ['John', 25, 'Male'],
    ['Sarah', 22, 'Female'],
    ['Peter', 30, 'Male'],
    ['Emily', 28, 'Female']
]

# Header untuk tabel
header = ['Name', 'Age', 'Gender']

# Layout GUI
layout = [
    [sg.Text('Name:'), sg.InputText(key='name')],
    [sg.Text('Age:'), sg.InputText(key='age')],
    [sg.Text('Gender:'), sg.InputText(key='gender')],
    [sg.Button('Add'), sg.Button('Exit')],
    [sg.Table(values=data, headings=header, max_col_width=25,
              auto_size_columns=True, justification='center',
              num_rows=min(25, len(data)), key='table')],
]

# Membuat Window
window = sg.Window('Table Example', layout)

# Loop event
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Add':
        # Ambil input dari user
        name = values['name']
        age = values['age']
        gender = values['gender']
        # Tambahkan baris baru ke tabel
        data.append([name, age, gender])
        # Update tampilan tabel
        window['table'].update(values=data)

# Keluar
window.close()