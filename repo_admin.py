import os


def checkout_branch(request):
    branch = request.args["branch"]
    return os.popen("git checkout " + branch).read()
