import argparse
import socket
import csv

def resolve_domains(file_path):
    """
    Read domains from a file and resolve them to IP addresses.

    :param file_path: Path to the file containing domain names.
    :return: Dictionary mapping domains to their resolved IPs or error messages.
    """
    resolved_ips = {}
    with open(file_path, 'r') as file:
        for line in file:
            domain = line.strip()
            try:
                ip = socket.gethostbyname(domain)
                resolved_ips[domain] = ip
            except socket.error as e:
                resolved_ips[domain] = f"Error: {e}"
    return resolved_ips

def save_to_csv(resolved_domains, output_file, ips_only):
    """
    Save the resolved domain details to a CSV file.

    :param resolved_domains: Dictionary of domains and their resolved IPs or errors.
    :param output_file: Path to the output CSV file.
    :param ips_only: Boolean indicating whether to save only IPs or include domain names.
    """
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if ips_only:
            writer.writerow(['IP'])
            for ip in resolved_domains.values():
                if 'Error' not in ip:
                    writer.writerow([ip])
        else:
            writer.writerow(['Domain', 'IP'])
            for domain, ip in resolved_domains.items():
                writer.writerow([domain, ip])

def main():
    parser = argparse.ArgumentParser(description="Resolve domains to IPs from a file")
    parser.add_argument('file_path', type=str, help='Path to the file containing domain names')
    parser.add_argument('--output', type=str, help='Path to the output CSV file (optional)')
    parser.add_argument('--ips-only', action='store_true', help='Print or save only the resolved IPs (optional)')
    args = parser.parse_args()

    resolved_domains = resolve_domains(args.file_path)
    
    if args.output:
        save_to_csv(resolved_domains, args.output, args.ips_only)
        print(f"Results saved to {args.output}")
    else:
        for domain, ip in resolved_domains.items():
            if args.ips_only and 'Error' not in ip:
                print(ip)
            elif not args.ips_only:
                print(f"{domain}: {ip}")

if __name__ == "__main__":
    main()
