import json
import unittest
from client import get_params, form_precense


class TestClient(unittest.TestCase):

    def test_form_precense(self):
        bin_tst = form_precense()
        bin_decode = bin_tst.decode('ascii')
        json_msg = json.loads(bin_decode)
        json_msg["time"] = 1
        message = {
            "action": "presense",
            "time": 1,
            "type": "status",
            "user": {
                "account_name": "account_name",
                "status": "Yep, I am here!"
            }
        }
        self.assertEqual(json_msg, message)

    def test_get_params(self):
        self.assertEqual(['localhost', 7777], [get_params().addr, get_params().p])


if __name__ == '__main__':
    unittest.main()
