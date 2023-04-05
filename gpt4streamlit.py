import streamlit as st
import pandas as pd

def determine_instruksi(reaksi):
    if reaksi == "10":
        return "good"
    elif reaksi == "11":
        return "bad"
    elif reaksi == "packing":
        return "OK"
    else:
        return "Unknown"

@st.cache_data
def load_data():
    columns = ["LOT", "Operator", "Faktor buret", "Faktor NaOH", "Reaksi", "Berat sample", "Jumlah titran", "AV", "Instruksi"]
    return pd.DataFrame(columns=columns)

df = load_data()

st.title("Input App")

with st.form(key='input_form'):
    LOT = st.text_input("LOT (string):")
    Operator = st.text_input("Operator (string):")
    Faktor_buret = st.number_input("Faktor buret (float):", format="%f")
    Faktor_NaOH = st.number_input("Faktor NaOH (float):", format="%f")
    Reaksi = st.text_input("Reaksi (string):")
    Berat_sample = st.number_input("Berat sample (float):", format="%f")
    Jumlah_titran = st.number_input("Jumlah titran (float):", format="%f")

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        AV = (Jumlah_titran * Faktor_buret * Faktor_NaOH * 5.61) / Berat_sample
        Instruksi = determine_instruksi(Reaksi)

        input_data = {
            "LOT": LOT,
            "Operator": Operator,
            "Faktor buret": Faktor_buret,
            "Faktor NaOH": Faktor_NaOH,
            "Reaksi": Reaksi,
            "Berat sample": Berat_sample,
            "Jumlah titran": Jumlah_titran,
            "AV": AV,
            "Instruksi": Instruksi
        }

        new_data = pd.DataFrame([input_data], columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)

st.write(df)
