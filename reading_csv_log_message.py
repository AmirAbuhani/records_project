
import pandas
from datetime import datetime


def read_csv():
    data = pandas.read_csv("saving_records.csv")
    return data


def log_message(message):
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_entry = f"{current_time} {message}\n"
    with open("saving_records_log.txt", "a") as log_file:
        log_file.write(log_entry)
