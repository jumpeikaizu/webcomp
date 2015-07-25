import sys,urllib,json
import random
reload(sys)
sys.setdefaultencoding("utf-8")

def food_genre(food_code):
    url = urllib.urlopen(
        "http://webservice.recruit.co.jp/hotpepper/food/v1/?%s"%
        urllib.urlencode(
             {"key":"697e60c662db1c19",
             "code":food_code,#R001~R064
             "format":"json"
             })
        )
    result = json.loads(url.read())
    return result["results"]["food"][0]["name"]

def hotpepper(location):
    while 1:
        food_code = "R" + str(random.randint(1,64)).zfill(3)
        food = food_genre(food_code)
        url = urllib.urlopen(
            "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?%s"%
            urllib.urlencode(
                {"key":"697e60c662db1c19",
                 #"address":address,
                 "lat":location["lat"],
                 "lng":location["lng"],
                 "food":food_code,#R001~R064
                 "format":"json"
                })
        )
        result = json.loads(url.read())
        if result["results"]["results_available"]>0:
            break
        
    print food    
    shop = result["results"]["shop"][0]
    print shop["name"]
    print shop["urls"]["pc"]
    #print result       
    
if "__main__" == __name__:
    hotpepper(sys.argv[1].encode("utf-8"))
