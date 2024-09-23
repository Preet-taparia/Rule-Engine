class Alert:
    def __init__(self, communication_component):
        self.communication_component = communication_component

    def generate_alert(self, violation):
        alert_message = {
            "severity": violation["severity"],
            "description": violation["description"],
            "timestamp": violation["timestamp"],
            "ip": violation["ip"],
        }
        print("Generating alert:", alert_message)
        self.communication_component.send_log(alert_message)
                    