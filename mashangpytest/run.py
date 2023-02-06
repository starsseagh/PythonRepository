import pytest

from commons.yaml_util import read_yaml_testcase

if __name__ == '__main__':
    # pytest.main()
    print(read_yaml_testcase("testcases/test_api.yaml"))
