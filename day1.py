import re
import logging


def convertToDigits(line: str):
    line = re.sub(r"(?:oneight)", "oneeight", line, 0)
    line = re.sub(r"(?:threeight)", "threeeight", line, 0)
    line = re.sub(r"(?:fiveeight)", "fiveeight", line, 0)
    line = re.sub(r"(?:nineight)", "nineeight", line, 0)
    line = re.sub(r"(?:twone)", "twoone", line, 0)
    line = re.sub(r"(?:sevenine)", "sevennine", line, 0)
    line = re.sub(r"(?:eightwo)", "eighttwo", line, 0)

    line = re.sub(r"(?:one)", "1", line, 0)
    line = re.sub(r"(?:two)", "2", line, 0)
    line = re.sub(r"(?:three)", "3", line, 0)
    line = re.sub(r"(?:four)", "4", line, 0)
    line = re.sub(r"(?:five)", "5", line, 0)
    line = re.sub(r"(?:six)", "6", line, 0)
    line = re.sub(r"(?:seven)", "7", line, 0)
    line = re.sub(r"(?:eight)", "8", line, 0)
    line = re.sub(r"(?:nine)", "9", line, 0)

    return line


def createCalibrationValue(digit1: str, digit2: str):
    combinedStr = digit1 + digit2
    logging.info("Combined String: %s", combinedStr)
    combinedInt = int(combinedStr)
    logging.info("Combined Int: %d", combinedInt)

    return combinedInt


def openReadData(file_name: str):
    logging.info("openReadData: %s", file_name)
    file_input = open(file_name, "r")
    lines = file_input.read().splitlines()

    logging.info("Lines Read: %s", lines)
    return lines


def init():
    # configure logging
    logging.basicConfig()
    logging.root.setLevel(logging.INFO)

    # global variables
    global calibration_value
    calibration_value = 0


def main():
    init()
    lines = openReadData("day1_input.txt")

    # iterate through all lines
    for line in lines:
        first_digit = ""
        last_digit = ""

        logging.info("Line To Process: %s", line)
        line = convertToDigits(line)
        logging.info("Line To Process: %s", line)

        # search line for first number character
        match = re.findall(r"\d{1}", line)
        logging.info("Matched Digits: %s", match)

        # was a match found
        if match is not None:
            last_match = match.__len__()
            logging.info("Len: %s", last_match)

            first_digit = match[0]

            if last_match == 1:
                last_digit = match[0]
            else:
                last_digit = match[last_match - 1]

        logging.info("First Digit: %s\nSecond Digit: %s", first_digit, last_digit)

        # Adding digits together
        global calibration_value
        calibration_value += createCalibrationValue(first_digit, last_digit)

        logging.info("CalibrationValue: %d", calibration_value)


if __name__ == "__main__":
    main()
