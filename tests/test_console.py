import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand
import sys
from io import StringIO


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()

    def test_do_create(self):
        sys.stdout = StringIO()
        self.hbnb.onecmd("create BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)

    def test_do_show(self):
        sys.stdout = StringIO()
        self.hbnb.onecmd("create BaseModel")
        id = sys.stdout.getvalue().strip()
        self.hbnb.onecmd("show BaseModel " + id)
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output.split(" ")[-1] == id)

    def test_do_destroy(self):
        sys.stdout = StringIO()
        self.hbnb.onecmd("create BaseModel")
        id = sys.stdout.getvalue().strip()
        self.hbnb.onecmd("destroy BaseModel " + id)
        self.hbnb.onecmd("show BaseModel " + id)
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output == "** no instance found **")

    def test_do_all(self):
        sys.stdout = StringIO()
        self.hbnb.onecmd("all")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output[0] == '[' and output[-1] == ']')

    def test_do_update(self):
        sys.stdout = StringIO()
        self.hbnb.onecmd("create BaseModel")
        id = sys.stdout.getvalue().strip()
        self.hbnb.onecmd("update BaseModel " + id + " first_name Betty")
        self.hbnb.onecmd("show BaseModel " + id)
        output = sys.stdout.getvalue().strip()
        self.assertTrue("'first_name': 'Betty'" in output)


if __name__ == "__main__":
    unittest.main()
