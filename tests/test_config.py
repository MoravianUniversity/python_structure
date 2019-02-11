
from python_structure.config import Config


def test_config_reads_delay_():
    config = Config()
    assert config.get_delay() == 100
