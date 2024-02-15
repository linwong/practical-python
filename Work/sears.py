# sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)

# bill_thickness = 0.11 * .001 # .11mm
# sears_height = 442
# num_bills = 1
# days = 1

# while num_bills * bill_thickness < sears_height:
#   print(days, num_bills, num_bills * bill_thickness)
#   days += 1
#   num_bills *= 2

# print('number of days:', days)
# print('number of bills:', num_bills)
# print('final height:', num_bills * bill_thickness)
