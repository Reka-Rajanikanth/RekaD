# eDrilling Interview Assignment

## Prerequisite

You will be added to `e5345de3-2af0-45ae-b6e6-8087db58c664` Azure Active Directory application. (If your email is not already associated with Microsoft account, you will be prompted to create account.)

Test `JWT` can be obtained using `OAuth 2.0` client credentials flow (client secret will be provided in a separate message). You may use one of MSAL libraries (`https://github.com/orgs/AzureAD/repositories?q=Microsoft+Authentication+Library`). Azure tenant ID: `843c50bf-97b6-4efe-a805-2108a2e76a71`, client ID as above.

## Task

1. Using any programming language and framework implement `HTTP` web server with the following endpoints:

    * `GET`: `/readTag`:

        This endpoint takes query parameter `name` (e.g. `/readTag?name=ConfigData.bit.totalFlowArea`), connects to `eDrillingHub` (see below), sends `read|$name` command over `WebSocket` as expects one of the following replies (string) from `WS` server:

        * `read|$name|...`: reply with `200` `HTTP` response with `JSON` (no need to parse reply from server):
  
            ```ts
            {
                response: string;
            }
            ```

        * `read_error|$name|...`: reply with `404` `HTTP` response

    * `POST`: `/writeTag`:

        This endpoint parses `JSON` body that needs to satisfy schema:

        ```ts
        {
            name: string; // required, e.g., ConfigData.bit.totalFlowArea
            value: number; // required, e.g. 0.5
        }
        ```

        Connect to `eDrillingHub` (see below) and send command:

        ```string
        write|$name|$unixTimestampMs|6|$value
        ```

        Reply with `200` `HTTP` response

    Both endpoints need to extract `JWT` from `HTTP` `Authorization` header (e.g., `Authorization: Bearer $TOKEN`) to pass it as `access_token` query parameter for `WebSocket` connection `URI`.

     To connect to `eDrillingHub`, connect to `WS` server: `wss://demo.edrilling.no/wells/75d178c4bc68/app/ws?access_token=$TOKEN`

2. Add basic `OpenAPI v3.0.3` specification in `YAML` or `JSON` declaring query parameter schema for `GET` endpoint and `body` schema for `POST` endpoint.

3. Add `Dockerfile`

4. Push code to `GitHub` repository for us to review. N.B.: Please avoid mentioning `eDrilling` in code, and do not commit Azure AD client secret.

Bonus 1. Deploy web service to public hosting

Bonus 2. Use `Kubernetes` or/and `Docker Compose` deployments 
