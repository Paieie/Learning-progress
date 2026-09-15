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