# Open the input file for reading
with open('C:/Users/gardn/Documents/honeypot/listofpasswords.txt', 'r') as f:

    # Create a dictionary to store the counts of each username
    counts = {}

    # Loop over each line in the file
    for line in f:
        # Split the line into username and count if possible
        elements = line.strip().split(': ')
        if len(elements) == 2:
            username, count = elements
            # Add the count to the existing count for this username
            counts[username] = counts.get(username, 0) + int(count)

# Sort the dictionary by count in descending order
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# Open the output file for writing
with open('C:/Users/gardn/Documents/honeypot/commonpasswords.txt', 'w') as f:

    # Write the top 10 most used usernames and their counts to the file
    for username, count in sorted_counts[:10]:
        f.write(f'{username}: {count}\n')