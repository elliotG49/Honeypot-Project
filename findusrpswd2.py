import json

with open('C:/Users/ellio/Documents/honeypot/cowrie.json.2023-04-08', 'r', encoding='utf-8') as f:
    usernames_file = open('C:/Users/ellio/Documents/honeypot/usernames/usernames.txt', 'a')
    passwords_file = open('C:/Users/ellio/Documents/honeypot/passwords/passwords.txt', 'a')
    
    for line in f:
        data = json.loads(line)
        if data['eventid'] == 'cowrie.login.failed':
            usernames_file.write(data['username'] + '\n')
            passwords_file.write(data['password'] + '\n')
            
    usernames_file.close()
    passwords_file.close()