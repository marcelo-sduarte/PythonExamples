import math

def main():
#2. Open a text file named dimensions.txt in append mode.#
#with open("sizes.txt", "at") as sizes_file:
    steelnames = ["# Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    steelradius = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
    steelheight=[10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11]
    steelcosts = [0.28,0.43,0.45,0.61,0.86,0.83,0.22,0.26,1.53,0.34,0.38,0.42]
     
    for i in range(len(steelnames)):
        volume = cylinder_volume(steelradius[i], steelheight[i])
        area = cylinder_surface_area(steelradius[i], steelheight[i])
        sf = storage_efficiency(volume, area)
        cost_eff = cost_efficiency(volume, steelcosts[i])
        print(f"Name: {steelnames[i]} Storage Efficiency: {sf:.1f} Cost Efficiency: ${cost_eff:.2f}" )
        print()

def cylinder_surface_area(radius, height):
    # Compute surface area is"
    #surface_area = 2π radius (radius + height)#
    area = 2 * math.pi * radius * (radius + height)
    return area

def cylinder_volume(radius, height):
    #Compute and return the volume of a right circular cylinder#
    #volume = π radius2 height#
    volume = math.pi * radius**2 * height
    return volume

def storage_efficiency (volume, surf_area):
    #Compute and return the store efficiency of a stell#
    #store efficiency = volume / surface area#
    sf = volume / surf_area
    return sf

def cost_efficiency(volume, cost):
    #Compute abd returns the volume of steel divided by cost#
    cost_eff = volume / cost
    return cost_eff

# 1. Call main
main()