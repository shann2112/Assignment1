'''
L00177543

Michael Shannon Assignment 1
This is the main file which runs our program
It calls on the MAc Class to fin realtime mac manufacturers
This program iterates through a text file and pulls back
Ip, Mac andComputer text

28/10/2022
'''
from operator import pos
from GetMacClass import GetMac
from WriteHeaderCsv import write_header
from WriteDataCsv import write_data
from pathlib import Path
import re, mmap, os, csv

#my_class = GetMac()


### Set up a few variables to hold values ###
My_Csv = []
my_ipaddress = ""
my_macaddress = ""
my_computername = ""
my_manufacturer = ""
### Finished setting up variables ###

### Lets call on our MAc Lookup class and update the MAc-Vender.txt file ###
my_class = GetMac()
my_class.updatevendors()
my_header = write_header()
my_data = write_data()
### Finished call on our MAc Lookup class ###

### The Main section is called directly ###
if (__name__ == '__main__'):
    
   
    ## Function to write out the CSV header section ###
    def write_header():
        header = ['Mac Address', 'IP Address', 'Computer', 'Manufacturer']
        with open('mac.csv', 'w+') as fv:
            writer = csv.writer(fv)
            # write the header
            writer.writerow(header)
            fv.close()
    ## End of Function to write out the CSV header section ###
    
    def write_linetocsv(my_line:str):
        with open('mac.csv', 'a+',newline='') as fv:
            writer = csv.writer(fv, quoting = csv.QUOTE_NONE, escapechar=',')
            # write the data
            writer.writerow(my_line.split())
            fv.close()
    my_header.writeheader()
    # write_header()

    filepath = Path(__file__).parent / "4654605.txt"
    os.system('cls')
    with open(filepath, "r") as f:
        f.seek(0)
        for rec in f:
            # type 1 search on DHCPARK
            
            poDHCPACK = (rec.find('DHCPACK',0))
            poDHCPACK2 = (rec.find('to',0))
            if poDHCPACK != -1:
                # if shorter line then this nwwd to be captures. There will be no Computer name here
                if poDHCPACK2 - poDHCPACK < 10 :
                    poDHCPACK2 = (rec.find('(',0)) 
                    poDHCPACK +=11
                    poDHCPACK2 += -1
                    #print(f"IP Starts at {poDHCPACK} and ends at {poDHCPACK2}")
                    My_Csv.append(rec[poDHCPACK:poDHCPACK2])
                    my_ipaddress = (rec[poDHCPACK:poDHCPACK2])
                    # lets get mac address need to move pointerd donw the list we will add to previous values.
                    poDHCPACK = poDHCPACK2 +2
                    poDHCPACK2 = poDHCPACK +17
                    #print(f"MAc Starts at {poDHCPACK} and ends at {poDHCPACK2}")
                    My_Csv.append(rec[poDHCPACK:poDHCPACK2])
                    #My_Csv.append(""+os.linesep)
                    my_macaddress = (rec[poDHCPACK:poDHCPACK2]) 
                    my_manufacturer = my_class.find_mac(my_macaddress)
                    #my_manufacturer = re.sub(",","",my_manufacturer)
                    my_computername = 'None'   
                else:
                    # long line and this will have a computer name
                    poDHCPACK +=11
                    poDHCPACK2 += -1
                    #print(f"IP Starts at {poDHCPACK} and ends at {poDHCPACK2}")
                    My_Csv.append(rec[poDHCPACK:poDHCPACK2])
                    my_ipaddress = (rec[poDHCPACK:poDHCPACK2])
                    # lets get mac address need to move pointerd donw the list we will add to previous values.
                    poDHCPACK = poDHCPACK2 +4
                    poDHCPACK2 = poDHCPACK +17
                    #print(f"MAc Starts at {poDHCPACK} and ends at {poDHCPACK2}")
                    My_Csv.append(rec[poDHCPACK:poDHCPACK2])
                    my_macaddress = (rec[poDHCPACK:poDHCPACK2])
                    my_manufacturer = my_class.find_mac(my_macaddress)
                    #my_manufacturer = '"'+re.sub(",","",my_manufacturer)+'"'
                    # need to check if there is a computer name on this line.
                    # if we can find a '(' then there is a name otherwise there is none)
                    
                    # get computer name
                    
                    poDHCPACK = poDHCPACK2 +2
                    poDHCPACK2 = (rec.find(')',0))
                    if poDHCPACK2 != -1:
                        #poDHCPACK2 += -1
                        My_Csv.append(rec[poDHCPACK:poDHCPACK2])
                        my_computername = (rec[poDHCPACK:poDHCPACK2])
        
                    else:
                        My_Csv.append(""+os.linesep)
                        my_computername = 'None'
                    
                    my_data.write_linetocsv(my_ipaddress+' '+my_macaddress+' '+my_computername+' '+my_manufacturer)
                    #write_linetocsv(my_ipaddress+' '+my_macaddress+' '+my_computername+' '+my_manufacturer)
else:
    print(f"This module executes as a standalone script")
### End of Main section ###
