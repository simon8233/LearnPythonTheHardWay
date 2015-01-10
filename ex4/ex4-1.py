cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passebgers_per_car = passengers / cars_driven


print "There are", cars,"cars available."
print "There are only", drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."

print "we can transport",carpool_capacity,"people today."
print "we have",passengers, "to car pool today."
print "we need to put about", average_passebgers_per_car , "in each car."

# first question , I think it. it is not .

# because people is full , can not split half or less one
