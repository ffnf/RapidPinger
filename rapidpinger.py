# https://github.com/ffnf/RapidPinger/
import ping3
import concurrent.futures
import tabulate
from datetime import datetime
import os

endpoints = [
    ('Google', 'google.com'),
    ('Amazon', 'amazon.com'),
    ('Facebook', 'facebook.com'),
    ('Netflix', 'netflix.com'),
    ('Microsoft', 'microsoft.com'),
    ('Twitter', 'twitter.com'),
    ('Instagram', 'instagram.com'),
    ('LinkedIn', 'linkedin.com'),
    ('GitHub', 'github.com'),
    ('Dropbox', 'dropbox.com'),
    ('Slack', 'slack.com'),
    ('WhatsApp', 'whatsapp.com'),
    ('Zoom', 'zoom.us'),
    ('Twitch', 'twitch.tv'),
    ('Reddit', 'reddit.com'),
    ('Stack Overflow', 'stackoverflow.com'),
    ('Wikipedia', 'wikipedia.org'),
    ('Adobe', 'adobe.com'),
    ('Apple', 'apple.com'),
    ('Spotify', 'spotify.com')
]


def ping_endpoint(endpoint):
    filename, server = endpoint
    response_time = ping3.ping(server)
    if response_time is not None:
        return (filename, server, response_time * 1000)

def ping_servers(endpoints):
    ping_results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(ping_endpoint, endpoints)
        for result in results:
            if result is not None:
                ping_results.append(result)
    return ping_results

def sort_servers_by_response_time(ping_results):
    sorted_results = sorted(ping_results, key=lambda x: x[2])
    return sorted_results

# Splitting endpoints into groups of 10
grouped_endpoints = [endpoints[i:i+10] for i in range(0, len(endpoints), 10)]

# Ping the endpoints and get response times using multithreading
ping_results = []
for group in grouped_endpoints:
    ping_results += ping_servers(group)

# Sort endpoints by response time
sorted_endpoints = sort_servers_by_response_time(ping_results)

show_server = False  # Set to False if you don't want to display the server column

# Display the sorted results
top10 = True  # Set this variable to True if you want to print only the top 10 results
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Get the directory path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the file path in the script's directory
file_path = os.path.join(script_dir, "10.txt")

if top10:
    top10_results = sorted_endpoints[:10]
    table_data = [(f"{filename}", round(response_time, 1)) for filename, server, response_time in top10_results]
    headers = ['Filename '+current_time, '(ms)']
    if show_server:
        table_data = [(f"{filename}", server, response_time) for filename, server, response_time in top10_results]
        headers = ['Filename '+current_time, 'Server', '(ms)']

    table = tabulate.tabulate(table_data, headers=headers, tablefmt='pretty')
    with open(file_path, "w") as file:
        file.write(table)
    print(table)
else:
    table = tabulate.tabulate(sorted_endpoints, headers=['Filename', 'Server', 'Response Time (ms)'], tablefmt='fancy_grid')
    print(table)
