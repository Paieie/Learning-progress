ip_addresses = [
    {"ip_address": "192.168.1.1",
     "subnet_mask": "255.255.255.0",
     "ip_class": "Class C",
     "use_desc": "Primary home or small office default gateway"
     },
    {"ip_address": "192.168.2.1",
         "subnet_mask": "255.255.255.0",
         "ip_class": "Class C",
         "use_desc": "Secondary subnet, guest network, or secondary access point"
         },
    {"ip_address": "10.0.0.1",
         "subnet_mask": "255.0.0.0",
         "ip_class": "Class A",
         "use_desc": "Enterprise core router, datacenter gateway, or ISP modem/router"
         },
]

def ip_list(list):
    for ip in range(0,len(list)):
        print(f"ip address: {list[ip]["ip_address"]}")
        print(f"subnet mask: {list[ip]["subnet_mask"]}")
        print(f"ip class: {list[ip]["ip_class"]}")
        print(f"use case:{list[ip]["use_desc"]}")
        print("----------")
   
# ip_list(ip_addresses)

# Better and faster one here:     
list_B = {
    "ip_addr": {
        "subnet_mask": "smth",
        "ip_class": "smth",
        "use_desc": "smth"
    },
    "ip_addrs": {
            "subnet_mask": "smth",
            "ip_class": "smth",
            "use_desc": "smth"
        },
    "ip_addrss": {
            "subnet_mask": "smth",
            "ip_class": "smth",
            "use_desc": "smth"
        }
}
# make sure that the keys are unique, otherwise the last one will overwrite the previous ones.

def ip_list2(list):
    for ip, ip_info in list.items():
        print(f"ip address: {ip}")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
        print("----------")    

ip_list2(list_B)        
        
