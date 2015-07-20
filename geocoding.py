import sys
import urllib
import json
reload(sys)
sys.setdefaultencoding("utf-8")

def geocoding():
    url = urllib.urlopen(
        "http://maps.google.com/maps/api/geocode/json?%s" %
        urllib.urlencode(
            {"address":sys.argv[1].encode("utf-8"),
             "sensor":"false"
             })
        )
    result = json.loads(url.read())
    print result["results"][0]["geometry"]["location"]
if "__main__" == __name__:
    geocoding()
