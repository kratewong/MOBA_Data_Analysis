import json

f = open('TestOne/testResult.json')
f2 = open('TestOne/KillingInfoMatchOne.json')

matchTimeline = json.load(f)
deathInfo = json.load(f2)

# print(matchTimeline)
#
# print(deathInfo)

# data = matchTimeline["Story"]["Characters"]

length = []

for i in range(9):
    length.append(len(matchTimeline["Story"]["Characters"]["Player" + str(i + 1)]))

print(length)

for items in deathInfo:
    try:
        victimID = items['victimID']
        placeIndex = items['placeIndex']
        timestamp = items['timestamp']

        currentPlayer = "Player" + str(victimID)

        currentTimeline = matchTimeline["Story"]["Characters"][currentPlayer]

        # print(currentPlayer)
        # currentTimeline = matchTimeline[currentPlayer]
        for i in range(len(currentTimeline)):
            if timestamp == currentTimeline[i]["End"]:
                # print(matchTimeline[currentPlayer][i]["End"])
                end = timestamp
                newStart = end - 5000  # 5000 as offset
                session = placeIndex
                currentTimeline[i]["End"] = newStart
                newObj = {
                    "Start": newStart,
                    "End": end,
                    "Session": session
                }
                if victimID > 5:
                    currentTimeline[i+1]["Session"] = 17
                else:
                    currentTimeline[i+1]["Session"] = 1
                # print(currentPlayer, i, timestamp, placeIndex)
                currentTimeline.insert(i + 1, newObj)
                break

        for i in range(len(currentTimeline)):
            if currentTimeline[i]["Start"] == currentTimeline[i]["End"]:
                if len(currentTimeline) - 1 != i:
                    # print(currentPlayer, currentTimeline[i])
                    newStart = currentTimeline[i]["Start"] - 5000

                    currentTimeline[i - 1]["End"] = newStart
                    currentTimeline[i]["Start"] = newStart

                    # print(victimID)
                    # if victimID <= 5:
                    #     currentTimeline[i]["Session"] = 1
                    # else:
                    #     currentTimeline[i]["Session"] = 17
                    # print(currentPlayer, currentTimeline[i])
                    break

    except:
        KeyError

jsonString = json.dumps(matchTimeline, indent=2)
jsonFile = open("TestOne/Correction.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
