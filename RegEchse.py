### RegEx colletion

# IP Digits: 8-Bit int - 0 .. 255
ByteInt = "(\d|1\d{1,2}|2[0-4]\d|25[0-5])"

# IPv4 0.0.0.0 .. 255.255.255.255
Ipv4 = "(?<IPv4>((\d|1\d{1,2}|2[0-4]\d|25[0-5])\.){3}(\d|1\d{1,2}|2[0-4]\d|25[0-5]))$"