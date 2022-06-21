import json

event_types = set()
champion_kill_event_position = []
building_kill_event_position = []
elite_monster_kill_event_position = []

f = open('EUW1_5922388644.json')
data = json.load(f)

info = data['info']

frames = data["info"]["frames"]

events = []

timelineInfo = []  # This list will include objects with x position, y position, timestamp

# Timestamp value does not match with the player's position
# We only have around 1000 positions

# Get Player10's position and timestamps based on 100s' interval
for i in range(len(frames)):
    timelineInfo.append(frames[i]["participantFrames"]["10"]["position"])
    timelineInfo[i]['timestamp'] = frames[i]["timestamp"]

    # Loop and Save the event list
    events.append(frames[i]['events'])

# print(timelineInfo)
# Events List is a 10D array

eventsWithPos = []

# Looping through events, Find position, timestamp and its relevant event

for i in range(len(events)):
    for j in range(len(events[i])):
        try:
            if events[i][j]['position']:
                eventsWithPos.append(events[i][j])
        except KeyError:
            continue

# print(eventsWithPos[0]['timestamp'])

# for i in range(len(eventsWithPos)):
#     print(eventsWithPos[i]['timestamp'])

# Merge two lists
# timelineInfo.append(eventsWithPos[0][''])

# print(eventsWithPos)

Player10PosTime = []
Player10Time = []


# print(eventsWithPos[100]['timestamp'])
# print(eventsWithPos[10]['victimDamageDealt'][10])

def add_Info():
    Player10PosTime.append(eventsWithPos[i]['position'])
    Player10Time.append(eventsWithPos[i]['timestamp'])


# print(len(eventsWithPos))
# print(len(eventsWithPos[0]['assistingParticipantIds']))

# Find out the timestamp and position info when any events happened to the player 10
for i in range(len(eventsWithPos)):
    try:
        if eventsWithPos[i]['killerId'] == 10:
            add_Info()
            continue

        if eventsWithPos[i]['victimId'] == 10:
            # Player10PosTime.append({'x': 5, 'y': 5})  # enable this for blue team
            Player10PosTime.append({'x': 14900, 'y': 14900})    # enable this for red team
            Player10Time.append(eventsWithPos[i]['timestamp'])
            continue

        # for j in range(len(eventsWithPos[i]['assistingParticipantIds'])):
        #     if eventsWithPos[i]['assistingParticipantIds'][j] == 10:
        #         add_Info()
        #         continue

        # for j in range(len(eventsWithPos[i]['victimDamageDealt'])):
        #     if eventsWithPos[i]['victimDamageDealt'][j] == 10:
        #         add_Info()
        #         continue
        #
        # for j in range(len(eventsWithPos[i]['victimDamageReceived'])):
        #     if eventsWithPos[i]['victimDamageReceived'][j] == 10:
        #         add_Info()
        #         continue
    except KeyError:
        pass

# Cleaning the data
for i in range(len(Player10PosTime)):
    Player10PosTime[i]['timestamp'] = Player10Time[i]

# Insert Player10's position and time into timelineInfo
for i in range(len(Player10PosTime)):
    timelineInfo.append(Player10PosTime[i])

# Ordering it based on the timestamp

timelineInfo.sort(key=lambda x: x['timestamp'])

print(timelineInfo)

jsonString = json.dumps(timelineInfo)
jsonFile = open("TestOne/Player10.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

# get time stamps
# for frame in info['frames']:
#     print(frame['timestamp'])  # milliseconds

# for event in frame['events']:
#     print(event['timestamp'])
#     print(event['type'])

# unique list of event types
for frame in info['frames']:
    for event in frame['events']:
        event_types.add(event['type'])

# print(event_types)

# index = 0
# indexTwo = 0
# indexThree = 0

# for frame in info['frames']:
#     for event in frame['events']:
#         if event['type'] == 'CHAMPION_KILL':
#             # print(event['position'])
#             champion_kill_event_position.insert(index, event['position'])
#             champion_kill_event_position.insert(index + 10, event['timestamp'])
#             index = index + 10
#
#         if event['type'] == 'BUILDING_KILL':
#             building_kill_event_position.insert(index, event['position'])
#             building_kill_event_position.insert(index + 10, event['timestamp'])
#             indexTwo = indexTwo + 10
#
#         if event['type'] == 'ELITE_MONSTER_KILL':
#             elite_monster_kill_event_position.insert(index, event['position'])
#             elite_monster_kill_event_position.insert(index + 10, event['timestamp'])
#             indexThree = indexThree + 10

# print(champion_kill_event_position)
# print(building_kill_event_position)
# print(elite_monster_kill_event_position)
# print(champion_kill_event_position[0]['x'])

# Find out the timestamp and its relevant position's information
# Not based on the frame

# extract player 10's position, 100s as an interval, draw lines
# do the same to the rest
