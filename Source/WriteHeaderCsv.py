# This class handles writing the Excel Header
# File Nodes.csv will be used
# Mick Shannon
# 04/11/2022
## Function to write out the CSV header section ###
import csv

class write_header():    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        self.debug = False
    
    def writeheader(self)->int :
        header = ['Mac Address', 'IP Address', 'Computer', 'Manufacturer']
        with open('nodes.csv', 'w+') as fv:
            writer = csv.writer(fv)
            # write the header
            try:
                writer.writerow(header)
            except:
                return 1
            finally:
                fv.close()
## End of Function to write out the CSV header section ###
