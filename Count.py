import json

f = open('lol.json')
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
            CHAMPION_KILL_INFO.append(temp_eventList[j]['timestamp'])
            CHAMPION_KILL_INFO.append(temp_eventList[j]['position'])
        if temp_eventList[j]['type'] == "CHAMPION_SPECIAL_KILL":
            CHAMPION_SPECIAL_KILL = CHAMPION_SPECIAL_KILL + 1
            CHAMPION_SPECIAL_KILL_INFO.append(temp_eventList[j]['timestamp'])
            CHAMPION_SPECIAL_KILL_INFO.append(temp_eventList[j]['position'])
        if temp_eventList[j]['type'] == "ELITE_MONSTER_KILL":
            ELITE_MONSTER_KILL = ELITE_MONSTER_KILL + 1
            ELITE_MONSTER_KILL_INFO.append(temp_eventList[j]['timestamp'])
            ELITE_MONSTER_KILL_INFO.append(temp_eventList[j]['position'])
        if temp_eventList[j]['type'] == "BUILDING_KILL":
            BUILDING_KILL = ELITE_MONSTER_KILL + 1
            BUILDING_KILL_INFO.append(temp_eventList[j]['timestamp'])

        try:
            if temp_eventList[j]['towerType']:
                BUILDING_KILL_INFO.append(temp_eventList[j]['towerType'])
            if temp_eventList[j]['buildingType']:
                BUILDING_KILL_INFO.append(temp_eventList[j]['towerType'])
        except KeyError:
            continue

print("CHAMPION_KILL: " + str(CHAMPION_KILL))
print("CHAMPION_SPECIAL_KILL: " + str(CHAMPION_SPECIAL_KILL))
print("ELITE_MONSTER_KILL: " + str(ELITE_MONSTER_KILL))
print("BUILDING_KILL: " + str(BUILDING_KILL))

print("CHAMPION_KILL_INFO: ")
print(CHAMPION_KILL_INFO)

print("CHAMPION_SPECIAL_KILL_INFO: ")
print(CHAMPION_SPECIAL_KILL_INFO)

print("ELITE_MONSTER_KILL_INFO: ")
print(ELITE_MONSTER_KILL_INFO)

print("BUILDING_KILL_INFO: ")
print(BUILDING_KILL_INFO)
