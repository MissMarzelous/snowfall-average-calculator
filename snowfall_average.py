# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Snowfall Average Calculator
# DATE WRITTEN: November 11, 2020
# UPDATED:      2026 — CRITICAL BUG FIX: maximum calculation was not inside
#                      a loop so it only checked one element and never found
#                      the real maximum. Fixed with a proper while loop.
#                      Added input validation, renamed to snake_case,
#                      fixed typos in comments.
#
# PURPOSE: Demonstrate how to define, create, and process an array/list
#          by storing snowfall amounts entered by the user, then calculating
#          and displaying the average, minimum, and maximum snowfall values.
#
# BEFORE (bug): The maximum was calculated outside a loop:
#               if snowfall[count] < maximum: maximum = snowfall[count]
#               This only checked ONE element and never updated correctly.
# AFTER  (fix): Uses a while loop identical in structure to the minimum loop.

# ============================================================
# Input Operations — ask how many snowfall amounts to enter
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("How many snowfall amounts will be entered into this list?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Validate that size is a positive integer
while True:
    try:
        size = int(input())
        if size <= 0:
            print("Please enter a number greater than zero.")
        else:
            break  # Valid input received
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# ============================================================
# Define the snowfall array/list — pre-filled with zeros
snowfall = [0] * size

# Initialize loop control variable / index and statistics variables
count = 0
maximum = 0.0
minimum = 0.0
snow_fall_avg = 0.0
sum_snowfall = 0.0

# ============================================================
# WHILE LOOP — populate / fill the snowfall list with user input
while count < size:

    # Input operations — collect each snowfall amount with validation
    while True:
        try:
            print(f"Enter snowfall amount #{count + 1} [positive value with decimals allowed]:")
            snowfall[count] = float(input())
            if snowfall[count] < 0:
                print("Snowfall cannot be negative. Please re-enter.")
            else:
                break  # Valid input received
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Update loop control variable / index
    count = count + 1
    # end while loop

# ============================================================
# Display the UNSORTED snowfall list
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                 UNSORTED SNOW FALL LIST")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" ")

# Reset array/list index back to 0
count = 0

# WHILE LOOP — display each snowfall value in the list
while count < size:
    print(snowfall[count])
    # Update loop control variable / index
    count = count + 1

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ============================================================
# WHILE LOOP — calculate the running sum of all snowfall values
count = 0

while count < size:
    # Keep a running sum of the snowfalls stored in the list
    sum_snowfall = sum_snowfall + snowfall[count]
    # Update loop control variable / index
    count = count + 1
    # end while loop

# Calculate the snowfall average
snow_fall_avg = sum_snowfall / len(snowfall)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("The snowfall average = " + format(snow_fall_avg, ".2f"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ============================================================
# Find MINIMUM snowfall value
count = 0

# 1st item is used as the starting minimum value
minimum = snowfall[0]

# WHILE LOOP — compare each element to find the smallest value
while count < size:
    if snowfall[count] < minimum:
        minimum = snowfall[count]   # Update minimum if smaller value found
    # Update loop control variable / index
    count = count + 1
    # end while loop

# ============================================================
# Find MAXIMUM snowfall value — FIXED: now uses a proper while loop
count = 0

# 1st item is used as the starting maximum value
maximum = snowfall[0]

# WHILE LOOP — compare each element to find the largest value
while count < size:
    if snowfall[count] > maximum:
        maximum = snowfall[count]   # Update maximum if larger value found
    # Update loop control variable / index
    count = count + 1
    # end while loop

# ============================================================
# Output snowfall statistics
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Minimum Snowfall Value = " + format(minimum, ".2f"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Maximum Snowfall Value = " + format(maximum, ".2f"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# END PROGRAM
