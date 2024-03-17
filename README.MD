Author: Amir Abu Hani

The records project is consisting of several moduls. each module has its own functions that all will be using in the 
main app, which be the user's menu for choice the operations on the records file.

At first, we have the reading_csv_log_message module. this module is responsible for 2 things:
One is to open the saving_records.csv file and return the data from this file in order to deal with this data for the 
different operations(e.g. adding, deleting ...)
Second is the log_message function. this function will help to record every log that the user do, and write it in the 
saving_records_log.txt file.

Adding_records module is consisting from 2 functions. the primary function is adding_record which adding new record at
the end of the records fill if the records does not exist. if the records is existing, we drop it and update the record
amount and adding it in the end of the file. these functions are having an adding_row auxiliary function, which responsible 
for create single record and update the records file.

Deleting_records module is consisting from 2 functions. the primary function is main_deleting_record, which is responsible
for extract the amount field for specific record in order to update it if necessary. The check_amount auxiliary function
is comparing the exist records amount with the wanted to delete records and send the answer to the main_deleting_record.

The records_names module has 2 functions. each function is responsible about different things regarding the record name.
The search function filtered all the records name that have the sub string, and then do lexicographical sorting on the
result.
The update_name function show the user all the records that have the same record name. the user choice which record he
wants to update its name, and the function replace the old name in the new name, and updating the file records.

The records_amount module has 2 functions.  each function is responsible about different things regarding the record amount.
The update_amount function is updating the exist record amount for new amount if the record amount is up than 0.
The print_all_records_amount function is counting all the records and return the result.

The records_sorting module has the sorting_records function. this function takes all the records names(in lower case)
and sorted it in lexicographical sorting.

The main module is the user_interface. This interface show the user all the operations that he can do in the records file
(8 different operations). in accordance with his choice, the program do the relevant operation on the records.
this menu will be shown until the user is decided to exit from the program. 