># Description
The Project was to identify every device on a client (192.168.5.0/24) and CCTV (192.168.12.0/24) network. This file was produced by John ORaw from his home router. There are 100 lines of output and consists of several headings. 
1.	DHCPARK
2.	UDI LEASE
3.	DHCPREQUEST
4.	DHCPINFORM
5.	DHCPDISCOVER
6.	DHCPOFFER

Once the file was read, then all unique MAC address should be collected and written out to Nodes.csv along with the IPaddress, Computer name and MAC manufacturer.

An example of this is ***Oct 20 15:19:51 dns1 dhcpd[1838]: DHCPACK on 192.168.5.168 to c8:4b:d6:0a:77:2d (A-76MRRL3) via eth0***

># Aims
The aims of this project are:

1.	With the headings above,  the object was to extract the computer name, Ip address, MAC address and the NIC manufacturer name by iterating through the text file 
2.	If there was no hostname, then” None” should be returned. 
3.	The MAC address must be examined, and the manufacturer’s name has to be found for this address. For example, in the above line, write out: ***c8:4b:d6:0a:77:2d, 192.168.5.168, A-76MRRL, Dell***
4.	In some cases, there are unique MAC addresses but there are NO hostnames. 
5.	Wherever you find information about a unique node, output it to a CSV file called nodes.csv.
6.	Do not write out duplicates.

># Methodology
1.	A project structure was created using a DOS bat file to create the directories needed for this project. 
2.	A main.py was created and several Classes were created to take the workload away from main.py. 
3.	These classes(getmacaddress.py, write_header.py, writedata.py) look up MAC addresses and returned the manufacturer’s name and handle the data output to Nodes.csv.  
4.	The MAC manufacturer’s list was created at runtime and used the internet to download a current manufacturer list. 
5.	This main.py  file contained iterated code which loops through the log file. 

># Results and testing
1.	The program created a CSV file called Nodes.csv and 6 unique MAC addresses were written out to this file. It was evident after writing procedures on DHCKARK ON, DHCPARK TO, DHCPREQUEST(with one IP address), and DHCPREQUEST(with two IP addresses) that replication began to creep in. There was no need to create a procedure on UDI LEASE, DHCPINFORM, DHCPDISCOVER or DHCPOFFER as they contained the same MAC addresses used in the previous iterations.
2.	Several Python files were created at the start of this project to test Classes and get MAC manufacturers’ names and these files can be found in the TESTS Directory. This was the starting point to build up code.
3. By populating a MAC text file to get the Manufacturer from, added a few second delay in the programs execution. 
4.	John ORaw did give an example of code that would suit this project in a lecture, but I choose not to copy this code and instead used my own version.
5.	In the Class files I put in minor error checking on writing and reading to a CSV file.
6.	The CSV file can be examined in the PROJECT folder

># Conclusions
The student produced a working main.py which iterated through a text file produced from John ORaw’s router. Main.py called on several classes to help with the workload and made the code more readable. On execution of main.py, a CSV file was produced with 6 Unique MAC addresses. Overall, the project was a success and the results produced fitted the brief. As stated in Results and Testing, there was no need to continue producing more iteration code to go through the final headings as the results would be discarded due to MAC address replication. However, if needed these extra procedures can easily be coded and slotted in main.py. The code produced was heavily documented for any other developer to understand the flow and syntax of the program.
