#docstring that tells you what this file should do
"""Generate sales report showing total melons each salesperson sold."""

#create an empty list and assign to variable name salespeople
salespeople = []
#create an empty list and assign to variable name melons_sold
melons_sold = []

#opens a file inputted as a string and assign to variable name f
f = open('sales-report.txt')

#iterate for each line in previously defined opened file
for line in f:
    #remove whitespace from the right
    line = line.rstrip()
    #create a list of items, where items are defined by | as the separator
    entries = line.split('|')
    #isolate name from list
    salesperson = entries[0]
    #isolate number of melons sold
    melons = int(entries[2])

    #if name already exists in list called salespeople
    if salesperson in salespeople:
        #find the index of where the name is in the list and assign to variable name position
        position = salespeople.index(salesperson)
        #update number of melons sold
        melons_sold[position] += melons

    #otherwise, add name to salespeople list and number of melons sold to melons_sold list    
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# iterate based on the length of the salespeople list less 1
for i in range(len(salespeople)):
    #print a message saying how much each person sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# Improvement Ideas:
    # Use a dictionary where key = name, values = sales amount, number of melons sold
        #Solves issue of dealing with two lists where mismatches or uneven lists can happen
    # Make it flexible with any text file by importing sys and using sys.argv
    # Refine variable names to hint about what they are