import json
import cv2
from PIL import Image

areaImage = Image.open('LoLBaseMap1.png')

image = cv2.imread('LoLBaseMap1.png')
height = image.shape[0]
width = image.shape[1]

factor = height / 15000
colour = (0, 0, 225)
thickness = -1

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

# Generating json for feeding

LOLTimeline = {
    "Story": {
        "Locations": {
            "BlueBase": [1],
            "BlueTopLane": [2],
            "TopBlueJungle": [3],
            "BlueMiddleLane": [4],
            "BottomRedJungle": [5],
            "BlueBottomLane": [6],
            "ContestedTop": [7],
            "TopRiver": [8],
            "ContestedMiddle": [9],
            "BottomRiver": [10],
            "ContestedBottom": [11],
            "PurpleTopLane": [12],
            "TopRedJungle": [13],
            "PurpleMiddleLane": [14],
            "BottomBlueJungle": [15],
            "PurpleBottomLane": [16],
            "PurpleBase": [17]
        },
        "Characters": {
            "Player1": [],
            "Player2": [],
            "Player3": [],
            "Player4": [],
            "Player5": [],
            "Player6": [],
            "Player7": [],
            "Player8": [],
            "Player9": [],
            "Player10": []
        }
    }
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
    bx = x
    by = y
    print(bx, by)
    x = (int)(x * width)
    # print(700 - y * height)
    y = (int)(1 - y * height)
    r, g, b, a = areaImage.getpixel((x, y))
    # print(r)
    # print(g)
    # print(b)
    print(x, y)

    area = colorToArea[(r, g, b)]

    #
    # if (r, g, b) in colorToArea.keys():
    #     area = colorToArea[(r, g, b)]
    #     cv2.circle(image, (x, -y), radius=5, color=(0, 0, 255), thickness=-1)
    #     cv2.imshow("LOL VIS", image)
    #     cv2.waitKey(100)
    # else:
    #     cv2.circle(image, (x, -y), radius=30, color=(255, 255, 0), thickness=-1)
    #     print("Add rgb to dict: " + str(r) + " " + str(g) + " " + str(b))
    #     cv2.waitKey(0)

    if bx == 11808/15000 and by == 1687/15000:
        area = colorToArea[(r, g, b)]
        cv2.circle(image, (x, -y), radius=5, color=(0, 0, 255), thickness=-1)
        cv2.imshow("LOL VIS", image)
        print(r,g,b)
        print(area)
        cv2.waitKey(0)

    # if bx == 11211/15000 and by == 10946/15000:
    #     area = colorToArea[(r, g, b)]
    #     cv2.circle(image, (x, -y), radius=5, color=(0, 0, 255), thickness=-1)
    #     cv2.imshow("LOL VIS", image)
    #     print(r,g,b)
    #     print(area)
    #     cv2.waitKey(0)

    print(areaToSession[area])
    return areaToSession[area]


f = open('TestOne/player1.json')
f2 = open('TestOne/player2.json')
f3 = open('TestOne/player3.json')
f4 = open('TestOne/player4.json')
f5 = open('TestOne/player5.json')
f6 = open('TestOne/player6.json')
f7 = open('TestOne/player7.json')
f8 = open('TestOne/player8.json')
f9 = open('TestOne/player9.json')
f10 = open('TestOne/player10.json')

fileOpenList = [f, f2, f3, f4, f5, f6, f7, f8, f9, f10]

playerList = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7', 'Player8',
              'Player9', 'Player10']

for i in range(len(playerList)):
    data = json.load(fileOpenList[i])

    for j in range(len(data) - 1):
        # Original Image (Map) size is 15000 * 15000, X and Y needs to be scaled
        x = data[j]['x'] / 15000
        y = data[j]['y'] / 15000

        # CV2 for debugging

        # cv2.imshow("LOL VIS", image)

        # pointOneX = int((data[j]['x']) * factor)
        # pointOneY = int((15000 - data[j]['y']) * factor)
        # pointTwoX = int((data[j+1]['x']) * factor)
        # pointTwoY = int((15000 - data[j+1]['y']) * factor)
        # start_point = (pointOneX, pointOneY)
        # end_point = (pointTwoX, pointTwoY)
        # image = cv2.line(image, start_point, end_point, colour, 1)

        obj = {
            "Start": data[j]['timestamp'],
            "End": data[j + 1]['timestamp'],
            "Session": getArea(x, y)
        }

        LOLTimeline["Story"]["Characters"][playerList[i]].append(obj)

    lastObj = {
        "Start": data[len(data) - 1]['timestamp'],
        "End": data[len(data) - 1]['timestamp'],
        "Session": getArea(x, y)
    }

    LOLTimeline["Story"]["Characters"][playerList[i]].append(lastObj)

    # CV2 for debugging
    # cv2.imshow("LOL VIS", image)
    # cv2.waitKey(0)

    jsonString = json.dumps(LOLTimeline, indent=2)
    jsonFile = open("TestOne/testResult.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
