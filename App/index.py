import os
from scapy.all import sniff
from rule_loader import RuleLoader
from logger import Logger
from stateful_firewall import StatefulFirewall
from rule_file_monitor import RuleFileMonitor


def packet_handler(packet, firewall):
    firewall.perform_stateful_inspection(packet)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(base_dir, 'files')
    logger_path = os.path.join(files_dir, 'logs.json')
    rules_path = os.path.join(files_dir, 'rules.json')

    logger = Logger(logger_path)
    rule_loader = RuleLoader(rules_path)
    firewall = StatefulFirewall(rule_loader.get_rules(), logger)

    rule_monitor = RuleFileMonitor(rule_loader, firewall)
    rule_monitor.start()

    try:
        firewall.logger.log("Starting packet capture...")
        sniff(prn=lambda pkt: packet_handler(pkt, firewall), store=False)
    except KeyboardInterrupt:
        firewall.logger.log("Stopping packet capture...")
    finally:
        rule_monitor.stop()


if __name__ == "__main__":
    main()
