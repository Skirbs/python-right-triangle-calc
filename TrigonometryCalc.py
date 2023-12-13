import os

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
    print(var_values)
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
    except:
        return False


def assign_variables():
    variable = input(f"({i+1}) Given Variable: ")
    while not variable_available(variable):
        variable = input(f"({i+1}) Given Variable: ")
    while True:
        try:
            value = int(input(f"({i+1}) Value: "))
            if int(variable) == 3 or int(variable) == 4:  # if angles was chosen
                var_values[3 if int(variable) == 4 else 4] = (
                    90 - value
                )  # Calculate for bot angles
            break
        except:
            continue
            pass
    var_values[int(variable)] = value
    display_guide()


def calculate_trigonometry():
    pass


display_guide()
given_variables = []
for i in range(2):
    assign_variables()
calculate_trigonometry()
