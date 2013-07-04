from util_gae import FixSysPath
FixSysPath()

import unittest
import sys
import webtest
import webapp2
import os
import pprint
import xml.dom.minidom
import urlparse

WEBSITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(WEBSITE_DIR)
import main


class LocalTests(unittest.TestCase):
    def setUp(self):
        self.testRoutes = main.GLOBAL_ROUTES

    def test_DescriptionsAccuracy(self):
        return

if __name__ == '__main__':
    for x in [LocalTests]:
        unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(x))
