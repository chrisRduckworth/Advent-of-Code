import re

def sum_calibration_values(calibration_values):
    calibration_values = calibration_values.splitlines()
    total = 0
    for value in calibration_values:
        digits = re.match(r"^[^\d]*(\d)(.*(\d))?[^\d]*$", value)
        if digits[3] is not None:
            calibration_value = f"{digits[1]}{digits[3]}"
        else:
            calibration_value = f"{digits[1]}{digits[1]}"
        calibration_value = int(calibration_value)
        total += calibration_value
    return total

with open("inputs/day_1.txt") as f:
    calibration_values = f.read()
    print(calibration_values)
    total = sum_calibration_values(calibration_values)
    print(total)
