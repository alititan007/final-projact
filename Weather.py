
# The code is written by Ali Rahbar. 


city = input('Enter your city:')

def rafsanjan():
    print("Temperature => 30 °C")
    print("Wind Gusts => 20 km/h")
    print("wind => 19 km/h")
    print("Air Quality => good ")
    
    
def tehran():
    print("Temperature => 27 °C")
    print("Wind Gusts => 38 km/h")
    print("wind => 8 km/h")
    print("Air Quality => bad ")
    
   
    
def jiroft():
    print("Temperature => 33 °C")
    print("Wind Gusts => 30 km/h")
    print("wind => 28 km/h")
    print("Air Quality => bad ")
    

    
def karman():
    print("Temperature => 36 °C")
    print("Wind Gusts => 28 km/h")
    print("wind => 18 km/h")
    print("Air Quality => good ")
    
    
    
if  city == "rafsanjan" :
    rafsanjan()
    
elif city  == "tehran" :
    tehran()

elif  city == "jiroft" :
    jiroft()

elif  city == "karman" :
    karman()
    
else :
    print("Enter the city name correctly.")
    
    
    
