import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor

def run_dig(ip_address):
    """Run dig -x command on the given IP address and return the result."""
    try:
        # Execute the dig command
        result = subprocess.run(['dig', '-x', ip_address, '+short'], capture_output=True, text=True, check=True)
        # Return the stdout with whitespace stripped
        dns_name = result.stdout.strip()
        # Return the result in the desired format
        return f"{ip_address}: {dns_name}" if dns_name else f"{ip_address}: No DNS record found"
    except subprocess.CalledProcessError:
        # Return an error message if dig command fails
        return f"{ip_address}: Failed to run dig"

def main(file_path, output_file):
    with open(file_path, 'r') as file:
        ip_addresses = [line.strip() for line in file.readlines()]

    # Use ThreadPoolExecutor to run dig queries concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Map the run_dig function to each IP address and execute concurrently
        results = list(executor.map(run_dig, ip_addresses))
    
    # Write the results to the output file and print them, separated by commas
    with open(output_file, 'w') as output:
        output.write(", ".join(results))
        print(", ".join(results))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform reverse DNS lookups on a list of IP addresses concurrently and save the results to a file.')
    parser.add_argument('--file', type=str, required=True, help='The file containing a list of IP addresses.')
    parser.add_argument('--output', type=str, required=True, help='The file where the results will be saved.')
    args = parser.parse_args()

    main(args.file, args.output)
