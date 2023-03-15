from datetime import datetime

class AcidValue


def acid_value():
    waktu = datetime.now().strftime("%H:%M")
    suhu = input("suhu(\xb0C)= ")
    berat_sample = float(input("berat sampel(gr) = "))
    jumlah_titran = float(input("jumlah titran(ml) = "))
    faktor_buret = float(input("faktor buret = "))
    faktor_NaOH = float(input("faktor NaOH = "))
    acid_value = (jumlah_titran * faktor_buret * faktor_NaOH * 5.61) / berat_sample
    keputusan = 'OK' if acid_value < 7.0 else 'NG'
    return f"{keputusan} dengan nilai acid value: {acid_value} pada waktu {waktu} di suhu {suhu}\xb0C"