data = '{"языки":["cpp","python","php","java"]}'
import json
print(json.loads(data)['языки'][1])
