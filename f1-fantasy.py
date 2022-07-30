######### Global Variables #########

from this import d
from turtle import position


driversPositionInQualy = {}
driversPositionInRace  = {}

driversPoints = {}
driversPointsPerMillion = {}

constructorsPoints = {}
constructorsPointsPerMillion = {}

######### Drivers & Constructors #########

driversNames = [
"Lecrerc",
"Sainz",
"Verstappen",
"Perez",
"Norris", 
"Ricciardo",
"Hamilton", 
"Russel",
"Alonso",
"Ocon",
"Bottas",
"Zhou",
"Gasly",
"Tsunoda",
"Vettel",
"Stroll",
"Albon",
"Latifi",
"Magnussen",
"Mick"
]

constructorNames = [
    "Mercedes",
    "RedBull",
    "Ferrari",
    "McLaren",
    "Alpine",
    "AstonMartin",
    "AlphaTauri",
    "AlfaRomeo",
    "Williams",
    "Haas"
]

constructorDrivers = {
    "Mercedes": ["Hamilton", "Russel"],
    "RedBull": ["Verstappen", "Perez"],
    "Ferrari": ["Lecrerc", "Sainz"],
    "McLaren": ["Norris", "Ricciardo"],
    "Alpine": ["Alonso", "Ocon"],
    "AstonMartin": ["Vettel", "Stroll"],
    "AlphaTauri": ["Gasly", "Tsunoda"],
    "AlfaRomeo": ["Bottas", "Zhou"],
    "Williams": ["Albon", "Latifi"],
    "Haas": ["Magnussen", "Mick"]
}
 
######### Points Scoring #########

# Qualifying #
def calcPointsQualifying():
    global driversPositionInQualy

    for driver in driversNames:
        position = driversPositionInQualy[driver]
        print(driver + " placed "+str(position)+" in qualy")
        
        # so far, assuming no DNF's
        # Q3 Finish
        if (position <= 10):
            driversPoints[driver] += 3
        # Q2 Finish
        elif (position <= 15):
            driversPoints[driver] += 2
        # Q1 Finish
        else:
            driversPoints[driver] += 1
        
        # Beat team mate (driver only)
        if (beatTeamMateInQualy(driver)):
            driversPoints[driver] += 2    
        # to be implemented:
        # Not classified (-5pts)
        # Disqualification from qualifying (-10pts)

# Qualifying Position Bonuses #
def calcPointsQualifyingPositionBonuses():
    global driversPositionInQualy

    for driver in driversNames:
        position = driversPositionInQualy[driver]
        driversPoints[driver] += (10-position + 1) if position<=10 else 0

# Race #
def calcPointsRace():
    global driversPositionInRace, driversPositionInQualy

    for driver in driversNames:
        positionInRace = driversPositionInRace[driver]
        positionInQualy = driversPositionInQualy[driver]

        # Classified (+1pt)    
        driversPoints[driver] += 1 # assuming no DNF's

        # Per position gained (+2pts, max. +10pts)
        # Per position lost (-2pts, max. -10pts)
        diffPositions               = positionInQualy - positionInRace # positive means gained positions
        pointsGainedByOvertaking    = diffPositions*2 if abs((diffPositions)*2) <= 10 else 10*sign(diffPositions)
        driversPoints[driver]       += pointsGainedByOvertaking

        # Beat team mate (driver only) (+3pts)
        if (beatTeamMateInRace(driver)):
            driversPoints[driver] += 3

        # to be implemented:
        # Fastest lap (+5pt)
        # Not classified (-10pts)
        # Disqualification from race (-20pts)

# Race Position Bonuses #
def calcPointsRacePositionBonuses():
    global driversPositionInRace
    
    for driver in driversNames:
        position = driversPositionInRace[driver]
        driversPoints[driver] += getRaceScore(position)

