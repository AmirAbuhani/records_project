# Author: Amir Abu Hani
from adding_records import adding_record
from deleting_records import main_deleting_record
from records_names import search, update_name
from records_amounts import update_amount, print_all_records_amount
from records_sorting import sorting_records
from reading_csv_log_message import log_message

isContinue = True


def main():
    global isContinue
    while isContinue:
        user_choice = input(
            "Here is the operations that you can do in the records stock. Please chose the operation number:\n"
            "1. Adding Record\n"
            "2. Deleting Record\n"
            "3. Searching Record according to name\n"
            "4. Updating Record name\n"
            "5. Updating Record amount\n"
            "6. Show all the records amount\n"
            "7. Show the records by lexicographical sorting\n"
            "8. Exit from the program\n")
        try:
            user_choice = int(user_choice)
            if 1 <= user_choice <= 8:
                if user_choice == 1:
                    record_name = input("Enter your record name for insert: ")
                    record_amount = input("Enter the record amount for insert: ")
                    adding_record(record_name, record_amount)
                elif user_choice == 2:
                    record_name = input("Enter your record for deleting: ")
                    record_amount = input("Enter the record amount for deleting: ")
                    main_deleting_record(record_name, record_amount)
                elif user_choice == 3:
                    search_name = input("Enter your record name or subname for searching: ")
                    search(search_name)
                elif user_choice == 4:
                    old_name = input("Enter your record name for updating: ")
                    new_name = input("Enter your new record name for updating: ")
                    update_name(old_name, new_name)
                elif user_choice == 5:
                    record_name = input("Enter your record name for amount updating: ")
                    record_amount = input("Enter your new record amount for updating: ")
                    update_amount(record_name, record_amount)
                elif user_choice == 6:
                    total_records_amount = print_all_records_amount()
                    print(f"Total records amount in the file is: {total_records_amount} ")
                elif user_choice == 7:
                    sorting_records()
                elif user_choice == 8:
                    print("Exit from program. Thank you!")
                    log_message("Exit Success")
                    isContinue = False
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid choice. Please enter a number ")


if __name__ == "__main__":
    main()
