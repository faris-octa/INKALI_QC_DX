from datetime import datetime

#### Dummy Datasources ####
# coa = {
#     {'SecItemNumber': '12345',
#      'ProductName': 'Amipole S',
#      'params': ['Appearance', 
#                 'Solid Content', 
#                 'pH 100%', 'pH 5%', 
#                 'Viscosity', 
#                 'Appearance 5%Solution', 
#                 'Filtration Test (Black Cotton)']}, 
#     {'SecItemNumber': '6789',
#      'ProductName': 'Sunsoflon WP',
#      'params': ['Appearance', 
#                 'Solid Content', 
#                 'pH 100%', 'pH 5%', 
#                 'Viscosity', 
#                 'Appearance 5%Solution']}
#     }

coa = []
###########################


class Qc:
    def __init__(self, SecItemNumber):
        self.SecItemNumber = SecItemNumber

    def get_SecItemNumber(self):
        return self.SecItemNumber
    
    def get_product_name(self):
        #cari di dictionary SecItemNumber == self.SecItemNumber
        coa['SecItemNumber'] == self.SecItemNumber
        for item in coa:
            if item['SecItemNumber'] == self.SecItemNumber:
                return item['ProductName']
    
qc1 = Qc(12345)

print('Second Item Number: ', qc1.get_SecItemNumber())
print('Product Name: ', qc1.get_product_name())


def appearance():
    appearance = input('Appearance = ')
    return appearance

def solid_content():
    berat_piringan = int(input('berat piringan = '))
    berat_basah = int(input('berat basah = '))
    berat_oven = int(input('berat kering = '))
    solid_content = (berat_basah - berat_oven)/berat_piringan * 100
    return solid_content

def viscosity():
    spindle = input('spindle = ')
    angka_terukur = int(input('angka terukur = '))
    viscosity = spindle * angka_terukur
    return viscosity

def acid_value():
    waktu = datetime.now().strftime("%H:%M")
    suhu = input("suhu = ")
    berat_sample = berat_sample (gr) 4 desimal
    jumlah_titran = jumlah_titran (ml) 2 desimal
    faktor_buret = faktor_buret
    faktor_NaOH = faktor_NaOH
    acid_value = (jumlah_titran * faktor_buret * faktor_NaOH * 5.61) / berat_sample
    keputusan = 'OK' if acid_value < 7.0 else 'NG'
    return f"{keputusan} dengan nilai acid value: {acid_value} pada waktu {waktu} di suhu {suhu}derajat C"

