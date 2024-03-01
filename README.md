# Ip to domain resolver

## Overview
The Reverse DNS Lookup Tool is a Python script designed to perform reverse DNS lookups on multiple IP addresses concurrently. Given a list of IP addresses in a text file, the tool queries the DNS for each IP address to find its associated hostname. The results are then saved to a specified output file, with each IP address and its corresponding DNS name separated by a comma.

## Installation

### Prerequisites
- Python 3.6 or higher
- Access to the `dig` command from the `dnsutils` package (Linux) or equivalent in other operating systems.

### Setup
No additional Python packages are required as the script uses the standard library modules `argparse`, `subprocess`, and `threading`.

## Usage

- `--file` specifies the path to the input file containing the list of IP addresses, one per line.
- `--output` specifies the path to the output file where the results will be saved.

### Example

To run the tool with `ip_list.txt` as the input file and save the results to `results.txt`, use the following command:

```bash
python reverse_dns_lookup.py --file ip_list.txt --output results.txt
```
This will perform reverse DNS lookups on all IP addresses listed in `ip_list.txt` and save the results to `results.txt`, with each result separated by a comma.

# Domain to IP Resolver

This Python script resolves domain names to IP addresses. It reads a list of domains from a file, resolves each to its corresponding IP address, and optionally saves the results to a CSV file.
Requirements

    Python 3.x
    Internet connection for domain name resolution

Installation

No additional installation is required, as the script uses standard Python libraries.
Usage

Run the script from the command line using Python. The script accepts the following arguments:

    file_path (required): Path to the file containing domain names (one domain per line).
    --output (optional): Path to the output CSV file. If specified, the script will save the results in this file.
    --ips-only (optional): When set, the script prints or saves only the resolved IP addresses, excluding domains that could not be resolved.

Command Line Syntax

css

python resolve_domains.py <file_path> [--output <output_file>] [--ips-only]

Examples

    Print Domain and IP Pairs:

    To print the resolved domain and IP pairs to the console:

python resolve_domains.py domains.txt

Save Domain and IP Pairs to CSV:

To save the resolved domain and IP pairs to a CSV file:

css

python resolve_domains.py domains.txt --output results.csv

Print Only Resolved IPs:

To print only the resolved IPs to the console:

css

python resolve_domains.py domains.txt --ips-only

Save Only Resolved IPs to CSV:

To save only the resolved IPs to a CSV file:

css

    python resolve_domains.py domains.txt --ips-only --output ips_only.csv

Output Format

    When saving to a CSV file without the --ips-only flag, the file will contain two columns: Domain and IP.
    With the --ips-only flag, the CSV file will contain only one column: IP.

This README should provide a clear and concise guide for using your Python script. You can include this in the same directory as your script for easy reference by users.
