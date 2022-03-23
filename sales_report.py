#docstring that tells you what this file should do
# """Generate sales report showing total melons each salesperson sold."""

# #create an empty list and assign to variable name salespeople
# salespeople = []
# #create an empty list and assign to variable name melons_sold
# melons_sold = []

# #opens a file inputted as a string and assign to variable name f
# f = open('sales-report.txt')

# #iterate for each line in previously defined opened file
# for line in f:
#     #remove whitespace from the right
#     line = line.rstrip()
#     #create a list of items, where items are defined by | as the separator
#     entries = line.split('|')
#     #isolate name from list
#     salesperson = entries[0]
#     #isolate number of melons sold
#     melons = int(entries[2])

#     #if name already exists in list called salespeople
#     if salesperson in salespeople:
#         #find the index of where the name is in the list and assign to variable name position
#         position = salespeople.index(salesperson)
#         #update number of melons sold
#         melons_sold[position] += melons

#     #otherwise, add name to salespeople list and number of melons sold to melons_sold list    
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# # iterate based on the length of the salespeople list less 1
# for i in range(len(salespeople)):
#     #print a message saying how much each person sold
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# Improvement Ideas:
    # Use a dictionary where key = name, values = sales amount, number of melons sold
        #Solves issue of dealing with two lists where mismatches or uneven lists can happen
    
    # Make it flexible for any file input
        #Directly running the file uses sales-report.txt as default file input
        #Running file interactively allows for other files to be used as file input
        #Make it interactive to run from command line
            #Attempted to import sys and use sys.argv but leads to indexerror
                #Only works in command line if it has enough items
    
    # Refine variable names to hint about what they are

def generate_sales_data_report(file_input="sales-report.txt"):
    """Generates a report showing how many melons sold and the sales amount made by each person.
    
    By default, it runs the sales-report.txt file unless another file is specified.
    """
    sales_report_info = open(file_input)

    sales_data_by_person = {}

    for line in sales_report_info:
        sales_data = line.rstrip().split("|")

        name, sales_amount, melons_sold = sales_data
        melons_sold = int(melons_sold)

        sales_data_by_person[name] = sales_data_by_person.get(name, 0) + melons_sold
        print(f"{name} sold {melons_sold} melons, generating ${sales_amount} in sales!")

generate_sales_data_report()