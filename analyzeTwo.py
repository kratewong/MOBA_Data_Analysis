import json

f = open('lol.json')
data = json.load(f)

info = data['info']

frames = data["info"]["frames"]

events = []

timelineInfo = []  # This list will include objects with x position, y position, timestamp

eventsWithPos = []


# Loop and Save the event list
for i in range(len(frames)):
    events.append(frames[i]['events'])

    # Looping through events, save position,
    # timestamp and its relevant event
    for j in range(len(events[i])):
        try:
            if events[i][j]['position']:
                eventsWithPos.append(events[i][j])
        except KeyError:
            continue

player9PosTime = []
player9Time = []

def add_Info():
    player9PosTime.append(eventsWithPos[i]['position'])
    player9Time.append(eventsWithPos[i]['timestamp'])


# Find out the timestamp and position info when any events happened to the player 9
# for i in range(len(eventsWithPos)):
#     for j in range(10):
#         try:
#             if eventsWithPos[i]['killerId'] == j+1:
#                 add_Info()
#                 continue
#
#             if eventsWithPos[i]['victimId'] == j+1:
#                 add_Info()
#                 continue
#
#             for k in range(len(eventsWithPos[i]['assistingParticipantIds'])):
#                 if eventsWithPos[i]['assistingParticipantIds'][j] == j+1:
#                     add_Info()
#                     continue
#
#             for k in range(len(eventsWithPos[i]['victimDamageDealt'])):
#                 if eventsWithPos[i]['victimDamageDealt'][j] == j+1:
#                     add_Info()
#                     continue
#
#             for k in range(len(eventsWithPos[i]['victimDamageReceived'])):
#                 if eventsWithPos[i]['victimDamageReceived'][j] == j+1:
#                     add_Info()
#                     continue
#         except KeyError:
#             pass
#
#     # Cleaning the data
#     for l in range(len(player9PosTime)):
#         player9PosTime[l]['timestamp'] = player9Time[l]
# participantFrame = []
# participantFrame.append(frames[0]["participantFrames"]) # 0 as var
# print(participantFrame[0]['1']['position']) # 0 as constant, '1' var

# Get player9's position and timestamps based on 60s' interval
for i in range(len(frames)):
    participantFrame = [frames[i]["participantFrames"]]

    for j in range(10):
        timelineInfo.append(participantFrame[0][str(j+1)]['position'])

        # timelineInfo[i]['timestamp'] = frames[i]["timestamp"]

id = 1

# insert pos / i*25+i
timelineInfo[i]['timestamp'] = frames[i]["timestamp"]

for i in range(len(timelineInfo)):
    # position i+1, index i
    if id > 10:
        id = 1
    if id <= 10:
        timelineInfo[i]['playerId'] = id
        id = id + 1

        # timelineInfo[i]['timestamp'] = frames[i]["timestamp"]

print(timelineInfo)

# Insert player9's position and time into timelineInfo

# for i in range(len(player9PosTime)):
#     timelineInfo.append(player9PosTime[i])

# Ordering it based on the timestamp

# timelineInfo.sort(key=lambda x:x['timestamp'])

# print(timelineInfo)

# jsonString = json.dumps(timelineInfo)
# jsonFile = open("combinedData.json", "w")
# jsonFile.write(jsonString)
# jsonFile.close()