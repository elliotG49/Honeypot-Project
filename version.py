import json

versions = []
with open('C:/Users/gardn/Documents/honeypot/json files/cowrie.json.2023-04-06', 'r') as f:
    for line in f:
        data = json.loads(line)
        if 'cowrie.client.version' in data['eventid']:
            version = data['version']
            versions.append(version)

# Write the versions to a new file
with open('C:/Users/gardn/Documents/honeypot/versions.txt', 'a', encoding='utf-8') as f:
    f.write('\n'.join(versions))