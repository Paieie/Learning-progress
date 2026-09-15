# This is the initial information based on the week1_2_scenario file
target_device_list = ["192.168.1.1",
                      "10.0.0.1",
                      "192.168.1.25",
                      "invalid_ip_format",
                      "172.16.0.1",
                      "192.168.1.100",
                      None]

device_inventory = {
    "192.168.1.1": {"hostname": "Core-Switch-01", "firmware_version": "v15.2", "device_type": "Switch"},
    "10.0.0.1": {"hostname": "Datacenter-GW", "firmware_version": "v16.1", "device_type": "Router"},
    "192.168.1.25": {"hostname": "Legacy-Branch-Router", "firmware_version": "v12.4", "device_type": "Router"},
    "172.16.0.1": {"hostname": "HQ-Firewall", "firmware_version": "v16.0", "device_type": "Firewall"},
    "192.168.1.100": {"hostname": "Branch-Switch-02", "firmware_version": "v15.0", "device_type": "Switch"}
}

# Making a function that checks each IP address in the target device list against the description.
def error_checking(target_list, device_inventory):
    for ip in target_list:
        try:
            #checking to see if it belongs to the 192.168.1.x subnet
            if  (float(device_inventory[ip]["firmware_version"][1:]) < 15.1 or device_inventory[ip]["device_type"] == "Router") and ip.startswith("192.168.1.") and ip in device_inventory:
                print(f"IP {ip} needs to be checked")
            else:
                pass
        except KeyError as e:
            print(f"[{e}] IP {ip} not found in inventory")
        except TypeError as e:
            print(f"[{e}] Invalid IP target encountered: <{ip}>")
        except Exception as e:
            print(f"[{e}] An unexpected error occurred while processing IP: <{ip}>")
            
            
# Testing
error_checking(target_device_list, device_inventory)