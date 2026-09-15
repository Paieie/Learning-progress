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
# def error_checking(target_list, device_inventory):
#     for ip in target_list:
#         try:
#             #checking to see if it belongs to the 192.168.1.x subnet
#             if  (float(device_inventory[ip]["firmware_version"][1:]) < 15.1 or device_inventory[ip]["device_type"] == "Router") and ip.startswith("192.168.1.") and ip in device_inventory:
#                 print(f"IP {ip} needs to be checked")
#             else:
#                 pass
#         except KeyError as e:
#             print(f"[{e}] IP {ip} not found in inventory")
#         except TypeError as e:
#             print(f"[{e}] Invalid IP target encountered: <{ip}>")
#         except Exception as e:
#             print(f"[{e}] An unexpected error occurred while processing IP: <{ip}>")
            
# After having it checked learned that this function has some issues and can be improved:
    # Short-Circuit Logical 
        # Error (ip in device_inventory placed at the end)In Python, conditions inside an if statement are evaluated left-to-right. In your code, device_inventory[ip] is accessed before Python evaluates ip in device_inventory. When ip = "invalid_ip_format", Python immediately raises a KeyError at the start of the if statement, rendering the check and ip in device_inventory useless.
    # Subnet Check Placement 
        # Your ip.startswith("192.168.1.") is also placed at the end of the if expression. Because of this, the code converts firmware strings to floats for non-matching IPs (like 10.0.0.1 or 172.16.0.1) before verifying if they even belong to the target subnet.
    # Float Conversion Risk
        # Parsing semantic version strings via float(firmware[1:]) works for v15.2 (15.2), but it breaks on semantic versions with multiple dots (e.g., v15.2.1 raises a ValueError).        
    # Exception Variable Printing
        # In Python, printing f"[{e}]" outputs the raw key or string representation (e.g., ['invalid_ip_format']). In network automation logging, explicit message tags like [KEY_ERROR] or [INVALID_INPUT] are preferred for readability.
    # Redundant Statements
        # The else: pass block is redundant in Python and should be omitted.
            
# Testing
# error_checking(target_device_list, device_inventory)

# Revised Solution
import logging 

TARGET_SUBNET = "192.168.1."
MIN_FIRMWARE_VERSION = "15.1"

def version_splitter(version_str: str) -> list:
    """Splits a version string into a list of integers for comparison."""
    return [int(part) for part in version_str.lstrip("v").split(".")]

def audit_network_devices(target_list: list, device_inventory: dict) -> None:
    for ip in target_list:
        try:
            # Checking if IP is a non-empty string
            if not isinstance(ip, str) or not ip.replace(".", "").isdigit():
                raise ValueError("Invalid IP target encountered")
            
            # Checking if the IP is in the device inventory
            if ip not in device_inventory:
                raise KeyError(f"IP {ip} not found in inventory")
            
            # By here we can be sure that the ip exists in the device_inventory so now we focus on filtering the device that needs to be flagged
            device = device_inventory[ip]
            
            # Checking if the device fits the subnet
            if not ip.startswith(TARGET_SUBNET):
                continue  # Skip devices not in the target subnet
            
            # Converting version
            raw_version = version_splitter(device["firmware_version"])
            
            # Condition checking
            is_outdated = False
            for number in version_splitter(MIN_FIRMWARE_VERSION):
                if raw_version < version_splitter(MIN_FIRMWARE_VERSION):
                    is_outdated = True
                    break
                elif raw_version > version_splitter(MIN_FIRMWARE_VERSION):
                    is_outdated = False
                    break
                
            is_router = device["device_type"].lower() == "router"
            if is_outdated or is_router:
                print(f"IP {ip} needs to be checked")            

        except KeyError as err:
            print(f"[KEY_ERROR] {err}")
        except TypeError as err:
            print(f"[INVALID_INPUT] {err}")
        except Exception as err:
            print(f"[UNEXPECTED_ERROR] Failed processing target <{ip}>: {err}")
        
        
# Testing the revised function
audit_network_devices(target_device_list, device_inventory)
        
        