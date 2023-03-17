# c0ff33b34n
# Subdomain Finder

import argparse
import socket

def subdomains(domain, wordlist_file):
    subdomains = []
    with open(wordlist_file, "r") as wordlist:
        print(f"[+] Using wordlist file: {wordlist_file}")
        for line in wordlist:
            subdomain = line.strip() + "." + domain
            try:
                host_ip = socket.gethostbyname(subdomain)
                subdomains.append(subdomain)
                print("[+] Discovered Subdomain: %s => %s" % (subdomain, host_ip))
            except socket.error:
                pass
    return subdomains

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find subdomains for a given domain name")
    parser.add_argument("-u", "--url", required=True, help="The domain name to search for subdomains")
    parser.add_argument("-s", "--silent", action="store_true", help="Suppress output and only save results to subs.txt")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="The wordlist file to use for subdomain search")
    args = parser.parse_args()

    if not args.silent:
        print("""
███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗███████╗███████╗██████╗ ██████╗ 
██╔════╝██║   ██║██╔══██╗██╔════╝██║   ██║╚══███╔╝╚══███╔╝╚════██╗██╔══██╗
███████╗██║   ██║██████╔╝█████╗  ██║   ██║  ███╔╝   ███╔╝  █████╔╝██████╔╝
╚════██║██║   ██║██╔══██╗██╔══╝  ██║   ██║ ███╔╝   ███╔╝   ╚═══██╗██╔══██╗
███████║╚██████╔╝██████╔╝██║     ╚██████╔╝███████╗███████╗██████╔╝██║  ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝
                                                                          
           subfuzzer.py - by c0ff33b34n
        """)

    domain = args.url
    wordlist_file = args.wordlist
    subdomains = subdomains(domain, wordlist_file)
    if not args.silent:
        print("[+] Total subdomains found: %d" % len(subdomains))

    with open("subs.txt", "w") as subs_file:
        for subdomain in subdomains:
            subs_file.write(subdomain + "\n")
    if not args.silent:
        print("[+] Subdomains saved to subs.txt")


