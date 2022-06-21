import json

killingInfo = open('KillingInfo.json')

killingData = json.load(killingInfo)

f = open('Match6/player1.json')
f2 = open('Match6/player2.json')
f3 = open('Match6/player3.json')
f4 = open('Match6/player4.json')
f5 = open('Match6/player5.json')
f6 = open('Match6/player6.json')
f7 = open('Match6/player7.json')
f8 = open('Match6/player8.json')
f9 = open('Match6/player9.json')
f10 = open('Match6/player10.json')

dataList = [json.load(f), json.load(f2), json.load(f3),
            json.load(f4), json.load(f5), json.load(f6),
            json.load(f7), json.load(f8), json.load(f9), json.load(f10)]

for item in killingData:
    # Based on Killer ID, we save the data
    try:

        timestamp = item['timestamp'] # Find timestamp of killing events

        # Find Killer ID and retrieve the player trajectory and save it to the list
        dataKiller = dataList[int(item['killerID']-1)]
        # The same to the Victim ID
        dataVictim = dataList[int(item['victimID']-1)]

        currentKiller = str(item['killerID'])
        currentVictim = str(item['victimID'])

        # print(dataKiller)

        for i in range(len(dataKiller)):
            # have = False
            if timestamp == dataKiller[i]['timestamp']:
                for j in range(len(dataVictim)):
                    if timestamp == dataVictim[j]['timestamp']:
                        try:
                            if timestamp == dataVictim[j]['timestamp']:
                                # print out the movements right before and after the killing event
                                print(item)

                                print("KillerID: " + currentKiller)
                                print(dataKiller[i-1])
                                print(dataKiller[i])
                                print(dataKiller[i+1])
                                print(dataKiller[i + 2])

                                print("VictimID: " + currentVictim)
                                print(dataVictim[j-1])
                                print(dataVictim[j])
                                print(dataVictim[j+1])
                                print(dataVictim[j + 2])

                                print("------------------------")
                        except KeyError:
                            continue

    except KeyError:
        continue