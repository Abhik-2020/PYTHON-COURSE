#            list comprehensions
#create a list containing the table of 5

#this is a first way to right a table on list (this is simple to read)

# table = []
# for i in range (1,11):
#     table.append(5*i)
# print(table)

#this is a second way to right a table on list (this is one line code to write a table on the list)

table = [5*i for i in range (1,11)]
print(table)



