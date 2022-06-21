import json

from PIL import Image

areaImage = Image.open('LoLBaseMap1.png')

colorToArea = {(0, 51, 153): 'BlueBase',
               (204, 204, 255): 'BlueTopLane',
               (102, 102, 255): 'TopBlueJungle',
               (255, 255, 255): 'BlueMiddleLane',
               (51, 102, 153): 'BottomRedJungle',
               (153, 255, 255): 'BlueBottomLane',
               (0, 0, 255): 'ContestedTop',
               (102, 153, 255): 'TopRiver',
               (128, 128, 128): 'ContestedMiddle',
               (0, 255, 255): 'BottomRiver',
               (51, 153, 102): 'ContestedBottom',
               (0, 255, 0): 'PurpleTopLane',
               (153, 153, 255): 'TopRedJungle',
               (220, 121, 0): 'PurpleMiddleLane',
               (255, 255, 0): 'BottomBlueJungle',
               (153, 0, 204): 'PurpleBottomLane',
               (255, 153, 204): 'PurpleBase',
               }

areaToSession = {
    'BlueBase': 1,
    'BlueTopLane': 2,
    'TopBlueJungle': 3,
    'BlueMiddleLane': 4,
    'BottomRedJungle': 5,
    'BlueBottomLane': 6,
    'ContestedTop': 7,
    'TopRiver': 8,
    'ContestedMiddle': 9,
    'BottomRiver': 10,
    'ContestedBottom': 11,
    'PurpleTopLane': 12,
    'TopRedJungle': 13,
    'PurpleMiddleLane': 14,
    'BottomBlueJungle': 15,
    'PurpleBottomLane': 16,
    'PurpleBase': 17
}

# x, y are between 0...1
def getArea(x, y):
    width, height = areaImage.size
    x = (int)(x * width)
    # print(700 - y * height)
    y = (int)(1 - y * height)
    r, g, b, a = areaImage.getpixel((x, y))
    # print(x, y)

    area = colorToArea[(r, g, b)]
    return areaToSession[area]

f = open('EUW1_5922388644Info.json')

data = json.load(f)

participantsInfo = data['info']['participants']

heroList = {}
heroInfo = []

for i in range(len(participantsInfo)):
    elem = {'participantId': participantsInfo[i]['participantId'], 'championId': participantsInfo[i]['championId'],
            'championName': participantsInfo[i]['championName']}
    heroInfo.append(elem)

def findName(id):
    for item in participantsInfo:
        if id == item['participantId']:
            # print(item['championName'])
            return item['championName']

def addInfo():
    try:
        for x in heroInfo:
            if x["participantId"] == temp_eventList[j]['killerId']:
                elem = {'timestamp': temp_eventList[j]['timestamp'],
                        'killerID': temp_eventList[j]['killerId'],
                        'killerName': x['championName'],
                        'victimID': temp_eventList[j]['victimId'],
                        'victimName': findName(temp_eventList[j]['victimId']),
                        'position': temp_eventList[j]['position'],
                        'placeIndex': getArea(temp_eventList[j]['position']['x']/15000, temp_eventList[j]['position']['y']/15000),
                        'killType': temp_eventList[j]['type']}
                # print(elem)
                CHAMPION_KILL_INFO.append(elem)
    except KeyError:
        for x in heroInfo:
            if x["participantId"] == temp_eventList[j]['killerId']:
                elem = {'timestamp': temp_eventList[j]['timestamp'],
                        'killerID': temp_eventList[j]['killerId'],
                        'killerName': x['championName'],
                        'position': temp_eventList[j]['position'],
                        'placeIndex': getArea(temp_eventList[j]['position']['x']/15000, temp_eventList[j]['position']['y']/15000),
                        'killType': temp_eventList[j]['type']}
                # print(elem)
                CHAMPION_KILL_INFO.append(elem)
                print(temp_eventList[j]['position']['x'], temp_eventList[j]['position']['y'])

