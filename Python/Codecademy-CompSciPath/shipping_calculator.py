#lbs
weight = 89
price = 0
drone_price = 0
ground_price = 0
prem_ground_price = 125

#Working out which shipping to use
#if weight

#Drone Shipping
if weight <= 2:
    drone_price = 4.50*weight
    print("Drone Shipping Cost: " + str(drone_price))
elif weight <= 6:
    drone_price = 9.00*weight
    print("Drone Shipping Cost: " + str(drone_price))
elif weight <= 10:
    drone_price = 12.00*weight
    print("Drone Shipping Cost: " + str(drone_price))
else:
    drone_price = 14.25*weight
    print("Drone Shipping Cost: " + str(drone_price))

#Ground Shipping
if weight <= 2:
    ground_price = (1.50*weight) + 20.00
    print("Regular Ground Shipping Cost: " + str(ground_price))
elif weight <= 6:
    ground_price = (3.00*weight) + 20.00
    print("Regular Ground Shipping Cost: " + str(ground_price))
elif weight <= 10:
    ground_price = (4.00*weight) + 20.00
    print("Regular Ground Shipping Cost: " + str(ground_price))
else:
    ground_price = (4.75*weight) + 20.00
    print("Regular Ground Shipping Cost: " + str(ground_price))

print("Premium Ground Shipping Cost: " + str(prem_ground_price))

print("")
print("Your weight is " + str(weight) + " lbs")

if drone_price < ground_price and drone_price < prem_ground_price:
  print("Your best shipping method is by drone")
  print("Total cost: " + str(drone_price))
elif ground_price < drone_price and ground_price < prem_ground_price:
  print("Your best shipping method is by regular ground shipping")
  print("Total cost: " + str(ground_price))
elif prem_ground_price < drone_price and prem_ground_price < ground_price:
  print("Your best shipping method is by regulgar ground shipping")
  print("Total cost: " + str(prem_ground_price))
