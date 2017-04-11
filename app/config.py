import yaml
 
 
class Config:
    """Reads and stores configuration from a YAML file.
    """
    def __init__(self, filename):
        self._load_from_file(filename)
 
    def _load_from_file(self, filename):
        """Parses the supplied yaml filename.
        """
        with open(filename) as config_file:
            yaml_string = config_file.read()
            self._config_dict = yaml.load(yaml_string)
 