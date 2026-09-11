"""Child PR in a stack test: consumes the parent's helper."""

from stack_parent import build_auth_header


def call_api(token, client):
    headers = build_auth_header(token)
    return client.get("/v1/things", headers=headers)


def retry_call(token, client, attempts=3):
    for _ in range(attempts):
        resp = call_api(token, client)
        if resp.status_code == 200:
            return resp
    return None
