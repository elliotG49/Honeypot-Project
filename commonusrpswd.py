from collections import Counter

# Define input and output file names
input_file = 'C:/Users/gardn/Documents/honeypot/versions.txt'
output_file = 'C:/Users/gardn/Documents/honeypot/mostcommonversions.txt'

# Read data from the input file
with open(input_file, 'r', encoding='utf-8') as f:
    data = f.read()

# Count entries in the data
entries = Counter(data.splitlines())

# Write the top 10 entries to the output file
with open(output_file, 'w', encoding='utf-8') as out_file:
    for entry, count in entries.most_common(10):
        out_file.write(f'{entry}: {count}\n')
