import re

# regular expression pattern for matching IP addresses
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'


# set to keep track of IP addresses that have been written to the output file
seen_ips = set()

with open('C:/Users/gardn/Documents/honeypot/ouput json files/cowrie03-06.txt', 'r', encoding='utf-8') as input_file:
    with open('C:/Users/gardn/Documents/honeypot/ListIP.txt', 'a', encoding='utf-8') as output_file:
         for line in input_file:
            # find all IP addresses in the current line
            ip_addresses = re.findall(ip_pattern, line)
            # write each unique IP address to the output file on a new line
            for ip_address in ip_addresses:
                if ip_address not in seen_ips:
                    output_file.write(ip_address + '\n')
                    seen_ips.add(ip_address)
       



