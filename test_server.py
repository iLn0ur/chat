import json
import unittest
from server import client_msg_receive, server_resp


class TestServ(unittest.TestCase):

    def test_client_msg_receive(self):
        binary_t_msg = b'{  "action": "presense", \
                            "time": 1, \
                            "type": "status", \
                            "user": { \
                                    "account_name": "account_name",\
                                    "status": "Yep, I am here!"\
                            }\
                        }'

        message = {
            "action": "presense",
            "time": 1,
            "type": "status",
            "user": {
                "account_name": "account_name",
                "status": "Yep, I am here!"
            }
        }
        self.assertEqual(client_msg_receive(binary_t_msg), message)

    def test_server_resp(self):
        binary_t_msg = b'{"response": 200, "alert": "notification"}'
        self.assertEqual(server_resp(), binary_t_msg)


if __name__ == '__main__':
    unittest.main()
