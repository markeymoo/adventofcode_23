import re
import logging


def convert_to_digits(line: str):
    line = line.replace("oneight", "oneeight") 
    line = line.replace("threeight", "threeeight")
    line = line.replace("fiveeight", "fiveeight")
    line = line.replace("nineight", "nineeight")
    line = line.replace("twone", "twoone")
    line = line.replace("sevenine", "sevennine")
    line = line.replace("eightwo", "eighttwo")

    line = line.replace("one", "1")
    line = line.replace("two", "2") 
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")

    return line





def create_calibration_value(digit1: str, digit2: str):
    combined_string = digit1 + digit2
    logging.info("Combined String: %s", combined_string)
    calibrated_value = int(combined_string)
    logging.info("Combined Int: %d", calibrated_value)

    return calibrated_value




def read_data(file_name: str):
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
