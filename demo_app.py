from flask import Flask, request
from library.demo_login import Login
from websocket import create_connection
import ssl

login = Login()
app = Flask(__name__)

@app.route('/readTag', methods=['GET'])
def readTag():
    if request.method == 'GET':
        name = request.args.get("name")

        ws = create_connection("wss://demo.edrilling.no/wells/75d178c4bc68/app/ws?access_token={}".format(
            login.access_token['access_token']), sslopt={'cert_reqs': ssl.CERT_NONE})
        ws.send('read|{}'.format(name))
        result = ws.recv()
        print(result)

        if 'read_error' in result:
            return result, 404
        else:
            return {'response': result}, 200

@app.route('/writeTag', methods=['POST'])
def writeTag():
    if request.method == 'POST':
        json_data = request.get_json()

        name = json_data['name']
        value = json_data['value']
        unix_timestamp = 0

        ws = create_connection("wss://demo.edrilling.no/wells/75d178c4bc68/app/ws?access_token={}".format(
            login.access_token['access_token']), sslopt={'cert_reqs': ssl.CERT_NONE})
        ws.send('write|{}|{}|6|{}'.format(name, unix_timestamp, value))
        return "success", 200

if __name__ == '__main__':
    app.run(port=5002)