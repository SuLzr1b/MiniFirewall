# MiniFirewall

A badass Python tool for cybersecurity enthusiasts to monitor network connections and block IPs using Windows Firewall. MiniFirewall logs all blocked IPs to `firewall_log.txt`, lets you unblock IPs with a simple command, and **requires administrator privileges** to work its magic. Hack your network like a pro! 🛡️

## Why Run as Administrator?
MiniFirewall uses `netsh advfirewall` commands to manage Windows Firewall rules, which demands admin privileges. Without them, you can’t block or unblock IPs. Always run this tool as an admin to avoid errors.

## Features
- **Network Monitoring**: View active connections (local/remote IPs and ports) with `psutil`.
- **IP Blocking**: Block IPs using `netsh`, with admin privileges.
- **Logging**: Every blocked IP is logged to `firewall_log.txt` with a timestamp.
- **Unblock IPs**: Easily remove blocked IPs with a `netsh` command.
- **Cyber CLI**: Colorful interface with `colorama` and ASCII art for hacker vibes.
- **Safety Checks**: Validates IPs and ensures admin mode.

## Log Example
MiniFirewall saves blocked IPs to `firewall_log.txt` in the project folder. Here’s what it looks like:

```
[2025-05-06 22:36] Bloqueado: 1.2.3.4
[2025-05-07 09:15] Bloqueado: 693.269.2.404
[2025-05-07 14:22] Bloqueado: 10.0.0.5
```

Each entry shows the date, time, and blocked IP, making it easy to track your firewall actions.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/MiniFirewall.git
   cd MiniFirewall
   ```

2. **Install Dependencies**:
   Requires Python 3.6+. Install the libraries:
   ```bash
   pip install psutil colorama
   ```

3. **Run as Administrator** (Mandatory):
   - **CMD**:
     - Press `Win + R`, type `cmd`, press `Ctrl + Shift + Enter` to open as admin (title should read “Administrator: Command Prompt”).
     - Navigate to the project folder:
       ```bash
       cd C:\Users\YourUsername\Desktop\MiniFirewall
       ```
     - Run:
       ```bash
       python minifirewall.py
       ```
   - **PowerShell**:
     - Search “PowerShell” in `Win + S`, right-click, select “Run as administrator”.
     - Navigate and run as above.
   - **Note**: If you see `C:\WINDOWS\system32>`, use `cd` to go to your project folder (e.g., `cd C:\Users\YourUsername\Desktop\MiniFirewall`).

## Usage
1. **Start the Tool**:
   - Run `python minifirewall.py` in an admin CMD or PowerShell.
   - You’ll see a slick ASCII banner and menu:
     ```
     🛡️ MiniFirewall by [YourName] 🛡️
     Menu:
     1. List connections
     2. Block IP
     3. Exit
     ```

2. **Menu Options**:
   - **List Connections**: Select `1` to see active connections (e.g., `127.0.0.1:8000 -> 192.168.1.1:443`).
   - **Block IP**: Select `2`, enter an IP (e.g., `1.2.3.4`), and it’s blocked. Check `firewall_log.txt` for the log.
   - **Exit**: Select `3` to close.

3. **View Logs**:
   - Open `firewall_log.txt` in the project folder to see blocked IPs and timestamps.

4. **Unblock an IP**:
   - To remove a blocked IP, run this in an admin CMD/PowerShell:
     ```bash
     netsh advfirewall firewall delete rule name="Block 1.2.3.4"
     ```
     Replace `1.2.3.4` with the IP you want to unblock.

5. **Generate Connections**:
   - Open a browser, Discord, or run:
     ```bash
     python -m http.server
     ```
     to create connections for listing.

## Troubleshooting
- **"Must run as admin"**: Open CMD/PowerShell as admin (right-click > “Run as administrator”). Check for “Administrator” in the title.
- **"Directory not found"**: From `C:\WINDOWS\system32>`, navigate with `cd C:\Users\YourUsername\Desktop\MiniFirewall`. Copy the path from File Explorer.
- **"netsh error"**: Run as admin and use a valid IP (e.g., `1.2.3.4`). Ensure Windows Firewall is enabled.
- **"Python not found"**: Use `C:\Python39\python.exe minifirewall.py` or add Python to PATH.
- **No logs**: Block an IP (option 2) and verify `firewall_log.txt` exists in the project folder.

## License
MIT License. See [LICENSE](LICENSE) for details.

---
Created by [SuLzr1b] as part of a cybersecurity learning journey.
