from msal import PublicClientApplication, ConfidentialClientApplication
import os, json

class Login(object):

    def __init__(self):
        self.access_token = self.login()

    def login(self):
        with open(os.getcwd()+"/resources/properties.json", "r") as f:
            content = json.loads(f.read())
            app = ConfidentialClientApplication(client_id=content['client_id'],
                                                client_credential=content['secret_key'],
                                                authority="https://login.microsoftonline.com/{}".format(content['tenant_id']))
            access_token = app.acquire_token_for_client(scopes=['api://{}/.default'.format(content['client_id'])])
            return access_token