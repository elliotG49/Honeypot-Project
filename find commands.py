import codecs

input_file_path = 'C:/Users/gardn/Documents/honeypot/log files/cowrie.log.2023-04-06'
output_file_path = 'C:/Users/gardn/Documents/honeypot/commands found/commands0406.txt'

with codecs.open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file, \
     codecs.open(output_file_path, 'w', encoding='utf-8', errors='ignore') as output_file:
    
    for line in input_file:
        if "Command found" in line:
            command = line.split("Command found: ")[1].strip()
            output_file.write(command + "\n")