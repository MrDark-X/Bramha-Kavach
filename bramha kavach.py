import subprocess
import ctypes
import sys
from prettytable import PrettyTable



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_firewall_rule():
    program_path = input("Enter the program path or leave blank for all programs: ")
    rule_name = input("Enter a name for the firewall rule: ")
    port = input("Enter the port number or leave blank for all ports: ")
    group_name = input("Enter a name for the rule group: ")

    if program_path:
        cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=allow program="{program_path}"'
    else:
        cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=allow'

    if port:
        cmd += f' protocol=TCP localport={port}'

    if group_name:
        cmd += f' group="{group_name}"'

    subprocess.run(cmd, shell=True)
    print("Firewall rule created successfully.")

def get_firewall_status():
    firewall_state = subprocess.run('netsh advfirewall show allprofiles state', capture_output=True, text=True, shell=True)
    return "ON" if "ON" in firewall_state.stdout else "OFF"

def delete_firewall_rule():
    rule_name = input("Enter the name of the firewall rule to delete: ")

    cmd = f'netsh advfirewall firewall delete rule name="{rule_name}"'
    subprocess.run(cmd, shell=True)
    print("Firewall rule deleted successfully.")

def disable_firewall_rule():
    rule_name = input("Enter the name of the firewall rule to disable: ")

    cmd = f'netsh advfirewall firewall set rule name="{rule_name}" new enable=no'
    subprocess.run(cmd, shell=True)
    print("Firewall rule disabled successfully.")

def enable_firewall_rule():
    rule_name = input("Enter the name of the firewall rule to enable: ")

    cmd = f'netsh advfirewall firewall set rule name="{rule_name}" new enable=yes'
    subprocess.run(cmd, shell=True)
    print("Firewall rule enabled successfully.")

def show_firewall_rules():
    firewall_rules = subprocess.run('netsh advfirewall firewall show rule name=all', capture_output=True, text=True, shell=True)
    rules_output = firewall_rules.stdout

    if "No rules match the specified criteria." in rules_output:
        print("No firewall rules found.")
        return

    # Parse the output and create a table
    rules_table = PrettyTable()
    rules_table.field_names = ["Rule Name", "Group", "Enabled", "Action", "Protocol", "Local Port"]

    # Split the output by line and skip the first two lines (headers)
    rule_lines = rules_output.split("\n")[2:]

    for line in rule_lines:
        line = line.strip()
        if line:
            rule_data = line.split()
            # Skip lines that don't contain rule data
            if len(rule_data) != 6:
                continue
            rules_table.add_row(rule_data)

    print(rules_table)


def main():
    if not is_admin():
        print("You are not an administrator. Please run the script as an administrator.")
        sys.exit()
    print("*********************")
    print("*   Bramha Kavach   *")
    print("*********************\n")
    print("Welcome to Bramha Kavach - Firewall Management Tool")
    print("This script allows you to enable/disable the firewall, create, delete, enable, disable, and show firewall rules.")


    print("\nExample:")
    print("To create a firewall rule:")
    print("- Choose '3' when prompted.")
    print("- Enter the program path or leave it blank for all programs.")
    print("- Enter a name for the rule.")
    print("- Enter the port number or leave it blank for all ports.")
    print("- Enter a name for the rule group or leave it blank for no grouping.")

    print("\nTo delete a firewall rule:")
    print("- Choose '4' when prompted.")
    print("- Enter the name of the rule to delete.")

    print("\nTo disable a firewall rule:")
    print("- Choose '6' when prompted.")
    print("- Enter the name of the rule to disable.")

    print("\nTo enable a firewall rule:")
    print("- Choose '5' when prompted.")
    print("- Enter the name of the rule to enable.")

    print("\nTo see all firewall rules:")
    print("- Choose '7' when prompted.")

    print("\nLet's get started!\n")

    print("Menu:")
    print("1. Enable Firewall")
    print("2. Disable Firewall")
    print("3. Create a New Firewall Rule")
    print("4. Delete an Existing Firewall Rule")
    print("5. Enable a Firewall Rule")
    print("6. Disable a Firewall Rule")
    print("7. Show All Current Firewall Rules")


    print("\n\nCurrent Firewall Status: " + get_firewall_status() + "\n")



    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        subprocess.run('netsh advfirewall set allprofiles state on', shell=True)
        print("Firewall has been enabled.")
    elif choice == "2":
        subprocess.run('netsh advfirewall set allprofiles state off', shell=True)
        print("Firewall has been disabled.")
    elif choice == "3":
        create_firewall_rule()
    elif choice == "4":
        delete_firewall_rule()
    elif choice == "5":
        enable_firewall_rule()
    elif choice == "6":
        disable_firewall_rule()
    elif choice == "7":
        show_firewall_rules()
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
