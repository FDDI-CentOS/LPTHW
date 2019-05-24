my_name =  'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes =  'Blue'
my_teeth = 'White'
my_hair =  'Brown'
#---------------------
#Additional Exercise Varbales
inch_to_centimeters = 2.54
lbs_to_kg = 0.453592

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's thats not too heavy.")
print( f"He's got {my_eyes} eyes and {my_hair} hair.")
print (f"His teeth are usually {my_teeth}")

#Additional Exercises
convert_weight = round(my_weight * lbs_to_kg)
convert_height = round(my_height * inch_to_centimeters)
print(f"Your weight is {my_weight} lbs or {convert_weight} kilograms")
print(f"Your height is {my_height} inches or {convert_height} centimeters")
