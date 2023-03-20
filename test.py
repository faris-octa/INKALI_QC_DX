import PySimpleGUI as sg

layout = [[sg.Text('Masukkan bilangan positif:'), sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Contoh Input Bilangan Positif', layout)

while True:
    event, values = window.Read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    try:
        number = int(values[0])
        if number <= 0:
            raise ValueError('Anda harus memasukkan bilangan positif')
        sg.Popup('Anda memasukkan bilangan positif: ' + str(number))
    except ValueError as e:
        sg.PopupError(str(e))

window.Close()



