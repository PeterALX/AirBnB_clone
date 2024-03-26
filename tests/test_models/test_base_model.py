#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import json


# think about them tests
class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_init(self):
        self.assertIsInstance(self.base, BaseModel)

    def test_kwargs_init(self):
        model = BaseModel()
        model_dict = model.to_dict()
        model_clone = BaseModel(**model_dict)
        self.assertFalse(model_clone is model)

    def test_to_dict(self):
        d = self.base.to_dict()
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)
        self.assertIsInstance(d['id'], str)

    def test_str(self):
        string_rep = f'[BaseModel] ({self.base.id}) {self.base.__dict__}'
        self.assertEqual(str(self.base), string_rep)

    def test_save(self):
        self.base.save()
        key = 'BaseModel' + "." + self.base.id
        with open('db.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], self.base.to_dict())
