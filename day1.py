import re
import logging

logging.basicConfig()
logging.root.setLevel(logging.INFO)

file_input = open("day1_input.txt", "r")
lines = file_input.read().splitlines()

logging.info("Lines Read: %s", lines)
calibration_value = 0

for line in lines:
    first_digit = ""
    last_digit = ""

    logging.info("Line To Process: %s", line)

    # search line for first number character
    match = re.findall(r"[0-9]+", line)
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
    calibration_value += int(first_digit) + int(last_digit)
    logging.info("CalibrationValue: %d", calibration_value)
