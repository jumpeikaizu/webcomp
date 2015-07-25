import sys
from hotpepper import hotpepper
from geocoding import geocoding
reload(sys)
sys.setdefaultencoding("utf-8")
def main(address):
    hotpepper(geocoding(address))

if "__main__" == __name__:
    main(sys.argv[1].encode("utf-8"))
