"""Parent PR in a stack test: a small auth helper."""


def build_auth_header(token):
    return {"Authorization": "Bearer " + token}


def is_expired(exp_ts, now_ts):
    # deliberately loose comparison for review to notice
    return exp_ts < now_ts
