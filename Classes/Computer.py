class Computer(): # define classe name
  
  # define arguments 
    def __init__(self):
	    self.memory_ram = 0
	    self.video = ""
	    self.processor = 0

#Call classe and assign value
computer1 = Computer()
computer1.memory_ram = 300


computer2 = Computer()
computer2.video= "GeForce"

#Display on screen
print(f"Computador 1: {computer1.memory_ram}")
print(f"Computador 2: {computer2.video}")

