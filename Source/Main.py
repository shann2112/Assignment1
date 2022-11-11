'''
L00177543
Michael Shannon Assignment 1
This is the main file which runs our program
It calls on the MAc Class to find realtime mac manufacturers
and uses write classes to write to CSV file
This program iterates through a text file and pulls back
Ip, Mac andComputer text. We then do a lookup on the Manufacture in real time
28/10/2022
'''
from operator import pos
import sys
from GetMacClass import GetMac
from WriteHeaderCsv import write_header
from WriteDataCsv import write_data
from pathlib import Path
import re, mmap, os, csv

### Set up a few variables to hold values ###
my_comparision = []
my_ipaddress = ""
my_macaddress = ""
my_computername = ""
my_manufacturer = ""
### Finished setting up variables ###

### Lets call on our classes ###
my_class = GetMac()
my_header = write_header()
my_data = write_data()
### Finished call on our class ###

def print_me(Theinfo:str):
    ### now lets write all the data collected to a line in the CSV file. This calls a class to do the work. ###    
    if my_data.write_linetocsv(Theinfo) == 1:
        print(' Error while writing to the CSV file, terminating program')
        sys.exit()

### The Main section is called directly ###
if (__name__ == '__main__'):
    
    ### Lets call the class t0 update our mac vendors. This is saved to a file called ###
    ### mac-venders.txt and is done live. It might slow the progran dow by a couple of seconds ###
    if my_class.updatevendors() == 1:
        print(' Error while updating the Manufacturer text file, terminating program')
        sys.exit()

    ### Lets kick off by writing out the CSV header Class file ###
    if my_header.writeheader() == 1:
        print(' Error while writing the CSV Header, terminating program')
        sys.exit()
    
    ### Set the file path to read from and clear the therminal window ###
    filepath = Path(__file__).parent / "4654605.txt"
    os.system('cls')

    ### This is the main section which does all the work. I open the file to read in the data ###
    ### Once read in, I seek and find locations to extract the data I need ###
    with open(filepath, "r") as f:
        f.seek(0)
        for rec in f:
            ### type 1 search on DHCPARK ON and DHCPARK TO ###
            ### DHCPACK to 192.168.5.21 (c0:25:a5:66:81:fc) via eth0 ###
            ### Lets look at TO and use a start and end position ###
            poDHCPACK = (rec.find('DHCPACK',0))
            poDHCPACK2 = (rec.find('to',0))
            
            ### if we find a match then continue ###
            if poDHCPACK != -1:
                ### if shorter line then this needs to be captures. There will be no Computer name here ###
                ### This will be the DHCPARK ON Section ###
                if poDHCPACK2 - poDHCPACK < 10 : # the start position  - end is less than 10
                    poDHCPACK2 = (rec.find('(',0)) 
                    
                    # reposition pointers
                    poDHCPACK +=11
                    poDHCPACK2 += -1
                   
                    ### We capture the IP Address here ###
                    my_ipaddress = (rec[poDHCPACK:poDHCPACK2])

                    # lets get mac address need to move pointerd down the list we will add to previous values.
                    # we take last position and make it start position and move pointers
                    poDHCPACK = poDHCPACK2 +2
                    poDHCPACK2 = poDHCPACK +17
                    
                    ### lets get the MAc address now and send it to a class to find the Manufacturer ###
                    ### In this section there is no Computer name ###
                    my_macaddress = (rec[poDHCPACK:poDHCPACK2]) 
                    
                    # Check for MAC replication, do nothing if found.
                    if my_macaddress in my_comparision:
                        continue
                    else:
                        my_comparision.append(my_macaddress)
                        my_manufacturer = my_class.find_mac(my_macaddress)
                        my_computername = 'None'  
                    
                    ### now lets write all the data collected to a line in the CSV file. This calls a class to do the work. ###          
                    print_me(my_ipaddress+' '+my_macaddress+' '+my_computername+' '+my_manufacturer)
                else:
                    ### long line and this will have a computer name this is DHCPARK TO section ###
                    ### DHCPACK on 192.168.5.168 to c8:4b:d6:0a:77:2d (A-76MRRL3) via eth0 ###
                    ### Reposition the seek to get to the correct location
                    poDHCPACK +=11
                    poDHCPACK2 += -1
                    
                    ### We capture the IP Address here ###
                    my_ipaddress = (rec[poDHCPACK:poDHCPACK2])
                    # lets get mac address need to move pointerd donw the list we will add to previous values.
                    poDHCPACK = poDHCPACK2 +4
                    poDHCPACK2 = poDHCPACK +17
                    
                    ### lets get the MAc address now and send it to a class to find the Manufacturer ###
                    my_macaddress = (rec[poDHCPACK:poDHCPACK2])
                    if my_macaddress in my_comparision:
                        continue
                    else:
                        my_comparision.append(my_macaddress)
                        my_manufacturer = my_class.find_mac(my_macaddress)
                    
                    ### need to check if there is a computer name on this line. ###
                    ### if we can find a '(' then there is a name otherwise there is none ###
                    ### get computer name. We move the pointer again to location ##
                    poDHCPACK = poDHCPACK2 +2
                    poDHCPACK2 = (rec.find(')',0))
                    if poDHCPACK2 != -1:
                        ### we have found the computer name ###
                        my_computername = (rec[poDHCPACK:poDHCPACK2])        
                    else:
                        ### No name of computer found so lets call it None ###
                        my_computername = 'None'
                    
                    ### now lets write all the data collected to a line in the CSV file. This calls a class to do the work. ###          
                    print_me(my_ipaddress+' '+my_macaddress+' '+my_computername+' '+my_manufacturer)
 
        with open(filepath, "r") as f:
            f.seek(0)
            for rec in f:
                ## Part 2 lookup Requests now 
                ### type 1 search on DHCPARK ON and DHCPARK TO ###
                ### Lets look at TO and use a start and end position ###
                
                poDHCPREQUEST = (rec.find('DHCPREQUEST',0))
                poDHCPREQUEST2 = (rec.find('from',0))  
                
                 ### if we fin a match then continue ###
                if poDHCPREQUEST != -1:                  
                    if (poDHCPREQUEST2 >70) :
                        # DHCPREQUEST for 192.168.5.220 (192.168.6.21) from bc:5f:f4:45:7c:1e via 192.168.5.10
                        # the IP has brackets around it and has pushed the FROM forward  
                        # we need to reposition the pointer back and find the start bracked ( then offset pointers
                        poDHCPREQUEST2 = (rec.find('(',0)) 
                        poDHCPREQUEST +=16
                        poDHCPREQUEST2 += -1
                        my_ipaddress = (rec[poDHCPREQUEST:poDHCPREQUEST2])                         
                        # lets get mac address need to move pointerd down the list we will add to previous values.
                        poDHCPREQUEST = (rec.find(')',0)) 
                        poDHCPREQUEST +=7
                        poDHCPREQUEST2 = poDHCPREQUEST +17
                        ### lets get the MAc address now and send it to a class to find the Manufacturer ###
                        my_macaddress = (rec[poDHCPREQUEST:poDHCPREQUEST2])                        
                        if my_macaddress in my_comparision:
                            continue
                        else:
                            my_comparision.append(my_macaddress)
                            my_manufacturer = my_class.find_mac(my_macaddress)
                        ### No name of computer found so lets call it None ###
                        my_computername = 'None'                         
                        ### now lets write all the data collected to a line in the CSV file. This calls a class to do the work. ###          
                        print_me(my_ipaddress+' '+my_macaddress+' '+my_computername+' '+my_manufacturer)    
                    else :
                        poDHCPREQUEST +=16
                        poDHCPREQUEST2 += -1
                        my_ipaddress = (rec[poDHCPREQUEST:poDHCPREQUEST2])     
                        # lets get mac address need to move pointerd down the list we will add to previous values.
                        poDHCPREQUEST = poDHCPREQUEST2 +6
                        poDHCPREQUEST2 = poDHCPREQUEST +17                                                                                
                        ### lets get the MAc address now and send it to a class to find the Manufacturer ###
                        my_macaddress = (rec[poDHCPREQUEST:poDHCPREQUEST2])                        
                        if my_macaddress in my_comparision:
                            continue
                        else:
                            my_comparision.append(my_macaddress)
                            my_manufacturer = my_class.find_mac(my_macaddress)
                        ### need to check if there is a computer name on this line. ###
                        ### if we can find a '(' then there is a name otherwise there is none ###
                        ### get computer name. We move the pointer again to location ##
                        poDHCPREQUEST = poDHCPREQUEST2 +2
                        poDHCPREQUEST2 = (rec.find(')',0))                       
                        if poDHCPREQUEST2 != -1:
                            ### we have found the computer name ###
                            my_computername = (rec[poDHCPREQUEST:poDHCPREQUEST2])        
                        else:
                            ### No name of computer found so lets call it None ###
                            my_computername = 'None' 
                        ### now lets write all the data collected to a line in the CSV file. This calls a class to do the work. ###          
                        print_me(my_ipaddress+' '+my_macaddress+' '+my_computername+' '+my_manufacturer)                                                          
else:
    print(f"This module executes as a standalone script")
### End of Main section ###
