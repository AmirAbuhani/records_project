from reading_csv_log_message import read_csv, log_message


def search(sub_record_name):
    data = read_csv()
    # Filter the DataFrame to include only the rows where 'RECORD_NAME' contains the specified substring
    filtered_data = data[data['RECORD_NAME'].str.contains(sub_record_name)]
    if filtered_data.empty:
        print("No records found containing the specified substring.")
        log_message("Search Failure")
        return
    # Sort the filtered DataFrame lexicographically by the 'RECORD_NAME' column
    sorted_data = filtered_data.sort_values(by='RECORD_NAME')

    print(f"This list is sorted lexicographically, which contains the {sub_record_name} string in the record name: \n")
    # Print the sorted DataFrame
    print(sorted_data)
    log_message("Search Success")


def update_name(old_name, new_name):
    data = read_csv()
    list_records = data["RECORD_NAME"].to_list()
    if old_name in list_records:
        print(data[data["RECORD_NAME"] == old_name])
        record_number = int(input("which record do you want to update? "))
        # get the relevant row
        get_record = data.iloc[record_number]
        # get the name of the specific record
        get_record_name = get_record["RECORD_NAME"]
        # update the old name to the new name
        get_record_name = new_name
        # update the change to the record
        data.at[record_number, "RECORD_NAME"] = get_record_name
        # update the csv file
        data.to_csv("saving_records.csv", index=False)
        print("Updating record name has been successfully!")
        log_message("UpdateName Success")
    else:
        print("This record name is not exists in the records ")
        log_message("UpdateName Failure")

# update_name("Beatles", "New_beatles")
# record_search("eat")
