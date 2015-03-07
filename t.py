from pprint import pprint
from collections import OrderedDict
import json
class JSONObject:
	def __init__(self, d):
		self.__dict__ = d


dat1 = '{"t":123,"ter":{"re":789,"wer":{"kan":234,"ass":897}},"qwer":2345,"gte":567}'
dat = "{'t':123,'ter':{'re':789,'wer':{'kan':234,'ass':897}},'qwer':2345,'tre':567}"
data = json.loads(dat,object_hook=JSONObject)
print(data.ter.wer.ass)
