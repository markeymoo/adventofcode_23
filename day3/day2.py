import re
import logging


def openReadData(file_name: str):
    logging.info("read_data: %s", file_name)
    file_input = open(file_name, "r")
    lines = file_input.read().splitlines()

    logging.info("Lines Read: %s", lines)
    return lines


def init():
    # configure logging
    logging.basicConfig()
    logging.root.setLevel(logging.INFO)

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
        match = re.findall(r"\d", line)
        logging.info("Matched Digits: %s", match)

        first_digit = match[0]

        if len(match) == 1:
            last_digit = match[0]
        else:
            last_digit = match[len(match) - 1]

        logging.info("First Digit: %s\nSecond Digit: %s", first_digit, last_digit)

        # Adding digits together
        global calibration_value
        calibration_value += createCalibrationValue(first_digit, last_digit)

        logging.info("CalibrationValue: %d", calibration_value)


if __name__ == "__main__":
    main()