f.close()

f = open('EUW1_5922388644.json')
data = json.load(f)

info = data['info']

frames = data["info"]["frames"]

p_frames = []

# set the counter
CHAMPION_KILL = 0
CHAMPION_SPECIAL_KILL = 0
ELITE_MONSTER_KILL = 0
BUILDING_KILL = 0

CHAMPION_KILL_INFO = []
CHAMPION_SPECIAL_KILL_INFO = []
ELITE_MONSTER_KILL_INFO = []
BUILDING_KILL_INFO = []

for i in range(len(frames)):
    temp_eventList = frames[i]['events']
    # print(len(temp_eventList))
    for j in range(len(temp_eventList)):
        if temp_eventList[j]['type'] == "CHAMPION_KILL":
            CHAMPION_KILL = CHAMPION_KILL + 1
            addInfo()

        # if temp_eventList[j]['type'] == "CHAMPION_SPECIAL_KILL":
        #     CHAMPION_SPECIAL_KILL = CHAMPION_SPECIAL_KILL + 1
        #     addInfo()

        # if temp_eventList[j]['type'] == "ELITE_MONSTER_KILL":
        #     ELITE_MONSTER_KILL = ELITE_MONSTER_KILL + 1
        #     addInfo()
        #
        if temp_eventList[j]['type'] == "BUILDING_KILL":
            BUILDING_KILL = ELITE_MONSTER_KILL + 1
            if 'towerType' in temp_eventList[j]:
                elem = {'timestamp': temp_eventList[j]['timestamp'],
                        'killerId': temp_eventList[j]['killerId'],
                        'towerType': temp_eventList[j]['towerType'],
                        'laneType': temp_eventList[j]['laneType'],
                        'position': temp_eventList[j]['position'],
                        'buildingType': temp_eventList[j]['buildingType'],
                        'killType': 'BUILDING_KILL'}
                # print(elem)
                CHAMPION_KILL_INFO.append(elem)
            else:
                elem = {'timestamp': temp_eventList[j]['timestamp'],
                        'killerId': temp_eventList[j]['killerId'],
                        'laneType': temp_eventList[j]['laneType'],
                        'position': temp_eventList[j]['position'],
                        'buildingType': temp_eventList[j]['buildingType'],
                        'killType': 'BUILDING_KILL'}
                # print(elem)
                CHAMPION_KILL_INFO.append(elem)

        # try:
        #     if temp_eventList[j]['towerType']:
        #         BUILDING_KILL_INFO.append(temp_eventList[j]['towerType'])
        #     if temp_eventList[j]['buildingType']:
        #         BUILDING_KILL_INFO.append(temp_eventList[j]['towerType'])
        # except KeyError:
        #     continue

print("CHAMPION_KILL: " + str(CHAMPION_KILL))
# print("CHAMPION_SPECIAL_KILL: " + str(CHAMPION_SPECIAL_KILL))
# print("ELITE_MONSTER_KILL: " + str(ELITE_MONSTER_KILL))
print("BUILDING_KILL: " + str(BUILDING_KILL))
#
# print("CHAMPION_KILL_INFO: ")
# print(CHAMPION_KILL_INFO)
#
# print("CHAMPION_SPECIAL_KILL_INFO: ")
# print(CHAMPION_SPECIAL_KILL_INFO)
#
# print("ELITE_MONSTER_KILL_INFO: ")
# print(ELITE_MONSTER_KILL_INFO)
#
# print("BUILDING_KILL_INFO: ")
# print(BUILDING_KILL_INFO)

CHAMPION_KILL_INFO.sort(key=lambda x: x["timestamp"])

jsonString = json.dumps(CHAMPION_KILL_INFO, indent=4)
jsonFile = open("TestOne/KillingInfoMatchOne.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

print("CHAMPION_KILL_INFO Json File generated, please check.")