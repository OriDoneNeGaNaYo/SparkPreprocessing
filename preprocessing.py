import os 
import pandas as pd 
from pathlib import Path


FILE_LOCATION = f"{Path(os.getcwd())}/data"
FILE = [data for data in os.listdir(FILE_LOCATION)]


def city_extract(filename):
    data = pd.read_csv(f"{FILE_LOCATION}/{filename}").values
    return [j for i in data for j in i]


def preprocessing(filename, csv_file):
    data = pd.read_csv(f"{FILE_LOCATION}/{filename}").drop(columns=["ename"])
    dd = [data[data["city"] == i] for i in csv_file]

    pd.concat(dd).to_csv("sgi_bus_station.csv", index=False, index_label=False)


    
if __name__ == "__main__":
    preprocessing(filename="english_korea_busstop.csv", 
                csv_file=city_extract(filename="gyoung.csv"))
