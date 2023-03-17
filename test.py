import PySimpleGUI as sg

# Set theme
sg.theme('DarkBlue3')

# Define layout
layout = [[sg.Column([[sg.Text('A:', justification='left')], 
                      [sg.Text('Text 1', justification='left')]], element_justification='left' ), 
           sg.Column([[sg.Text('B:', justification='right')], 
                      [sg.Text('Text 2', justification='right')]], element_justification='right', grab=True)]]

# Create window
window = sg.Window('Two Columns with Different Justifications', layout, resizable=True, size=(400, 100))

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

# Close window
window.close()

