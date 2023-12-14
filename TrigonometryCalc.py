import os
import math

# [A, B , C, ∠AC, ∠BC]
var_values = ["N/A", "N/A", "N/A", "N/A", "N/A"]


display_print = f"""
  (3) ∠AC
      |\ 
      | \ 
(0) A |  \ C (2)
      |   \ 
      |____\ ∠BC (4)
    (1) B
"""


def display_guide():
    os.system("cls")
    print(display_print)
    print(f"A = {var_values[0]}") if var_values[0] != "N/A" else print("", end="")
    print(f"B = {var_values[1]}") if var_values[1] != "N/A" else print("", end="")
    print(f"C = {var_values[2]}") if var_values[2] != "N/A" else print("", end="")
    print(f"∠AC = {var_values[3]}°") if var_values[3] != "N/A" else print("", end="")
    print(f"∠BC = {var_values[4]}°") if var_values[4] != "N/A" else print("", end="")
    print("-------------------------")


def variable_available(var):
    if not var.isdigit():
        return False
    try:
        if var_values[int(var)] == "N/A":
            return True
    except Exception as e:
        print(e)
        return False


def assign_variables():
    variable = input(f"({i+1}) Given Variable: ")
    while not variable_available(variable):
        variable = input(f"({i+1}) Given Variable: ")
    while True:
        try:
            value = float(input(f"({i+1}) Value: "))
            if int(variable) == 3 or int(variable) == 4:  # if angles was chosen
                if value >= 90:
                    print("Angle Must Be Less Than 90")
                    continue
                var_values[3 if int(variable) == 4 else 4] = 90 - value

            # Code below ensures hypotenuse is always longer than the two sides

            # If side A has a value and hypotenuse is selected
            if (var_values[0] != "N/A") and int(variable) == 2:
                if var_values[0] >= value:
                    print("Hypotenuse Must Be Longer Than Side A")
                    continue
            # If side B has a value and hypotenuse is selected
            if (var_values[1] != "N/A") and int(variable) == 2:
                if var_values[1] >= value:
                    print("Hypotenuse Must Be Longer Than Side B")
                    continue

            # If hypotenuse has a value and side A is selected
            if (var_values[2] != "N/A") and int(variable) == 0:
                if var_values[2] <= value:
                    print("Side A Must Be Shorter Than Hypotenuse")
                    continue
            # If hypotenuse has a value and side B is selected
            if (var_values[2] != "N/A") and int(variable) == 1:
                if var_values[2] <= value:
                    print("Side B Must Be Shorter Than Hypotenuse")
                    continue

            break
        except Exception as e:
            continue

    var_values[int(variable)] = value
    display_guide()


def is_not_NA(var1, var2):
    if var_values[var1] == "N/A" or var_values[var2] == "N/A":
        return False
    return True


def calculate_trigonometry():
    if is_not_NA(0, 1):
        var_values[2] = round(math.sqrt(var_values[0] ** 2 + var_values[1] ** 2), 4)
        var_values[3] = round(math.degrees(math.atan(var_values[1] / var_values[0])), 4)
        var_values[4] = round(math.degrees(math.atan(var_values[0] / var_values[1])), 4)
    elif is_not_NA(0, 2):
        var_values[1] = round(math.sqrt(var_values[2] ** 2 - var_values[0] ** 2), 4)
        var_values[3] = round(math.degrees(math.atan(var_values[1] / var_values[0])), 4)
        var_values[4] = round(math.degrees(math.atan(var_values[0] / var_values[1])), 4)
    elif is_not_NA(1, 2):
        var_values[0] = round(math.sqrt(var_values[2] ** 2 - var_values[1] ** 2), 4)
        var_values[3] = round(math.degrees(math.atan(var_values[1] / var_values[0])), 4)
        var_values[4] = round(math.degrees(math.atan(var_values[0] / var_values[1])), 4)
    elif is_not_NA(0, 3):
        var_values[1] = round(var_values[0] * math.tan(math.radians(var_values[3])), 4)
        var_values[2] = round(math.sqrt(var_values[0] ** 2 + var_values[1] ** 2), 4)
    elif is_not_NA(1, 3):
        var_values[0] = round(var_values[1] / math.tan(math.radians(var_values[3])), 4)
        var_values[2] = round(math.sqrt(var_values[0] ** 2 + var_values[1] ** 2), 4)
    elif is_not_NA(2, 3):
        var_values[0] = round(var_values[2] * math.cos(math.radians(var_values[3])), 4)
        var_values[1] = round(var_values[2] * math.sin(math.radians(var_values[3])), 4)
    elif is_not_NA(0, 4):
        var_values[1] = round(var_values[0] / math.tan(math.radians(var_values[4])), 4)
        var_values[2] = round(math.sqrt(var_values[0] ** 2 + var_values[1] ** 2), 4)
    elif is_not_NA(1, 4):
        var_values[0] = round(var_values[1] * math.tan(math.radians(var_values[4])), 4)
        var_values[2] = round(math.sqrt(var_values[0] ** 2 + var_values[1] ** 2), 4)
    elif is_not_NA(2, 4):
        var_values[0] = round(var_values[2] * math.sin(math.radians(var_values[4])), 4)
        var_values[1] = round(var_values[2] * math.cos(math.radians(var_values[4])), 4)


display_guide()
given_variables = []
for i in range(2):
    assign_variables()
calculate_trigonometry()
display_guide()

""" 
A = 3.0
B = 4.0
C = 5.0
∠AC = 53.13°
∠BC = 36.87° 
"""
