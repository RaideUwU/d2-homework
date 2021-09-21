import os
import sentry_sdk

from bottle import Bottle, run, HTTPResponse, route
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
   dsn="DSN",
   integrations=[BottleIntegration()]
)

@route('/success')  
def success():  
   return HTTPResponse("200 OK", 200)

@route('/fail')
def fail():
   raise RuntimeError("fail")

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
