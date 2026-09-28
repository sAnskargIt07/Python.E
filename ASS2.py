EARTH_GRAVITY = 9.81
MOON_GRAVITY = 1.62

def weight(mass, gravity):
    return mass * gravity

mass = float(input("Enter mass in kg: "))

print(f"Weight on Earth = {weight(mass, EARTH_GRAVITY)} N")
print(f"Weight on Moon = {weight(mass, MOON_GRAVITY)} N")