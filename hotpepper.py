import sys,urllib,json
reload(sys)
sys.setdefaultencoding("utf-8")
def hotpepper():
    url = urllib.urlopen(
        "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?%s"%
        urllib.urlencode(
            {"key":"697e60c662db1c19",
             "address":sys.argv[1].encode("utf-8"),
             #"lat":,"lng":,
             "food":"R038",#R001~R064
             "format":"json"
             })
        )
    result = json.loads(url.read())
    shop = result["results"]["shop"][0]
    print shop["name"]
    print shop["urls"]["pc"]
    #print result
    
if "__main__" == __name__:
    hotpepper()
