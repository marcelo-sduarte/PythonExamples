import math

def main():

    #radius = 6.83
    #height = 7.62	


    # call function volume
    volume = cylinder_volume(radius, height)
    # call function surface_area
    area = surface_area (radius, height)
    
    storage_efficiency = volume / area
    print(f"Store Efficiency is: {storage_efficiency:.2}")


def cylinder_volume(radius, height):
    #Compute and return the volume of a right circular cylinder#
    #volume = π radius2 height#
    volume = math.pi * radius**2* height
    return volume

def surface_area (radius,height):
    # Compute surface area is"
    #surface_area = 2π radius (radius + height)#
    surface_area = 2*math.pi*radius*(radius + height)
    return surface_area

main()





