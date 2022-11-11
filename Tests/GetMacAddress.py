'''
Mick Shannon 
This scritp returns the manufacture of the passed in MAC address
24/10/22
'''
from mac_vendor_lookup import MacLookup, BaseMacLookup
BaseMacLookup.cache_path = "mac-venders.txt"
mac = MacLookup()
mac.update_vendors()  # <- This can take a few seconds for the download

def find_mac(mac_address):
    print(mac.lookup(mac_address))

