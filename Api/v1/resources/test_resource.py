import falcon
import json
from ..schemas import json_schema
from datetime import datetime as dt
from ..schemas.test import *


# TEST CLASS
# this is only to test the API

class TestResource(object):
    def __init__(self):
        super().__init__()

    @json_schema.validate(test_schema_req, test_schema_resp)
    def on_get(self, req, res):
        print('incoming GET request')
        """Handles a test GET request."""
        res.status = falcon.HTTP_200  # This is the default status
        res.media = { "message": "The TEST endpoint works fine and your API is running ;) " }
        res.json = { "message": "The TEST endpoint works fine and your API is running ;) " }
        print(res.media)

    @json_schema.validate(test_schema_req, test_schema_resp)
    def on_post(self, req, res):
        print('incoming POST request')
        """Handles a test POST request."""
        res.status = falcon.HTTP_200  # This is the default status
        res.media = { "message": "The TEST endpoint works fine and your API is running ;) " }
        res.json = { "message": "The TEST endpoint works fine and your API is running ;) " }

# TIME Endpoint
class GetTime(object):
    def on_get(self, req, res):
        print('incoming GET request')
        res.status = falcon.HTTP_200
        res.json = { 'time': dt.now().strftime("%m/%d/%Y, %H:%M:%S") }
        res.body = json.dumps(res.json)
        
    def on_post(self, req, res):
        print('incoming POST request')
        res.status = falcon.HTTP_200
        res.json = { 'time': dt.now().strftime("%m/%d/%Y, %H:%M:%S") }
        res.body = json.dumps(res.json)