# Race Streaks #
def calcPointsRaceStreaks():
    #to be implemented
    # Driver Qualifying - driver qualifies in the Top 10 for 5 qualifying sessions in a row (+5 pts)
    # Driver Race - driver finishes in the Top 10 for 5 races in a row (+10 pts)
    # Constructor Qualifying - both drivers qualify in the Top 10 for 3 qualifying sessions in a row (+5 pts)
    # Constructor Race - both drivers finish in the Top 10 for 3 races in a row (+10 pts)
    # NOTES:
    # * When a driver or constructor achieves a streak, that streak will reset and must be built up again. For example: A driver achieves five top tens in a row and will be awarded a streak, but must achieve another five top tens in a row to get streak points for a second time.
    # ** Sprint is excluded from Streaks calculations.
    pass

# Sprint #
def calcPointsSprint():
    # NOTES:
    # * Sprint Positions Gained: Sprint positions gained are relative to Qualifying finishing position.
    # ** Classification: Cars that have covered 90% of the number of laps covered by the winner (rounded down to the nears whole number of laps) will be deemed to be Classified. Cars that have covered less than 90% of the number of laps covered by the winner (rounded down to the nearest whole number of laps) will be deemed to be Not Classified. Cars that are not listed on the Sprint Starting Grid will be neither Classified nor Not Classified, and will not receive points for either event type. Classifications are based on FIA decisions.
    # *** Sprint is excluded from Streaks calculations.

    # to be implemented
    # Classified (+1pt)
    # Per position gained (max. +5 pts) (+1pt)
    # Beat team mate (driver only) (+2 pts)
    # Fastest lap (+3pts)
    # Per position lost (max. -5 pts) (-1pt)
    # Not classified (-5pts)
    # Disqualification from sprint (-10pts)
    pass

######### Getter Functions #########

