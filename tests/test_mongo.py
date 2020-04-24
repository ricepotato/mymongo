# -*- coding: utf-8 -*-

import unittest
from unittest.mock import Mock, call

from app.mongo import mongo


class SomeTestCase(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test(self):
        users = mongo()
        assert users
        print(users)
