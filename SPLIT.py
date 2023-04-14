import json

with open('C:/Users/gardn/Documents/honeypot/json files/cowrie.json.2023-04-05', 'r', encoding='utf-8') as input_file:
    with open('C:/Users/gardn/Documents/honeypot/ouput json files/cowrie04-05.txt', 'w', encoding='utf-8') as output_file:
        for line in input_file:
            log_element = json.loads(line)
            output_file.write(json.dumps(log_element, ensure_ascii=False) + '\n')