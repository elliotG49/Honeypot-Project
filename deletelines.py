filename = 'C:/Users/gardn/Documents/honeypot/countries.txt'

with open(filename, 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        words = line.split()[3:]
        new_line = ' '.join(words) + '\n'
        file.write(new_line)
    file.truncate()