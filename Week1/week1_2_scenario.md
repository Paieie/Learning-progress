**Lab Exercise: Network Device Config Auditor**

**Scenario**
You are a Junior Network Automation Engineer at **Apex Tech**. Your team maintains a mixed network environment of core switches, firewalls, and legacy branch routers.

During a recent network sweep, the security team flagged that several legacy devices on the `192.168.1.x` subnet are using outdated firmwares or untracked hostnames. Your task is to write a Python script that iterates through a provided list of network targets, filters out high-risk legacy targets matching specific conditions, and safely logs them without letting bad data crash the script.

---

**Target Device List**
Your script must process the following raw IP targets (note: some entry formats contain bad data):

* `192.168.1.1`
* `10.0.0.1`
* `192.168.1.25`
* `invalid_ip_format`
* `172.16.0.1`
* `192.168.1.100`
* `None`

---

**Device Inventory Data**
Use the following dictionary mapping IP addresses to device attributes:

```python
device_inventory = {
    "192.168.1.1": {"hostname": "Core-Switch-01", "firmware_version": "v15.2", "device_type": "Switch"},
    "10.0.0.1": {"hostname": "Datacenter-GW", "firmware_version": "v16.1", "device_type": "Router"},
    "192.168.1.25": {"hostname": "Legacy-Branch-Router", "firmware_version": "v12.4", "device_type": "Router"},
    "172.16.0.1": {"hostname": "HQ-Firewall", "firmware_version": "v16.0", "device_type": "Firewall"},
    "192.168.1.100": {"hostname": "Branch-Switch-02", "firmware_version": "v15.0", "device_type": "Switch"}
}

```

---

**Exercise Requirements**

1. **Looping:** Iterate through the raw target list item by item.
2. **Matching Conditions:** Flag and print a warning message for a device ONLY if it meets **all** of the following conditions:
* Belongs to the `192.168.1.x` subnet (starts with `"192.168.1."`).
* Running a firmware version lower than `"v15.1"` **OR** has a device type equal to `"Router"`.


3. **Error Handling (`try/except`):**
* Wrap the inventory lookup and validation logic inside a `try/except` block.
* If a target IP isn't found in `device_inventory` (a `KeyError`), handle it gracefully with a message like: `[ERROR] IP <ip> not found in inventory.`
* If an input target is invalid/malformed (e.g., non-string, `TypeError`, or invalid format), catch the exception and print: `[ERROR] Invalid IP target encountered: <target>.`
* Ensure the loop continues to the next item after catching an exception instead of terminating.



---