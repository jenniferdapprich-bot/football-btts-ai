import pandas as pd
import os

#Ordner mit den CSV-Dateien
DATA_PATH = "data/raw"

#Alle CSV-Dateien im Ordner auflisten
files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

# Alle Daten aus den CSV-Dateien in einen DataFrame laden
dataframes = []

for file in files:
    df = pd.read_csv(os.path.join(DATA_PATH, file))
    df["Season"] = file.replace(".csv", "")
    dataframes.append(df)

    # Alle DataFrames zu einem einzigen DataFrame zusammenführen
    matches = pd.concat(dataframes, ignore_index=True)

    # Erste Informationen über den DataFrame ausgeben
print("Anzahl Spiele:", len(matches))
print("\nSpalten:")
print(matches.columns)

print("\nErste 5 Zeilen:")
print(matches.head())


