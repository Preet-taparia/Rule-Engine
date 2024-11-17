import json

from rule import Rule

class RuleLoader:
    """
    A class to handle loading and managing firewall rules from a JSON file.

    Attributes:
        json_file (str): Path to the JSON file containing the rules.
        rules (list): A list of Rule objects loaded from the JSON file.
    """
    def __init__(self, json_file):
        self.json_file = json_file
        self.rules = []
        self.load_rules()

    def load_rules(self):
        """
        Load rules from the JSON file and initialize Rule objects.
        """
        with open(self.json_file, 'r') as f:
            rules_data = json.load(f)
        self.rules = [Rule(**rule) for rule in rules_data]

    def get_rules(self):
        return self.rules
