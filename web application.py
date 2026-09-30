import psutil
from datetime import datetime

LOG_FILE = "firewall_log.txt"


def monitor_connections():
    print("\n--- Active Network Connections ---")

    connections = psutil.net_connections(kind="inet")

    if not connections:
        print("No active connections found.")
        return

    for conn in connections:
        local = conn.laddr if conn.laddr else "-"
        remote = conn.raddr if conn.raddr else "-"
        status = conn.status

        print(f"Local: {local}")
        print(f"Remote: {remote}")
        print(f"Status: {status}")
        print("-" * 40)


def save_firewall_log():
    connections = psutil.net_connections(kind="inet")

    with open(LOG_FILE, "a") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write("Personal Firewall Log\n")
        file.write("Time: " + str(datetime.now()) + "\n")
        file.write("=" * 50 + "\n")

        for conn in connections:
            local = conn.laddr if conn.laddr else "-"
            remote = conn.raddr if conn.raddr else "-"
            status = conn.status

            file.write(f"Local: {local}\n")
            file.write(f"Remote: {remote}\n")
            file.write(f"Status: {status}\n")
            file.write("-" * 40 + "\n")

    print("\nFirewall log saved successfully!")
    print("File name:", LOG_FILE)


def main():
    while True:
        print("\n================================")
        print("     PERSONAL FIREWALL")
        print("================================")
        print("1. Monitor Network Connections")
        print("2. Save Firewall Log")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            monitor_connections()

        elif choice == "2":
            save_firewall_log()

        elif choice == "3":
            print("Firewall program closed.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()