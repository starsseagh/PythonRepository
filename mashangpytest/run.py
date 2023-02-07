import os
import time

import pytest

from commons.yaml_util import read_yaml_testcase

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")
