from collections import Counter

# read the text file
with open('C:/Users/gardn/Documents/honeypot/countries.txt') as f:
    lines = f.readlines()

# count the occurrences of each country code
country_counts = Counter([line.strip().split(',')[0].strip() for line in lines])

# write the country codes and their counts to a file
with open('C:/Users/gardn/Documents/honeypot/countrycount.txt', 'w') as f:
    for code, count in country_counts.most_common():
        f.write(f"{code}: {count}\n")