import sys
import urllib
import json
reload(sys)
sys.setdefaultencoding("utf-8")

def geocoding(address):
    url = urllib.urlopen(
        "http://maps.google.com/maps/api/geocode/json?%s" %
        urllib.urlencode(
            {"address":address,
             "sensor":"false"
             })
        )
    result = json.loads(url.read())
    return result["results"][0]["geometry"]["location"]

if "__main__" == __name__:
    print geocoding(sys.argv[1].encode("utf-8"))
