import unittest

from apis.account_api import account_list, raise_base_exception
import threading

from apis.exceptions import MyBaseException, MyDerivedException
from flask import Flask, jsonify
from User import User


class test_account_api(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.app_context = app.app_context()
        self.app_context.push()
        current_thrd = threading.currentThread()
        print(current_thrd.ident)
        current_thrd.my_prop = "Test"
        # Find from bearer header the User token and then assign it to User if none found we have an annonymoud session
        user = User("test", ["a", "b", "c"])
        current_thrd.user = user
        print(current_thrd.my_prop)

    def tearDown(self):
        self.app_context.pop()
        current_thrd = threading.currentThread()
        print("ending request")
        print(current_thrd.ident)
        print(current_thrd.my_prop)
        current_thrd.my_prop = None

    def test_account_list(self):
        response = account_list()
        self.assertEqual(response.json, [1, 2, 3, 4])
        self.assertEqual(response.status_code, 200)

    def test_raise_base_exception(self):
        with self.assertRaises(MyBaseException.MyBaseException) as ex:
            raise_base_exception()

        print(str(ex))
