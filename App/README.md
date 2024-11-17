# Stateful Firewall Application Documentation

## Overview

This project implements a stateful firewall that inspects network packets and applies rules defined in a configuration file. The firewall is able to log actions, perform stateful inspection, and trigger email alerts when a specified packet threshold is reached. The system also monitors and updates firewall rules in real-time by watching for changes in the rule file.

The firewall is built using the Scapy library for packet capture and analysis, Python’s threading for monitoring file changes, and JSON for configuration and logging.

### Features

- **Stateful Packet Inspection**: The firewall inspects each incoming packet in the context of its state, allowing or denying traffic based on rules defined in the configuration.
- **Dynamic Rule Monitoring**: Rules are loaded from a JSON file, and changes in this file are automatically detected and applied in real-time by a background thread.
- **Rule-based Actions**: Rules define actions to take upon packet matches, including:
  - **Allow**: Permit the packet to pass through.
  - **Deny**: Block the packet.
  - **Mail**: Trigger an alert via email if a specified threshold is reached (e.g., if a certain number of "MAIL" actions occur).
- **Logging**: Every event and action taken by the firewall (e.g., packet matches, rule changes) is logged in a JSON file, with timestamps for each log entry.
- **Alerting via Email**: When the packet matches a rule with the "MAIL" action and a threshold (from settings) is reached, an alert email is sent to a predefined recipient.
- **Threshold-based Alerts**: The system supports a mail threshold setting, limiting how many alerts are sent in a given time frame to prevent excessive emailing.
- **Configurable Rule File**: The firewall rules are read from a user-defined JSON file, which can be updated without restarting the system. A background thread monitors this file for changes and automatically reloads the rules.
- **Scalable and Modular**: The system is designed to be scalable with additional rules and inspection capabilities. It also allows for modular extensions (e.g., new rule actions, logging mechanisms).
- **Multithreading**: The rule file monitoring is handled in a separate thread, ensuring the system does not block other processes while monitoring for changes.
- **Cross-Platform Support**: The system is implemented in Python, using the Scapy library for packet analysis, ensuring compatibility across multiple platforms (Linux, Windows).

---

## Components

### 1. `index.py`

The main entry point of the application. It sets up the firewall system, loads rules, starts packet capture, and continuously monitors the rule file for updates.

#### Key Functions:

- **`packet_handler(packet, firewall)`**: This function handles incoming packets and performs stateful inspection on them.
- **`main()`**: The core function that initializes the firewall, logger, and rule monitor, and starts packet capture.

### 2. `logger.py`

Handles logging for the application. It logs messages to a JSON file, ensuring that logs are stored with a timestamp and are retrievable for later review.

#### Key Functions:

- **`__init__(log_file_path)`**: Initializes the logger and ensures the log directory exists.
- **`ensure_log_directory_exists()`**: Creates the log directory if it does not exist.
- **`log(message)`**: Logs a message with the current timestamp. It appends the message to the log file in JSON format.

### 3. `mailer.py`

Handles sending email alerts when the firewall encounters certain conditions, such as exceeding a specified threshold for packet filtering actions.

#### Key Functions:

- **`send_alert_email(subject, body)`**: Sends an email alert to the receiver with the given subject and body.
- **Email Configuration**: Loads Gmail credentials from a `.env` file for authentication.

### 4. `rule_file_monitor.py`

Monitors the rule configuration file for any changes and updates the firewall rules accordingly.

#### Key Functions:

- **`__init__(rule_loader, firewall, interval=5)`**: Initializes the file monitor, setting up the interval to check for file changes.
- **`run()`**: Continuously checks the rule file for changes. If a change is detected, it reloads the rules and updates the firewall.
- **`stop()`**: Stops the monitoring thread.

### 5. `rule_loader.py`

Responsible for loading and parsing firewall rules from a JSON file. Each rule is represented as an instance of the `Rule` class.

#### Key Functions:

- **`__init__(json_file)`**: Initializes the rule loader with the path to the rules JSON file and loads the rules.
- **`load_rules()`**: Loads and parses the rules from the JSON file.
- **`get_rules()`**: Returns the list of loaded rules.

### 6. `rule.py`

Represents a firewall rule, including its attributes and the logic for matching packets against these rules.

#### Key Functions:

- **`__init__(id, source_ip, destination_ip, source_port, destination_port, protocol, action)`**: Initializes the rule with its attributes.
- **`__str__()`**: Returns a string representation of the rule.
- **`matches(packet)`**: Checks if a given packet matches the rule based on its attributes (IP, port, protocol).

### 7. `stateful_firewall.py`

The core of the firewall, performing packet inspection and logging actions based on the defined rules.

#### Key Functions:

- **`__init__(rules, logger)`**: Initializes the firewall with a list of rules and a logger.
- **`load_mail_threshold()`**: Loads the threshold for the number of mail actions before an email alert is triggered.
- **`update_rules(rules)`**: Updates the list of rules in the firewall.
- **`check_packet(packet)`**: Checks a packet against the current rules and returns the action to take (ALLOW, DENY, or MAIL).
- **`handle_mail_action(packet_info)`**: Increments a counter and sends an email alert when the mail threshold is reached.
- **`log_packet(packet_info, action)`**: Logs the packet information and the action taken.
- **`extract_packet_info(packet)`**: Extracts relevant information (IP, port, protocol) from a packet.
- **`perform_stateful_inspection(packet)`**: Performs the packet inspection and executes the appropriate action (ALLOW, DENY, MAIL).

---

## Configuration

- **Rules File**: The firewall rules are loaded from a JSON file specified in the `RuleLoader` class. This file defines conditions for matching packets, including source and destination IP addresses, ports, protocols, and actions (ALLOW, DENY, or MAIL).

  Example rule entry:

  ```json
  [
    {
      "id": 1,
      "source_ip": "192.168.1.1",
      "destination_ip": "any",
      "source_port": "any",
      "destination_port": "80",
      "protocol": "TCP",
      "action": "ALLOW"
    },
    {
      "id": 2,
      "source_ip": "any",
      "destination_ip": "any",
      "source_port": "any",
      "destination_port": "any",
      "protocol": "ICMP",
      "action": "DENY"
    },
    {
      "id": 3,
      "source_ip": "any",
      "destination_ip": "any",
      "source_port": "any",
      "destination_port": "any",
      "protocol": "TCP",
      "action": "MAIL"
    }
  ]
  ```

- **Settings File**: The `settings.json` file is used to configure the email threshold for triggering alerts. The default threshold is set to 10.

  Example settings file:

  ```json
  {
    "MAIL_threshold": 10
  }
  ```

---

## Running the Application

1. **Set up environment variables**:

   - Create a `.env` file in the root directory with your Gmail credentials.
     ```
     GMAIL_USER=your-email@gmail.com
     GMAIL_PASS=your-password
     RECEIVER_EMAIL=receiver-email@example.com
     ```

2. **Start the application**:

   - Run the `index.py` script to start the packet capture and firewall inspection:
     ```bash
     python index.py
     ```

3. **Monitor logs**:

   - Logs are stored in the `files/logs.json` file. You can inspect the log to track packet actions and rule changes.

4. **Update firewall rules**:
   - The application continuously monitors the rules file for changes. If the file is updated, the new rules are automatically loaded.

---
