import json
import copy
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

# x, y are between 0...1
def getAreaName(x, y):
    width, height = areaImage.size
    x = (int)(x * width)
    y = (int)(height - y * height)
    r, g, b, a = areaImage.getpixel((x, y))

    area = colorToArea[(r, g, b)]

    return area


def getArea(x, y):
    width, height = areaImage.size
    x = (int)(x * width)
    y = (int)(height - y * height)
    r, g, b, a = areaImage.getpixel((x, y))

    area = colorToArea[(r, g, b)]
    return areaToSession[area]
    

event_types = set()
champion_kill_event_position = []
building_kill_event_position = []
elite_monster_kill_event_position = []

f = open('EUW1_5922388644.json')
data = json.load(f)

info = data['info']
frames = data["info"]["frames"]


# Timestamp value does not match with the player's position
# We only have around 1000 positions

def add_Info():
    PlayerPosTime.append(eventsWithPos[i]['position'])
    PlayerTime.append(eventsWithPos[i]['timestamp'])


currentPlayerID = 0

for p in range(1,11):
    currentPlayerID = p
    
    events = []
    timelineInfo = []  # This list will include objects with x position, y position, timestamp
    
    # Get Player's position and timestamps based on 100s' interval
    for i in range(len(frames)):
        timelineInfo.append(frames[i]["participantFrames"][str(currentPlayerID)]["position"])
        timelineInfo[i]['timestamp'] = frames[i]["timestamp"]

        # Loop and Save the event list
        events.append(frames[i]['events'])

    eventsWithPos = []

    # Looping through events, Find position, timestamp and its relevant event
    for i in range(len(events)):
        for j in range(len(events[i])):
            if events[i][j]['type'] == "CHAMPION_KILL" and events[i][j]['victimId'] == currentPlayerID:
                time = events[i][j]['timestamp']
                time1 = time - 250
                time2 = time + 250
                copy1 = copy.copy(events[i][j])
                copy2 = copy.copy(events[i][j])
                copy1['timestamp'] = time1
                copy2['timestamp'] = time2
                eventsWithPos.append(copy1)
                eventsWithPos.append(copy2)
                #print(time1)
                #print(time2)
                
                victimID = events[i][j]['victimId']
                x = events[i][j]['position']['x']
                y = events[i][j]['position']['y']
                area = getAreaName(x / 15000, y / 15000)
                
                print("playerID = " + str(victimID) + " area = " + area + " time = " + str(time1) + "- D")
                print("playerID = " + str(victimID) + " area = " + area + " time = " + str(time) + "< D")
                print("playerID = " + str(victimID) + " area = " + area + " time = " + str(time2) + "+ D")
                
            else:
                try:
                    if events[i][j]['position'] and events[i][j]['participantId'] == currentPlayerID:
                        eventsWithPos.append(events[i][j])
                except KeyError:
                    continue

    PlayerPosTime = []
    PlayerTime = []
    
    # Find out the timestamp and position info when any events happened to the player
    for i in range(len(eventsWithPos)):
        try:
            if eventsWithPos[i]['killerId'] == currentPlayerID:
                add_Info()
                continue

            # go back to base after being killed
            if eventsWithPos[i]['victimId'] == currentPlayerID:
                if currentPlayerID <= 5:
                    PlayerPosTime.append({'x': 5, 'y': 5})            # blue team
                    area = getAreaName(50 / 15000, 50 / 15000)
                else:
                    PlayerPosTime.append({'x': 14900, 'y': 14900})    # red team
                    area = getAreaName(14900 / 15000, 14900 / 15000)
                    
                newtime = eventsWithPos[i]['timestamp'] + 500
                PlayerTime.append(newtime)
                print("playerID = " + str(currentPlayerID) + " area = " + area + " time = " + str(newtime) + " > base")
                continue

        except KeyError:
            pass

    # Cleaning the data
    for i in range(len(PlayerPosTime)):
        PlayerPosTime[i]['timestamp'] = PlayerTime[i]

    # Insert Player10's position and time into timelineInfo
    for i in range(len(PlayerPosTime)):
        timelineInfo.append(PlayerPosTime[i])

    # Ordering it based on the timestamp
    timelineInfo.sort(key=lambda x: x['timestamp'])

    #print(timelineInfo)

    jsonString = json.dumps(timelineInfo)
    jsonFile = open("TestOne/Player" + str(currentPlayerID) + ".json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
