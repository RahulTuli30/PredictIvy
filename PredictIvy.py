DELIMETER = ","
BLANK_PLOT = "B"
import pprint

pp = pprint.PrettyPrinter(indent=4)


def main(filename="input.txt"):
    config = readFromFile(filename)
    dimensions, instructions = getDimensionsAndInstructions(config=config)
    garden = createGarden(dimensions, instructions)
    pp.pprint(garden)
    pass


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


if __name__ == "__main__":
    main()
