import csv
header = ['Mac Address', 'IP Address', 'Computer']
data = ['Afghanistan', 652090, 'AF']
data2 = ['Afghanistan', 652090, 'AF']
with open('mac.csv', 'a+',newline='') as fv:
    writer = csv.writer(fv)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)
    writer.writerow(data2)

#
# print My_Csv(*a, sep = "\n")
fv.close()
