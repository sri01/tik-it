#from HydMetroTicketing.Input import *
from HydMetroTicketing.Input.InputData import *
from string import *

def isStationPresentIn(station, line):
    if station in line.keys():
        return 1
    else:
        return 0

print('Hello World')

def getLineOfStation(station):
    ListName = None
    if(isStationPresentIn(station, line_1)):
        return line_1
    elif isStationPresentIn(station, line_2):
        return line_2
    elif isStationPresentIn(station, line_3):
        return line_3


def getJunctionInLine(line):
    JunctionsList = []
    #for each  key of list:
     #       if key starts with x
     #           JunctionsList.add(list.keys().value
    for station in line.keys():

        if station.startswith("X"):
            JunctionsList.append(list(line.keys()).index(station))

    print(JunctionsList)

    return(JunctionsList)

def getIndexOf(station):
    line = getLineOfStation(station)
    return(list(line.keys()).index(station))
    # end of getIndexOf


def getDistance(station1Index, station2Index):
    # assumption both are same line

    #print(list(line1.keys()).index(station1))
    #print(list(line2.keys()).index(station2))
    return(abs(station1Index - station2Index))


    # End of getDistance



def getNearestJunction(station, JunctionListIndex):
    distanceList=[]
    print("Insude getNearestJucntion")

    stationLine = getLineOfStation(station)
    stationIndex = list(stationLine.keys()).index(station)

    print("Station: " + station)
    print("station INdex: ")
    print(stationIndex)
    print("JUnction List: ")
    print(JunctionListIndex)

    for JunctionIndex in JunctionListIndex:
        d = getDistance(stationIndex, JunctionIndex)
        distanceList.append(d)

    print("Distance List: ")
    print(distanceList)

    return(JunctionListIndex[distanceList.index(min(distanceList))])
    #if station is before nearest junction
    # if   (stationIndex < JunctionListIndex[list(distanceList.keys()).index(min(distanceList))]):
    #    return(stationIndex + min(distanceList))
    #elif (stationIndex > JunctionListIndex[list(distanceList.keys()).index(min(distanceList))]):
    #    return(stationIndex - min(distanceList))
    # End of getNearestJunction


print('End of world!')