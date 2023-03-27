import PySimpleGUI as sg

layout = [[sg.Text('Enter your name and age')],
          [sg.Text('Name', size=(15, 1)), sg.InputText()],
          [sg.Text('Age', size=(15, 1)), sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Mini Form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Submit':
        name = values[0]
        age = values[1]
        sg.popup_yes_no()

window.close()