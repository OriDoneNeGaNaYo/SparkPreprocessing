from pyspark import SparkConf, SparkContext
import os
import pandas as pd

conf = SparkConf().setMaster("local").setAppName("bus-stop")
sc = SparkContext(conf=conf)

directory = f"{os.getcwd()}/data"
csv_file = "bus.csv"


def preprocessing():
    data = sc.textFile(f"file:///{directory}/{csv_file}")
    header = data.first()
    filetred_lines = data.filter(lambda row: row != header)

    return filetred_lines
    
def count():
    lines_split = preprocessing().map(lambda x: x.split(",")[-1])
    count = lines_split.countByValue()
    
    return count