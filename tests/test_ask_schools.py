from ask_schools import __version__
from ask_schools import find_schools_by_mentee_suffix


def test_version():
    assert __version__ == '0.1.0'

def check_school_name_equal_toronto():
    result = find_schools_by_mentee_suffix('_tor')
    assert result == 'Tordonto'
