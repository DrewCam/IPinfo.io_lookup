# IP Lookup Script

This script performs detailed lookups for IP addresses from a text file using the [IPinfo](https://ipinfo.io) API. It retrieves data such as city, region, country, location, organization, and postal code for each IP address listed in the input file.

---

## Features

- Automatically detects a text file named `IPList.txt` or similar in the script directory.
- Reads and validates IP addresses from the input file, ignoring numeric indices.
- Queries the [IPinfo API](https://ipinfo.io) to gather detailed information about each IP address.
- Saves the results in a structured JSON file (`IPLookupResults.json`) for later analysis.

---

## Prerequisites

### Environment Setup
1. Install Python (>=3.6).
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the script directory with the following content:
   ```plaintext
   IPINFO_TOKEN=your_ipinfo_token
   ```
   Replace `your_ipinfo_token` with your API token from [IPinfo](https://ipinfo.io).

---

## Input File Format

- The script expects a text file named `IPList.txt` or similarly named (`iplist*.txt`) in the script directory.
- The file should contain one IP address per line. Numeric indices (e.g., `1.`) are ignored automatically.

### Example `IPList.txt`:
```
1. 8.8.8.8
2. 1.1.1.1
192.168.1.1
```

---

## How to Use

1. Place your `IPList.txt` file in the same directory as the script.
2. Run the script:
   ```bash
   python ip_lookup.py
   ```
3. The script will:
   - Automatically locate the input file.
   - Perform lookups for all valid IP addresses.
   - Save the results to `IPLookupResults.json`.

---

## Output

### Example JSON Output (`IPLookupResults.json`):
```json
{
    "1. 8.8.8.8": {
        "IP": "8.8.8.8",
        "City": "Mountain View",
        "Region": "California",
        "Country": "US",
        "Location": "37.4056,-122.0775",
        "Organization": "AS15169 Google LLC",
        "Postal": "94043"
    },
    "2. 1.1.1.1": {
        "IP": "1.1.1.1",
        "City": "Sydney",
        "Region": "New South Wales",
        "Country": "AU",
        "Location": "-33.4940,151.3430",
        "Organization": "AS13335 Cloudflare, Inc.",
        "Postal": "2000"
    },
    "3. 192.168.1.1": {
        "Error": "Failed to fetch data for IP 192.168.1.1. Status code: 400"
    }
}
```

---

## Error Handling

- If the script cannot find the input file, it will raise an error:
  ```
  No IP list file found with a name like 'IPList.txt' or 'iplist.txt'.
  ```
- If an invalid or empty file is provided, it will raise an appropriate error:
  ```
  The IP list file is empty or incorrectly formatted.
  ```
- If the API token is missing or invalid:
  ```
  IPINFO_TOKEN environment variable not set. Please check your .env file.
  ```

---

## Customization

### File Names
You can modify the `find_ip_list_file` function to look for specific file names or prompt the user for an input file.

### API Integration
To extend functionality or use a different API, modify the `detailed_ip_lookup` function.

---

## Notes

- Ensure that your `.env` file is not committed to version control by adding it to `.gitignore`:
  ```
  .env
  ```
