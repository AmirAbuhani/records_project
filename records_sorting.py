from reading_csv_log_message import read_csv, log_message


def sorting_records():
    data = read_csv()
    # Sort the filtered DataFrame lexicographically by the 'RECORD_NAME' column
    if data.empty:
        print("There is no records for lexicographical sort ")
        log_message("Print Failure")

    # Convert 'RECORD_NAME' column to lowercase for case-insensitive sorting
    data['RECORD_NAME'] = data['RECORD_NAME'].str.lower()
    sorted_data = data.sort_values(by='RECORD_NAME')
    for index, row in sorted_data.iterrows():
        log_message(f"PrintAll {row['RECORD_NAME']} {row['AMOUNT']}")
    print(sorted_data)


#sorting_records()
