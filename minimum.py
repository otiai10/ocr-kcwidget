# Python Version 2.6.6

# --- modules
from flask import Flask
from flask import request
from flask import make_response
import sys

# --- my modules
import conf
from handler import Handler

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
  (body, status) = Handler(request).handle()
  resp = make_response(body, status)
  resp.headers['Content-Type'] = 'application/json'
  return resp

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    app.debug = True
  app.run(host=conf.host,port=conf.port)
