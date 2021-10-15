import pytest

if __name__ == '__main__':
    dirname=""
    level='--allure-severities=critical'
    pytest.main(["-q", "-s", dirname,'--clean-alluredir',level])

