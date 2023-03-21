from pathlib import Path

import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

# Excel File
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'av.xlsx'
df = pd.read_excel(EXCEL_FILE, sheet_name='s1200')
data = []
header = df.columns.tolist()
# pd.read_excel(EXCEL_FILE, sheet_name='s1200')

table_column = [
    [sg.Table(values=data, headings=header, max_col_width=25, key='-TABLE-',
              visible_column_map=[True, True, False, False, False,
                                  False, False, False, False, False])],   #num_rows=min(25, len(data))
    [sg.Submit(pad=(300, 5))]
]

layout = [table_column]
          
window = sg.Window('Simple excel form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()
