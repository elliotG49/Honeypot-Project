import re
from collections import defaultdict

# Step 1: Extract login attempts
login_attempts = []
with open('C:/Users/gardn/Documents/honeypot/log files/cowrie.log.2023-04-05', 'r', encoding='utf-8') as f:
    for line in f:
        if 'login attempt' in line:
            login_attempts.append(line)

# Step 2: Extract usernames and passwords
usernames = []
passwords = []
for line in login_attempts:
    user_match = re.search(r"b'(\S+)/", line)
    pass_match = re.search(r"b'/(\S+)'", line)
    if user_match and pass_match:
        username = user_match.group(1)
        password = pass_match.group(1)
        usernames.append(username)
        passwords.append(password)

# Step 3: Count username and password occurrences
username_counts = defaultdict(int)
password_counts = defaultdict(int)
for username, password in zip(usernames, passwords):
    username_counts[username] += 1
    password_counts[password] += 1

# Step 4: Sort and save results to a file
with open('C:\\Users\\gardn\\Documents\\honeypot\\passwordlist\\panduoutput0405.txt', 'w', encoding='utf-8') as f:
    f.write('Top 10 usernames:\n')
    for username, count in sorted(username_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        f.write(f"{username}: {count}\n")

    f.write('\nTop 10 passwords:\n')
    for password, count in sorted(password_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        f.write(f"{password}: {count}\n")
