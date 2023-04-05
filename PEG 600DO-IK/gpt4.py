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

def get_input_data():
    print("\nEnter the following information:")
    
    LOT = input("LOT (string): ")
    Operator = input("Operator (string): ")
    Faktor_buret = float(input("Faktor buret (float): "))
    Faktor_NaOH = float(input("Faktor NaOH (float): "))
    Reaksi = input("Reaksi (string): ")
    Berat_sample = float(input("Berat sample (float): "))
    Jumlah_titran = float(input("Jumlah titran (float): "))

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
    
    return input_data

def main():
    data_list = []
    columns = ["LOT", "Operator", "Faktor buret", "Faktor NaOH", "Reaksi", "Berat sample", "Jumlah titran", "AV", "Instruksi"]
    df = pd.DataFrame(columns=columns)

    while True:
        input_data = get_input_data()
        data_list.append(input_data)
        new_data = pd.DataFrame([input_data], columns=columns)
        df = pd.concat([df, new_data], ignore_index=True)

        print("\nCurrent tabular data:")
        print(df)

        exit_prompt = input("\nDo you want to add another input session? (Enter 'Y' to continue or any other key to exit): ")
        if exit_prompt.lower() != 'y':
            break

    print("\nFinal tabular data:")
    print(df)

if __name__ == "__main__":
    main()