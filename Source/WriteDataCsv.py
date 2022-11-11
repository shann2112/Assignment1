# This class handles writing out lines of data to Nodes.csv
# It also adds in the comma for Excel
# Mick Shannon
# 04/11/2022
## Function to write out the CSV Data section ###
import csv

class write_data():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        self.debug = False

    def write_linetocsv(self, my_line:str)->int:
        with open('nodes.csv', 'a+',newline='') as fv:
            writer = csv.writer(fv, quoting = csv.QUOTE_NONE, escapechar=',')
            # write the data
            try:
                writer.writerow(my_line.split())
            except:
                return 1
            fv.close()
## End of Function to write out the CSV Data section ###
