# Brahma Kavach - Firewall Management Tool

Brahma Kavach is a powerful firewall management tool designed and developed by Chalamalasetty Yaswanth Surya. It provides a user-friendly interface and a set of features to enable users to manage firewall rules efficiently on their Windows systems.


## Features

    Firewall Control: Brahma Kavach allows you to easily enable or disable the firewall with a single click, providing quick control over the system's network security.

    Rule Creation: Create new firewall rules using an intuitive interface. Specify rule properties such as program path, port number, rule name, and group name. The tool supports both TCP and UDP protocols.

    Rule Deletion: Remove existing firewall rules effortlessly by specifying the name of the rule to be deleted. This feature ensures easy management and cleanup of firewall configurations.

    Rule Enable/Disable: Enable or disable specific firewall rules as needed. This capability gives you the flexibility to control the behaviour of individual rules based on changing requirements.

    Rule Listing: View all current firewall rules in a structured and organized manner. The tool displays rule details, including name, group, enabled status, action, protocol, and local port, in a table format.

    Logging: Brahma Kavach provides a logging feature that keeps a record of firewall rule changes and actions performed. This enables you to track and review past firewall modifications for auditing and troubleshooting purposes.

    Import/Export Rules: Easily import and export firewall rules from/to external files. This functionality simplifies the process of backing up, sharing, and migrating firewall configurations across systems.

    Rule Modification: Modify existing firewall rules, including properties like program paths, ports, groups, actions, and more. This feature allows you to adapt and fine-tune firewall configurations to suit your specific needs.

    Rule Search: Find specific firewall rules quickly using the search functionality. Search by name, group, or other criteria to locate the desired rules efficiently, even in large rule sets.

    Rule Ordering: Specify the order in which firewall rules are applied. This capability ensures that rules are prioritized and executed in the desired sequence, providing precise control over rule precedence.

    Rule Templates: Utilize pre-defined rule templates for common use cases. The tool includes templates for popular applications or services, simplifying the creation of rules and ensuring compatibility with known scenarios.

    Rule Scheduling: Schedule the activation or deactivation of firewall rules based on specific time intervals or events. This feature allows you to automate rule management and adapt to dynamic network requirements.

## Requirements

To use Brahma Kavach, ensure that your system meets the following requirements:

    Operating System: Windows (supports Windows 7 and above)
    Administrative Privileges: Brahma Kavach requires administrative rights to manage firewall rules effectively.
    Python: The tool is built using Python and requires a compatible Python environment (Python 3.7 or above).

## Advantages

    Easy-to-Use Interface: Brahma Kavach provides a user-friendly interface, making it accessible to users with varying levels of technical expertise.
    Time-Saving: The tool simplifies firewall rule management tasks, saving you time and effort in configuring and maintaining firewall configurations.
    Flexibility: Brahma Kavach offers a range of features to suit different requirements, allowing you to customize and manage firewall rules according to your needs.
    Enhanced Security: By providing a convenient way to manage firewall rules, Brahma Kavach helps you maintain a secure network environment and protect your system from 
    unauthorized access.
    Centralized Control: The tool enables centralized control and visibility over firewall rules, making it easier to monitor and manage the network security of your system.

## Example: Running Brahma Kavach

To run Brahma Kavach, follow these steps:

    Ensure that you have administrative privileges on your Windows system.
    Install Python 3.7 or above if not already installed.
    Install the required dependencies by running the command: pip install prettytable.
    Download the Brahma Kavach source code from the official repository or obtain the executable file.
    Open a command prompt or terminal and navigate to the directory where the Brahma Kavach source code or executable file is located.
    Run the command: python brahma_kavach.py or execute the Brahma Kavach executable file.
    The tool will launch, presenting you with a menu and options to perform various firewall management tasks. Follow the on-screen prompts to use the desired features.

## Frequently Asked Questions (FAQs)

Q1. Can I use Brahma Kavach on operating systems other than Windows?
No, Brahma Kavach is specifically designed for Windows systems and is not compatible with other operating systems.

Q2. Is it safe to create, modify, or delete firewall rules using Brahma Kavach?
Yes, Brahma Kavach is designed to ensure the safe management of firewall rules. However, exercise caution while making changes and thoroughly test firewall configurations before applying them in production environments.

Q3. Can I customize the logging behaviour of Brahma Kavach?
At the moment, Brahma Kavach provides basic logging functionality. Future updates may include more extensive logging capabilities and customizable options.

Q4. How can I report issues or provide feedback on Brahma Kavach?
For any issues, feedback, or suggestions, please contact us at cyaswanthsurya@gmail.com We appreciate your input and will respond as soon as possible.
License and Open Source Information

## Brahma Kavach is released under the MIT License.

The tool utilizes the following open-source components:

    PrettyTable: Licensed under the BSD License. For more details, refer to the PrettyTable documentation.
