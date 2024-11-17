import json
from rule import Rule
from logger import Logger
from mailer import send_alert_email
from scapy.all import TCP, IP, ICMP, ARP, UDP

class StatefulFirewall:
    def __init__(self, rules: list[Rule], logger: Logger):
        self.rules = rules
        self.logger = logger
        self.mail_counter = 0
        self.load_mail_threshold()

    def load_mail_threshold(self):
        try:
            with open("files/settings.json", "r") as f:
                settings = json.load(f)
                self.mail_threshold = settings.get("MAIL_threshold", 10)
        except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
            print(f"Error loading MAIL_threshold: {e}")
            self.mail_threshold = 10

    def update_rules(self, rules: list[Rule]):
        """Update the list of firewall rules."""
        self.rules = rules
        self.logger.log("Firewall rules have been updated.")

    def check_packet(self, packet) -> str:
        src_ip, dst_ip, src_port, dst_port, protocol = self.extract_packet_info(packet)
        
        packet_info = {
            'source_ip': src_ip,
            'destination_ip': dst_ip,
            'source_port': src_port,
            'destination_port': dst_port,
            'protocol': protocol
        }

        for rule in self.rules:
            if rule.matches(packet_info):
                if rule.action == "MAIL":
                    self.handle_mail_action(packet_info)
                else:
                    self.log_packet(packet_info, rule.action)
                return rule.action

        self.log_packet(packet_info, 'ALLOW')
        return 'ALLOW'

    def handle_mail_action(self, packet_info):
        """Increment mail action counter and send alert if threshold is reached."""
        self.mail_counter += 1
        self.log_packet(packet_info, "MAIL")

        if self.mail_counter >= self.mail_threshold:
            subject = "Firewall Alert: Mail Threshold Reached"
            body = f"The firewall has reached the MAIL action threshold. Packet details: {packet_info}"
            send_alert_email(subject, body)
            self.mail_counter = 0

    def log_packet(self, packet_info, action):
        """Log packet details and action taken."""
        log_message = f"Packet {packet_info} action: {action}"
        self.logger.log(log_message)

    def extract_packet_info(self, packet):
        try:
            if packet.haslayer(TCP):
                tcp_layer = packet[TCP]
                ip_layer = packet[IP]
                return ip_layer.src, ip_layer.dst, tcp_layer.sport, tcp_layer.dport, 'TCP'

            elif packet.haslayer(UDP):
                udp_layer = packet[UDP]
                ip_layer = packet[IP]
                return ip_layer.src, ip_layer.dst, udp_layer.sport, udp_layer.dport, 'UDP'

            elif packet.haslayer(ICMP):
                ip_layer = packet[IP]
                return ip_layer.src, ip_layer.dst, 'any', 'any', 'ICMP'

            elif packet.haslayer(ARP):
                arp_layer = packet[ARP]
                return arp_layer.psrc, arp_layer.pdst, 'any', 'any', 'ARP'
        except Exception as e:
            self.logger.log(f"Error extracting packet info: {e}")

        return None, None, None, None, 'Invalid'

    def perform_stateful_inspection(self, packet):
        """Perform stateful inspection of a packet."""
        action = self.check_packet(packet)
        if action == 'DENY':
            print("Deny")
        elif action == "MAIL":
            print("MAIL")
        else:
            print("Allow")
