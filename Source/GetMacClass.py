# This class handles mac address lookups
# It also strips out commas, spaces and full stops found in manufacturer name which would upset excel
# Mick Shannon
# 04/11/2022

# Start of Class
from mac_vendor_lookup import MacLookup, BaseMacLookup

class GetMac():
    # Define a class object attribute, it will be the same for any instance of the class
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        self.debug = False

    # lookup the Mac address from the list file to return the MAnufacturer
    def find_mac(self,mac_address):
        mac = MacLookup()
        my_text = mac.lookup(mac_address)
        my_text = my_text.replace(" ","-")
        my_text = my_text.replace(".,","-")
        my_text = my_text.replace(".","")
        my_text = my_text.replace(",","-")
        return my_text
        
    # Update the list first to pull in new Manufacturers
    def updatevendors(self) -> int:
        try:
            BaseMacLookup.cache_path = "mac-venders.txt"
            mac = MacLookup()
            mac.update_vendors()  # <- This can take a few seconds for the download
        except:
            return 1
# End of Class
