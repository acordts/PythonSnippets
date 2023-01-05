import argparse
import re
class IPValidator:
    v4seq = r"(25[0-5]|(2[0-4]|1?\d)?\d)"
    v4addr = r"({v4}\.){{3}}{v4}".format(v4=v4seq)
    v4_regex = re.compile(r"^{v4}$".format(v4=v4addr))

    hex = r"[\da-fA-F]"
    v6seq = r"{hex}{{1,4}}".format(hex=hex)
    v6_regex = re.compile(
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
        r"({v6}:){{1,4}}:{v4addr})$".format(v4addr=v4addr, v6=v6seq, hex=hex))
    
    def is_valid_v4(self, ip_address):
        return self.v4_regex.match(ip_address) is not None

    def is_valid_v6(self, ip_address):
        return self.v6_regex.match(ip_address) is not None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", required=True, help="IP address to validate")
    args = parser.parse_args()
    validator = IPValidator()
    if validator.is_valid_v4(args.ip):
        print(f"{args.ip} is a valid IPv4 address")
    elif validator.is_valid_v6(args.ip):
        print(f"{args.ip} is a valid IPv6 address")
    else:
        print(f"{args.ip} is not a valid IP address")
