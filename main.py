import urllib.request, json

api = 'RGAPI-bd7e0ddf-fefa-4be8-9cad-ce8c8c4fe9c1'

with urllib.request.urlopen(
        'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/vN-WV6AAZjx6rwTrmYJb1Up6lo2b9PSKWQWYF-tePIuyqVYoUJSlkJZkY5ILr0lHOee2ugeoUNwpBw/ids?start=0&count=20&api_key=RGAPI-bd7e0ddf-fefa-4be8-9cad-ce8c8c4fe9c1') as url:
    matchList = json.loads(url.read().decode())

print(matchList)

i = 1

for match in matchList:
    with urllib.request.urlopen(
            'https://americas.api.riotgames.com/lol/match/v5/matches/' + match + '/timeline?api_key=' + api) as url:
        data = json.loads(url.read().decode())
        jsonString = json.dumps(data, indent=4)
        jsonFile = open("Match" + str(i) + ".json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        print("Match" + str(i) + "data fetched!")
    i = i + 1
