
import os
from configparser import ConfigParser


class Config:

    def __init__(self):
        # determine where this file is located
        file_dir = os.path.dirname(__file__)
        filename = file_dir + '/config.cfg'

        self.config = ConfigParser()
        self.config.read(filename)

    def get_delay(self):
        return int(self.config['DEFAULT']['delay'])
