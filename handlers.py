def download(request):
    filename = request.args["file"]
    return open("/data/" + filename).read()
