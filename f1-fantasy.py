# global vars

driversPositionInQualy = {}
driversPositionInRace  = {}

driversPoints = {}
driversPointsPerMillion = {}

constructorsPoints = {}
constructorsPointsPerMillion = {}

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

def initDriversPoints():
    global driversNames
    for name in driversNames:
        driversPoints[name] = 0

def fillDriversPointsPerMillion():
    for name in driversNames:
        driversPointsPerMillion[name] = driversPoints[name]*1000/getDriversValue(name)  

def fillConstructorPoints():
    for constructor in constructorNames:
        driver1     = constructorDrivers[constructor][0]
        driver2     = constructorDrivers[constructor][1]
        driver1Points = driversPoints[driver1]
        driver2Points = driversPoints[driver2]

        constructorsPoints[constructor] = driver1Points + driver2Points

def fillConstructorPointsPerMillion():
    for constructor in constructorNames:
        constructorsPointsPerMillion[constructor] = constructorsPoints[constructor]*1000/getConstructorsValue(constructor)  

def getDriverConstructor(name):
    for constructor in constructorNames:
        if (name in constructorDrivers[constructor]):
            return constructor
    # return nothing if constructor not found
    print("constructor not found !")
    return ""

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

def getResultsQualy(path):
    global driversPositionInQualy

    f = open(path, 'r')
    lines = f.readlines()
    # first, fill all positions, to later calculate beatTeamMateInQualy()
    for position, driver in enumerate(lines, start=1):
        driver = driver.replace('\n','').replace(' ','')
        driversPositionInQualy[driver] = position

    #print(driversPositionInQualy)

    for position, driver in enumerate(lines):
        driver = driver.replace('\n', '').replace(' ', '')
        driversPoints[driver] += (10-position) if position<10 else 0
        if (position <= 15):
            driversPoints[driver] += 1
        if (position <= 10):
            driversPoints[driver] += 2 + 3
        if (beatTeamMateInQualy(driver)):
            driversPoints[driver] += 2    

def getResultsRace(path):
    f = open(path, 'r')
    lines = f.readlines()
    
    # first, fill all positions, to later calculate beatTeamMateInQualy()
    for position, driver in enumerate(lines, start=1):
        driver = driver.replace('\n','').replace(' ','')
        driversPositionInRace[driver] = position

    for position, driver in enumerate(lines, start=1):
        driver = driver.replace('\n', '').replace(' ', '')
        driversPoints[driver] += 1 # 1 point for finishing the race
        driversPoints[driver] += getRaceScore(position) # race score
        if (beatTeamMateInRace(driver)):
            driversPoints[driver] += 3
        
        # positive result means gained positions
        diffPositions = driversPositionInQualy[driver] - driversPositionInRace[driver]
        if (diffPositions > 0): # if gained positions
            driversPoints[driver] += 2*diffPositions if abs(2*diffPositions)<=10 else 10
        elif (diffPositions < 0): # if lost positions
            driversPoints[driver] -= 2*diffPositions if abs(2*diffPositions)<=10 else 10
        else: ## same position in qualy and race
            pass

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

def getConstructorPoints():
    d = driversPoints
    output = sorted( ((driver, points) for driver, points in d.items()), reverse=True, key=lambda item: item[1])
    print("\nPosition - Driver \tPoints")
    print("--------------------------------")
    for position, (driver, points) in enumerate(output, start=1):
        print("{0: ^8} - {1} \t {2}".format(position,driver, points))

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

if __name__ == '__main__':
    
    initDriversPoints()
    getResultsQualy('qualy.txt')
    getResultsRace('race.txt')
    
    # test example
    #beatTeamMateInQualy("Bottas")

    fillDriversPointsPerMillion()

    fillConstructorPoints()
    fillConstructorPointsPerMillion()

    printDriversPoints()
    printDriversPointsPerMillion()

    printConstructorPoints()
    printConstructorPointsPerMillion()



   