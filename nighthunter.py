import os
import sys
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.RED + r"""
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
""")
    print(Fore.CYAN + ">> NightHunter - Automated Recon Framework")
    print(Fore.YELLOW + ">> Hunt the surface. Own the night.\n")

def create_structure(domain):
    base_path = f"results/{domain}"
    os.makedirs(base_path, exist_ok=True)
    return base_path

def run_subfinder(domain, path):
    print(Fore.GREEN + "[+] Running Subdomain Enumeration...")
    os.system(f"subfinder -d {domain} -silent -o {path}/subdomains.txt")

def run_httpx(path):
    print(Fore.GREEN + "[+] Checking Live Hosts...")
    os.system(f"httpx -l {path}/subdomains.txt -silent -o {path}/live.txt")

def run_nmap(path):
    print(Fore.GREEN + "[+] Running Port Scan on Live Hosts...")
    os.system(f"nmap -iL {path}/live.txt -T4 -oN {path}/ports.txt")

def summary(path):
    print(Fore.CYAN + "\n[✓] Recon Completed Successfully")
    print(Fore.YELLOW + f"[+] Results saved in: {path}")
    print(Fore.MAGENTA + "[+] Files Generated:")
    print("   ├── subdomains.txt")
    print("   ├── live.txt")
    print("   └── ports.txt\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 nighthunter.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    banner()

    print(Fore.RED + f"[+] Target Locked: {domain}")
    print(Fore.BLUE + f"[+] Scan Started: {datetime.now()}\n")

    path = create_structure(domain)

    run_subfinder(domain, path)
    run_httpx(path)
    run_nmap(path)

    summary(path)

if __name__ == "__main__":
    main()
