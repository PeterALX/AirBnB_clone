#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


# think about them tests
class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_isinstance(self):
        self.assertIsInstance(self.base, BaseModel)

    def test_to_dict(self):
        d = self.base.to_dict()
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)
        self.assertIsInstance(d['id'], str)
