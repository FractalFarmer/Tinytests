'''
Created on Jan 22, 2023

@author: Shawn Kunkel
'''

import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass