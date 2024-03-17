from reading_csv_log_message import read_csv, log_message


def check_amount(data, exists_amount, delete_amount, record_number):
    if exists_amount > delete_amount:
        exists_amount = exists_amount - delete_amount
        # Update the amount in the DataFrame
        data.at[record_number, "AMOUNT"] = exists_amount
        print("Successfully updating!")
        # update the csv file
        data.to_csv("saving_records.csv", index=False)
        log_message("Delete Success")
    elif exists_amount == delete_amount:
        # delete the record
        data = data.drop(index=record_number)
        # update the csv file
        data.to_csv("saving_records.csv", index=False)
        print("Record is deleting!")
        log_message("Delete Success")
    else:
        print("Can not update.The amount you are want to delete is more than the exists amount for this record")
        log_message("Delete Failure")


def main_deleting_record(record_name, amount):
    data = read_csv()
    list_records = data["RECORD_NAME"].to_list()
    if record_name in list_records:
        print(data[data["RECORD_NAME"] == record_name])
        record_number = int(input("which record do you want to update? "))
        # get the relevant row
        get_record = data.iloc[record_number]
        # get the amount of the relevant row
        get_record_amount = int(get_record["AMOUNT"])
        check_amount(data, get_record_amount, amount, record_number)

    else:
        print("This record is not exists ")
        log_message("Delete Failure")

#main_deleting_record("hi", 2)
