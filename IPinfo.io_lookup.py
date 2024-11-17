import os
import requests
import json
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

def find_ip_list_file():
    """Find a file in the script's directory with a name like 'IPList.txt' or 'iplist.txt'."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(script_dir):
        if re.match(r'^iplist.*\.txt$', filename, re.IGNORECASE):
            return os.path.join(script_dir, filename)
    raise FileNotFoundError("No IP list file found with a name like 'IPList.txt' or 'iplist.txt'.")

def load_ip_list(file_path):
    """Load IPs from the specified text file, ignoring numeric indices if present."""
    ip_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.isdigit():  # Ignore numeric indices
                    ip_list.append(stripped_line)
        if not ip_list:
            raise ValueError("The IP list file is empty or incorrectly formatted.")
    except Exception as e:
        raise Exception(f"Error loading IP list: {e}")
    
    return ip_list

def detailed_ip_lookup(ip_list):
    token = os.getenv('IPINFO_TOKEN')
    if not token:
        raise ValueError("IPINFO_TOKEN environment variable not set. Please check your .env file.")
    
    ip_info = {}
    for index, ip in enumerate(ip_list, start=1):  # Start numbering from 1
        try:
            response = requests.get(f"https://ipinfo.io/{ip}?token={token}")
            if response.status_code != 200:
                raise ValueError(f"Failed to fetch data for IP {ip}. Status code: {response.status_code}")
            
            data = response.json()
            ip_info[f"{index}. {ip}"] = {
                'IP': data.get('ip'),
                'City': data.get('city'),
                'Region': data.get('region'),
                'Country': data.get('country'),
                'Location': data.get('loc'),
                'Organization': data.get('org'),
                'Postal': data.get('postal')
            }
        except Exception as e:
            ip_info[f"{index}. {ip}"] = {'Error': str(e)}

    return ip_info

def save_results_to_file(data, filename="IPLookupResults.json"):
    """Save the lookup results to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Results saved to {filename}")

# Run the script
try:
    # Find the IP list file
    file_path = find_ip_list_file()
    ip_list = load_ip_list(file_path)
    lookup_results = detailed_ip_lookup(ip_list)
    
    # Output results to the console
    print(json.dumps(lookup_results, indent=4))
    
    # Save results to a file
    save_results_to_file(lookup_results)
except Exception as e:
    print(f"An error occurred: {e}")