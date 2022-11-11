# Michael Shannon L00177543 Assignment 1 #
![img.png](atu.jpg)
---
The assignment is to identify every device on a client (192.168.5.0/24) and CCTV (192.168.12.0/24) network.
To do this, the program is going to trawl through the DHCP server log files which was provided by the lecturer.

>The exercise is to demonstrate writing Python code to read a text file. Iterate through this file and extract IpAddress, Mac address, and computer name if present.

**The Aims of this Assignment:**
1. Open the file for reading and retrieve specific information.
2. Open a CSV file to write out the results and wherever you find information about a unique node, output it to a CSV file called nodes.csv.
3. Do not write out duplicates.
4. Get the manufacturer of the ethernat card by looking up the MAC address.

>There is complexity in reading information from the file
- Some line headings such as DHCPARK have 2 forms of input.
- Some line headings such as DHCPREQUEST have 3 forms of input.

> In order to run this program, follow the instructions below.

1. Navigate to the project folder.
2. Open the folder and then go to the source directory. 
3. Run main.py in a therminal window to execute the code. 

*The results wiill be saved in a nodes.csv file with only unique mac address shown.*





