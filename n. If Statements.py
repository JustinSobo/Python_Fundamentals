Real World Example:

I wake up
If I'm hungry
    I eat breakfast

I leave my house
if it's cloudy
    I bring an umbrella
otherwise
    I bring sunglasses

I'm at a restaurant
if I want meate
    I order a steak
otherwise if I want pasta
    I order spaghetti & meatballs
otherwise
    I order a salad.
#########################################
#########################################
#########################################
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You are either not male or not tall or both.")

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are a short male.")
else:
    print("You are not a male and not tall.")
