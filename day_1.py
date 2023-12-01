import re
import unicodedata

def replace_digits(match):
    numbers = {unicodedata.name(str(i))[6:].lower(): str(i) for i in range(1,10)}
    return match.group(1) + numbers[match.group(2)] + match.group(2)[-1]

def sum_calibration_values(calibration_values):
    calibration_values = calibration_values.splitlines()
    total = 0
    for value in calibration_values:
        value = re.sub(r"^(.*?)(one|two|three|four|five|six|seven|eight|nine)", replace_digits, value)
        value = re.sub(r"^(.*)(one|two|three|four|five|six|seven|eight|nine)", replace_digits, value)
        digits = re.match(r"^[^\d]*(\d)(.*(\d))?[^\d]*$", value)
        if digits[3] is not None:
            calibration_value = f"{digits[1]}{digits[3]}"
        else:
            calibration_value = f"{digits[1]}{digits[1]}"
        calibration_value = int(calibration_value)
        total += calibration_value
    return total

if __name__ == "__main__":
    with open("inputs/day_1.txt") as f:
        calibration_values = f.read()
        total = sum_calibration_values(calibration_values)
        print(total)
