import requests
import numpy
import json

url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
url = "https://min-api.cryptocompare.com/data/price?fsym=BTS&tsyms=BTC,USD,EUR"
url = "https://min-api.cryptocompare.com/data/price?fsym=ETC&tsyms=BTC,USD,EUR"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "258e0547-a128-5c59-1c5d-8a6fc8379b58"
}

i = 0

# for (i=0: i<2: i++)
#    response = requests.request("GET", url[i], headers=headers)
#    print(response.text)

while i < 1:
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    i += 1

binomial_name1 = response.text
group1 = binomial_name1[34:38]
print("Euro:", group1)
# def find_ryans_value(id, json_repr):
#   results = []
#   def _decode_dict(a_dict):
#       try: results.append(a_dict[id])
#       except KeyError: pass
#       return a_dict

#   json.loads(json_repr, object_hook=_decode_dict)  # Return value ignored.
#   return results

# json_repr = response.text

# print find_ryans_value('DefaultWatchlist', json_repr)
# print find_ryans_value('BTC', json_repr)
# print find_ryans_value('ETC', json_repr)
# print find_ryans_value('DASH', json_repr)
