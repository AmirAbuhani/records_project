from reading_csv_log_message import read_csv, log_message


def update_amount(record_name, new_amount):
    data = read_csv()
    list_records = data["RECORD_NAME"].to_list()
    if record_name in list_records:
        print(data[data["RECORD_NAME"] == record_name])
        record_number = int(input("which record do you want to update? "))
        # get the relevant row
        get_record = data.iloc[record_number]
        # get the name of the specific record
        get_record_amount = get_record["AMOUNT"]
        if get_record_amount > 0:
            get_record_amount = new_amount
            data.at[record_number, "AMOUNT"] = get_record_amount
            # update the csv file
            data.to_csv("saving_records.csv", index=False)
            print("Updating record amount has been successfully!")
            log_message("UpdateAmount Success")
        else:
            print("Can not update amount. amount is 0")
            log_message("UpdateAmount Failure")
    else:
        print("This record name is not exists in the records")
        log_message("UpdateAmount Failure")


def print_all_records_amount():
    data = read_csv()
    list_amount = data["AMOUNT"].to_list()
    total_amount = 0
    if len(list_amount) == 0:
        print("There is no records in records stock")
        log_message(f"PrintAmount {total_amount}")
        return
    else:
        for amount in list_amount:
            total_amount += int(amount)
        log_message(f"PrintAmount {total_amount}")
        return total_amount


# update_amount("pink floyd", 30)
# amounts = print_all_records_amount()
# print(amounts)
