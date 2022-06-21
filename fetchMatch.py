import urllib.request, json

api = 'RGAPI-bd7e0ddf-fefa-4be8-9cad-ce8c8c4fe9c1'

match = 'EUW1_5922388644'

with urllib.request.urlopen(
        'https://europe.api.riotgames.com/lol/match/v5/matches/' + match + '/timeline?api_key=' + api) as url:
    data = json.loads(url.read().decode())
    jsonString = json.dumps(data, indent=4)
    jsonFile = open(match+ ".json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

with urllib.request.urlopen(
        'https://europe.api.riotgames.com/lol/match/v5/matches/' + match + '?api_key=' + api) as url:
    data = json.loads(url.read().decode())
    jsonString = json.dumps(data, indent=4)
    jsonFile = open(match+ "Info.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

print("Match " + match + " data fetched!")