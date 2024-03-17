from reading_csv_log_message import read_csv, log_message


def adding_row(data, record_name, amount):
    # create a new record, in accordance to the arguments
    new_raw = {"RECORD_NAME": record_name, "AMOUNT": amount}
    # Append the new row to the DataFrame
    data = data._append(new_raw, ignore_index=True)
    print("New Record added")
    # Save the modified DataFrame to the CSV file
    data.to_csv("saving_records.csv", index=False)


def adding_record(record_name, amount):
    data = read_csv()
    list_records = data["RECORD_NAME"].to_list()
    if record_name in list_records:
        print(data[data["RECORD_NAME"] == record_name])
        record_number = int(input("which record do you want to update? "))
        data = data.drop(index=record_number)
        data.to_csv("saving_records.csv", index=False)
        print("Old Record Removed!")
        adding_row(data, record_name, amount)
        log_message("Insert Success")
    else:
        adding_row(data, record_name, amount)
        log_message("Insert Success")

#adding_record("Micheal Jackson", 40)
