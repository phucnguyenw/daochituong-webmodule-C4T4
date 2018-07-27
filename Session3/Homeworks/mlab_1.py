#mongodb://<dbuser>:<dbpassword>@ds247191.mlab.com:47191/si_pho_ti_pho
import mongoengine

host = "ds247191.mlab.com"
port = 47191
db_name = "si_pho_ti_pho"
user_name =     "GGGGGG"
password =      "GGGGGG10"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())