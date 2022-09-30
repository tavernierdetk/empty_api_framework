import json
import falcon
import datetime as dt

from Api.middleware.cors import *

app = falcon.API(middleware=[CorsMiddleware()])

from Api.routes import *

print('['+ dt.now().strftime('%Y-%m-%d %H:%M:%S') +']' + ' Routes loaded ! ✅')
print('['+ dt.now().strftime('%Y-%m-%d %H:%M:%S') +']' + ' This server is ready !')


