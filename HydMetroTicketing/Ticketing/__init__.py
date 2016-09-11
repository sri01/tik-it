from HydMetroTicketing.DerivedInput import *

#
ready = 1
def readyForTickets():
    print("Enter source station: ")
    SourceStation = str(input().strip())
    print("Enter destination station: ")
    DestStation = str(input().strip())

    print("Entered stations: ", SourceStation, DestStation)
    source_line = getLineOfStation(SourceStation)
    if source_line == None:
        print("Invalid station name")
        exit()
    else:
        # print(SourceStation, ' exists in ', source_line)
        print("hi")
    dest_line = getLineOfStation(DestStation)
    if dest_line == None:
        print("Invalid station name")
        exit()
    else:
        # print(DestStation, ' exists in ', dest_line)
        print("hi")

    if source_line != dest_line:

        # get junctions in each source and dest lines
        SourceLineJunctions = getJunctionInLine(source_line)
        DestLineJunctions = getJunctionInLine(dest_line)

        # get nearest junction to source and dest
        SourceNearestJunctionIndex = getNearestJunction(SourceStation, SourceLineJunctions)
        DestNearestJunctionIndex = getNearestJunction(DestStation, DestLineJunctions)
        print("#######Source Details: ")
        print(SourceStation)
        print(getIndexOf(SourceStation))
        print("Jucntions that are in same line as Source")
        print(SourceLineJunctions)
        print("SourceNearestJunctionIndex: ")
        print(SourceNearestJunctionIndex)

        print("#####Destination Details:")
        print(DestStation)
        print(getIndexOf(DestStation))
        print("Jucntions that are in same line as Dest")
        print(DestLineJunctions)
        print("DestNearestJunctionIndex: ")
        print(DestNearestJunctionIndex)
        # Distance = number of stations b/w src and dest
       # TotalDistance = getDistance(getIndexOf(SourceStation), SourceNearestJunctionIndex) + getDistance(getIndexOf(DestStation), DestNearestJunctionIndex) \
       #       + getDistance(SourceNearestJunctionIndex, DestNearestJunctionIndex)

        # calculateTicket(TotalDistance, line_number)
    else:
        # source and dest are in same line
        # get distance b/w stations
        print("hi")
        #TotalDistance = getDistance(SourceStation, DestStation)

         #calculateTicket(TotalDistance, line_number)


if ready:
    readyForTickets()
else:
    print("not ready yet, derived input has to get ready...")