def getRaceScore(position):
    points = {
        1: 25,
        2: 18,
        3: 15,
        4: 12,
        5: 10,
        6: 8,
        7: 6,
        8: 4,
        9: 2,
        10: 1,
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return points.get(position, 0)

def getDriversValue(name):
    value = {
        "Lecrerc"   :   18.8,
        "Sainz"     :   17.2,
        "Verstappen":   30.4,
        "Perez"     :   18.3,
        "Norris"    :   15.7,
        "Ricciardo" :   13.5,
        "Hamilton"  :   30.1,
        "Russel"    :   24.1,
        "Alonso"    :   12.5,
        "Ocon"      :   12.3,
        "Bottas"    :   9.7,
        "Zhou"      :   8.4,
        "Gasly"     :   12.9,
        "Tsunoda"   :   8.3,
        "Vettel"    :   11.5,
        "Stroll"    :   9.1,
        "Albon"     :   7.6,
        "Latifi"    :   6.7,
        "Magnussen" :   6.1,
        "Mick"      :   6.2
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return value.get(name, 0)

def getConstructorsValue(constructor):
    value = {
        "Mercedes"      : 33.7,
        "RedBull"       : 32.5,
        "Ferrari"       : 25.8,
        "McLaren"       : 17.5,
        "Alpine"        : 14.0,
        "AstonMartin"   : 11.1,
        "AlphaTauri"    : 10.1,
        "AlfaRomeo"     : 8.5,
        "Williams"      : 7.2,
        "Haas"          : 6.3,
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return value.get(constructor, 0)

def getDriverConstructor(name):
    for constructor in constructorNames:
        if (name in constructorDrivers[constructor]):
            return constructor
    # return nothing if constructor not found
    print("constructor not found !")
    return ""

def getResultsQualy(qualy_file):
    global driversPositionInQualy

    f = open(qualy_file, 'r')
    lines = f.readlines()
    # first, set all positions, to later calculate beatTeamMateInQualy()
    for position, driver in enumerate(lines, start=1):
        driver = driver.replace('\n','').replace(' ','')
        driversPositionInQualy[driver] = position

    #print(driversPositionInQualy)

    calcPointsQualifying()
    calcPointsQualifyingPositionBonuses()

def getResultsRace(race_file):
    f = open(race_file, 'r')
    lines = f.readlines()
    
    # first, set all positions, to later calculate beatTeamMateInQualy()
    for position, driver in enumerate(lines, start=1):
        driver = driver.replace('\n','').replace(' ','')
        driversPositionInRace[driver] = position

    calcPointsRace()
    calcPointsRacePositionBonuses()
    calcRaceStreaks()
       
def getConstructorPoints():
    d = driversPoints
    output = sorted( ((driver, points) for driver, points in d.items()), reverse=True, key=lambda item: item[1])
    print("\nPosition - Driver \tPoints")
    print("--------------------------------")
    for position, (driver, points) in enumerate(output, start=1):
        print("{0: ^8} - {1} \t {2}".format(position,driver, points))

######### Setter Functions #########

def initDriversPoints():
    global driversNames
    for driver in driversNames:
        driversPoints[driver] = 0

def setDriversPointsPerMillion():
    for name in driversNames:
        driversPointsPerMillion[name] = driversPoints[name]*1000/getDriversValue(name)  

def setConstructorPoints():
    for constructor in constructorNames:
        driver1     = constructorDrivers[constructor][0]
        driver2     = constructorDrivers[constructor][1]
        driver1Points = driversPoints[driver1]
        driver2Points = driversPoints[driver2]

        constructorsPoints[constructor] = driver1Points + driver2Points

def setConstructorPointsPerMillion():
    for constructor in constructorNames:
        constructorsPointsPerMillion[constructor] = constructorsPoints[constructor]*1000/getConstructorsValue(constructor)  

######### Print Functions #########

def printDriversPoints():
    d = driversPoints
    output = sorted( ((driver, points) for driver, points in d.items()), reverse=True, key=lambda item: item[1])
    print("\nPosition - Driver \tPoints")
    print("--------------------------------")
    for position, (driver, points) in enumerate(output, start=1):
        print("{0: ^8} - {1} \t {2}".format(position,driver, points))

def printDriversPointsPerMillion():
    d = driversPointsPerMillion
    output = sorted( ((driver, points) for driver, points in d.items()), reverse=True, key=lambda item: item[1])
    print("\nPosition - Driver \tPointsPerMillion")
    for position, (driver, pointsPerMillion) in enumerate(output, start=1):
        print("{0: ^8} - {1} \t {2}".format(position,driver, pointsPerMillion))

def printConstructorPoints():    
    d = constructorsPoints
    output = sorted( ((driver, points) for driver, points in d.items()), reverse=True, key=lambda item: item[1])
    print("\nPosition - Constructor \tPoints")
    print("--------------------------------")
    for position, (constructor, points) in enumerate(output, start=1):
        print("{0: ^8} - {1} \t {2}".format(position,constructor, points))

def printConstructorPointsPerMillion():   
    d = constructorsPointsPerMillion
    output = sorted( ((driver, points) for driver, points in d.items()), reverse=True, key=lambda item: item[1])
    print("\nPosition - Constructor \tPoints")
    print("--------------------------------")
    for position, (constructor, points) in enumerate(output, start=1):
        print("{0: ^8} - {1} \t {2}".format(position,constructor, points))

######### Aux Functions #########

def beatTeamMateInQualy(driver):
    constructor = getDriverConstructor(driver)
    teamMates = constructorDrivers[constructor]
    teamMatesAux = teamMates.copy()
    teamMatesAux.remove(driver)
    teamMate = teamMatesAux[0]
    
    driverPositionInQualy   = driversPositionInQualy[driver]
    teamMatePositionInQualy = driversPositionInQualy[teamMate]

    if (driverPositionInQualy < teamMatePositionInQualy):
        return True
    else:
        return False

def beatTeamMateInRace(driver):
    constructor = getDriverConstructor(driver)
    teamMates = constructorDrivers[constructor]
    teamMatesAux = teamMates.copy()
    teamMatesAux.remove(driver)
    teamMate = teamMatesAux[0]
    
    driverPositionInRace    = driversPositionInRace[driver]
    teamMatePositionInRace  = driversPositionInRace[teamMate]

    if (driverPositionInRace < teamMatePositionInRace):
        return True
    else:
        return False

def sign(x):
    return -1 if (x<0) else +1

######### Main #########

if __name__ == '__main__':
    
    initDriversPoints()
    getResultsQualy('qualy.txt')
    getResultsRace('race.txt')
    
    # test example
    #beatTeamMateInQualy("Bottas")

    setDriversPointsPerMillion()

    setConstructorPoints()
    setConstructorPointsPerMillion()

    printDriversPoints()
    printDriversPointsPerMillion()

    printConstructorPoints()
    printConstructorPointsPerMillion()



   