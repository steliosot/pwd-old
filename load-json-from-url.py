import urllib.request, json
def get_data_from_url(myURL):
    with urllib.request.urlopen(myURL) as url:
        data = json.loads(url.read().decode())
        return(data)

