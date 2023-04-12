import PySimpleGUI as sg
import matplotlib.pyplot as plt
import io
from PIL import Image

def equation_to_image(equation, dpi=100):
    buffer = io.BytesIO()
    plt.figure(figsize=(2, 1), dpi=dpi)
    plt.text(0, 0, r'${}$'.format(equation), fontsize=12)
    plt.axis('off')
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    buffer.seek(0)
    image = Image.open(buffer)
    bio = io.BytesIO()
    image.save(bio, format='PNG')
    return bio.getvalue()

# equation = r'\frac{d}{dx} \int_a^x f(t) dt = f(x)'
equation = r'av = 1.67 * mass'

layout = [
    [sg.Text('Equation:')],
    [sg.Image(data=equation_to_image(equation))],
    [sg.Button('OK')]
]

window = sg.Window('Equation Example', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK':
        break

window.close()