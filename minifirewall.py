import psutil
import os
from colorama import init, Fore
import time
import re


init(autoreset=True)

def print_banner():
    print(Fore.BLUE + r"""
 __  __       _ _______ _          ____  
|  \/  |     (_)__   __| |        |___ \ 
| \  / | __ _ _   | |  | |__   __  __) |
| |\/| |/ _` | |  | |  | '_ \ / __|__ < 
| |  | | (_| | |  | |  | | | | (__ ___) |
|_|  |_|__,_|_| |____|_| |_|__,_|____/ 
    """)
    print(Fore.CYAN + "🛡️ MiniFirewall by SuLzr1b 🛡️")

def list_connections():
    print(Fore.CYAN + "Active connections:")
    connections = []
    for conn in psutil.net_connections():
        if conn.laddr and conn.raddr:
            local = f"{conn.laddr.ip}:{conn.laddr.port}"
            remote = f"{conn.raddr.ip}:{conn.raddr.port}"
            connections.append((local, remote, conn.status))
            print(Fore.GREEN + f"Connection: {local} -> {remote} (Status: {conn.status})")
        elif conn.laddr:
            print(Fore.YELLOW + f"Local: {conn.laddr.ip}:{conn.laddr.port} (Status: {conn.status})")
    return connections

def block_ip(ip):

    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        print(Fore.RED + "Invalid IP! Use the format xxx.xxx.xxx.xxx 🚨")
        return

    command = f'netsh advfirewall firewall add rule name="Block {ip}" dir=in action=block remoteip={ip}'
    try:
        result = os.system(command)
        if result == 0:  
            with open("firewall_log.txt", "a") as file:
                file.write(f"[{time.strftime('%Y-%m-%d %H:%M')}] Bloqueado: {ip}\n")
            print(Fore.GREEN + f"IP {ip} Successfully blocked! 🛑")
        else:
            print(Fore.RED + f"Error executing netsh! Check permissions or syntax. 🚨")
    except Exception as e:
        print(Fore.RED + f"Error blocking IP: {str(e)} 🚨")


print_banner()


while True:
    print(Fore.CYAN + "\nMenu:")
    print("1. List Connections")
    print("2. Block IP")
    print("3. Exit")
    choice = input(Fore.CYAN + "Choose an option (1-3): ").strip()

    if choice == "1":
        list_connections()
    elif choice == "2":
        ip = input(Fore.CYAN + "Enter the IP to block: ").strip()
        if ip:
            block_ip(ip)
        else:
            print(Fore.RED + "IP not provided! 🚨")
    elif choice == "3":
        print(Fore.GREEN + "Leaving the MiniFirewall... 👋")
        break
    else:
        print(Fore.RED + "Invalid option! Try again🚨")
