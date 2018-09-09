from bson import json_util
import json
def tojson(object):
    if object:
        return json.loads(json_util.dumps(object))
    else:
        return None