DELIMETER = ","
BLANK_PLOT = "B"
GOAL_STATE = "F"
FILENAME = "input.txt"

import sys


def main(arguments):
    if arguments:
        run(filename=arguments)
    else:
        run(filename=FILENAME)


def run(filename):
    config = readFromFile(filename)
    dimensions, instructions = getDimensionsAndInstructions(config=config)
    garden = createGarden(dimensions, instructions)
    growTillConsumption(garden, verbose=False)


def readFromFile(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def getDimensionsAndInstructions(config):
    dimensions = [int(dimension) for dimension in config[0].split(",")]
    instructions = config[1:]

    return dimensions, instructions


def createGarden(dimensions, instructions):
    garden = {col: {row: BLANK_PLOT for row in range(dimensions[1])}
              for col in range(dimensions[0])}
    garden = parseAndExecuteInstructionsOnGarden(garden=garden, instructions=instructions)
    return garden


def parseAndExecuteInstructionsOnGarden(garden, instructions):
    parsedInstructions = parseInstructions(instructions)
    garden = executeParsedInstructionsOnGarden(garden, parsedInstructions)
    return garden


def parseInstructions(instructions):
    return [parseInstruction(instruction) for instruction in instructions]


def parseInstruction(instruction):
    instruction = instruction.split(",")
    instruction = instruction[0], int(instruction[1]), int(instruction[2])
    return instruction


def executeParsedInstructionsOnGarden(garden, instructions):
    for instruction in instructions:
        garden[instruction[1]][instruction[2]] = instruction[0]
    return garden


def growTillConsumption(garden, verbose=False):
    growPoints = getIvyLocations(garden)
    days = 0
    done = False
    while not done:
        growPoints = getNextCandidates(growPoints, garden)
        if not growPoints or willConsume(growPoints, garden):
            done = True
            continue
        garden = grow(growPoints, garden)
        days += 1
        if verbose:
            print(days)
            printGarden(garden)
    print(days)
    printGarden(garden)


def getIvyLocations(garden):
    ivyLocations = []
    for col in garden:
        for row in garden[col]:
            if garden[col][row] == 'I':
                ivyLocations.append((col, row))
    return ivyLocations


def getNextCandidates(growPoints, garden):
    next_candidates = []

    for growPoint in growPoints:
        possible_candidates = getCandidatesInFourDirections(growPoint)
        next_candidates.extend(getValidCandidatesInGarden(possible_candidates, garden))

    return set(next_candidates)


def getCandidatesInFourDirections(growPoint):
    north = growPoint[0], growPoint[1] - 1
    south = growPoint[0], growPoint[1] + 1
    east = growPoint[0] + 1, growPoint[1]
    west = growPoint[0] - 1, growPoint[1]

    return [north, south, east, west]


def getValidCandidatesInGarden(candidates, garden):
    return [candidate for candidate in candidates if isValid(candidate, garden)]


def isValid(candidate, garden):
    width = len(garden)
    heigth = len(garden[0])
    # print(width, heigth)
    if candidate[0] < 0 or candidate[0] > width - 1:
        return False
    if candidate[1] < 0 or candidate[1] > heigth - 1:
        return False
    if garden[candidate[0]][candidate[1]] == 'W':
        return False
    return True


def willConsume(candidates, garden):
    for candidate in candidates:
        if isFlowerButNotIvy(candidate, garden):
            return True
    return False


def isFlowerButNotIvy(candidate, garden):
    plot_contents = garden[candidate[0]][candidate[1]]
    return plot_contents == GOAL_STATE


def grow(growPoints, garden):
    for candidate in growPoints:
        garden[candidate[0]][candidate[1]] = 'I'
    return garden


def printGarden(garden):
    for row in garden:
        for col in garden[row]:
            print(garden[row][col], end="")
        print()


if __name__ == "__main__":
    main(sys.argv[1:])
