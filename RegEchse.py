### RegEx collection

# IP Digits: 8-Bit int - 0 .. 255
ByteInt = r"(25[0-5]|(2[0-4]|1?\d)?\d)"

# hexadecimal number
Hex = r"[\da-fA-F]"

# IPv4 0.0.0.0 .. 255.255.255.255
IPv4addr = r"({byteInt}\.){{3}}{byteInt}".format(byteInt=ByteInt)

IPv6seq = r"{hex}{{1,4}}".format(hex=Hex)

# IPv6 adress
IPv6addr = 
    r"^(({v6}:){{7}}{v6}|"
    r"({v6}:){{1,7}}:|"
    r"({v6}:){{1,6}}(:{v6})|"
    r"({v6}:){{1,5}}(:{v6}){{1,2}}|"
    r"({v6}:){{1,4}}(:{v6}){{1,3}}|"
    r"({v6}:){{1,3}}(:{v6}){{1,4}}|"
    r"({v6}:){{1,2}}(:{v6}){{1,5}}|"
    r"({v6}:)(:{v6}){{1,6}}|"
    r":((:{v6}){{1,7}}|:)|"
    r"fe80:(:({hex}|{v6})){{0,4}}%[\da-zA-Z]+|"
    r"::(ffff(:0{{1,4}})?:)?{v4addr}|"
    r"({v6}:){{1,4}}:{v4addr})$".format(v4addr=IPv4addr, v6=IPv6seq, hex=Hex)
    
