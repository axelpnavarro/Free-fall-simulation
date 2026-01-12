#free fall and distance calculation 
print("Free fall calculator")
#Get time
t = float(input("Enter time in seconds:"))
#ask user for initial velocity
u = float(input('Enter initial velocity in m/s in case there is no initial velocity enter "0":'))
#ask initial height
h = float(input('Enter initial height in meters in case there is no initial height enter "0":'))
#define gravity value
def gravity():
    return 9.8
g = gravity()
#show user final distance and velocity without initial velocity
if u == 0 and h == 0:
    #calculate velocity and distance
    v = g * t
    d = 0.5* g * t ** 2
    print ("You travel in free fall a distance of", f"{d:,.2f}" , "m with a velocity of", v, "m/s")
elif u != 0 and h == 0:
    #calculate velocity and distance with initial velocity
    v= u + g * t
    d= u * t + 0.5 * g * t ** 2
    #show user final distance and velocity with initial velocity
    print ("You travel a distance of", f"{d:,.2f}" , "m with a velocity of", v, "m/s") 
elif u == 0 and h != 0:
    #calculate velocity and distance with initial height
    v = g * t
    d = h + 0.5* g * t ** 2
    #show user final distance and velocity with initial height
    print ("You travel in free fall a distance of", f"{d:,.2f}" , "m with a velocity of", v, "m/s")
elif u != 0 and h != 0:
    #calculate velocity and distance with initial height and initial velocity
    v= u + g * t
    d= u * t + 0.5 * g * t ** 2
    #show user final distance and velocity with initial height and initial velocity
    print ("You travel a distance of", f"{d:,.2f}" , "m with a velocity of", v, "m/s") 
