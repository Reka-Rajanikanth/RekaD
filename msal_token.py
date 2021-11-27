from msal import PublicClientApplication, ConfidentialClientApplication

# app = ConfidentialClientApplication(client_id="e5345de3-2af0-45ae-b6e6-8087db58c664", client_credential="C7P7Q~oHg6cqMHdQ6herd3xpsMofgFqeU4qsn")
# print(app)
# app = PublicClientApplication("e5345de3-2af0-45ae-b6e6-8087db58c664", authority="https://login.microsoftonline.com/843c50bf-97b6-4efe-a805-2108a2e76a71")
# print(app)
# token = app.acquire_token_by_authorization_code('C7P7Q~oHg6cqMHdQ6herd3xpsMofgFqeU4qsn', scopes=['api://e5345de3-2af0-45ae-b6e6-8087db58c664/.default'])
# print(token)

# app = ConfidentialClientApplication(client_id="e5345de3-2af0-45ae-b6e6-8087db58c664",
#                                     client_credential="C7P7Q~oHg6cqMHdQ6herd3xpsMofgFqeU4qsn",
#                                     authority="https://login.microsoftonline.com/843c50bf-97b6-4efe-a805-2108a2e76a71")
#
# print(app.acquire_token_for_client(scopes=['api://e5345de3-2af0-45ae-b6e6-8087db58c664/.default']))