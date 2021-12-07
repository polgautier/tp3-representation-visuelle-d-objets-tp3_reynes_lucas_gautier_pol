# -*- coding: utf-8 -*-

from Configuration import Configuration
from Section import Section
from Wall import Wall
from Door import Door
from Window import Window
from House import House
from Opening import Opening
import copy


def Q1a():
	return Configuration()
	
def Q1b_f():
	return Configuration({'screenPosition': -5, 'xAxisColor': [1, 1, 0]}). \
		setParameter('xAxisColor', [1, 1, 0]). \
		setParameter('yAxisColor', [0,1,1]). \
		display()
		
def Q2b():
	# Ecriture en utilisant le chaînage
	return Configuration().add(
			Section({'position': [1, 1, 0], 'width':7, 'height':2.6})
			) 

def Q2c():
	section = Section({'position': [1, 1, 0], 'width':7, 'height':2.6, 'edges': True })
	Configuration().add(section).display()

		

def Q3a():
	return Configuration().add(
		Wall({'position': [1, 1, 0], 'width':7, 'height':2.6, "orientation": 20})
	)   

def Q4a():
	# Ecriture en utilisant des variables : A compléter
	wall1 = Wall({'position': [0, 0, 0], 'width': 7, 'height': 2.6, "orientation": 0})
	wall2 = Wall({'position': [7, 0, 0], 'width': 7, 'height': 2.6, "orientation": 90})
	wall3 = Wall({'position': [0, 0, 0], 'width': 7, 'height': 2.6, "orientation": 90})
	wall4 = Wall({'position': [-wall1.parameters["thickness"], 7, 0], 'width': 7+wall1.parameters["thickness"], 'height': 2.6, "orientation": 0})
	house = House({'position': [0, 0, 0], 'orientation': 0})
	house.add(wall1).add(wall3).add(wall4).add(wall2)
	return Configuration().add(house)   
	
def Q5a():  
	# Ecriture avec mélange de variable et de chaînage    
	opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
	opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})    
	return Configuration().add(opening1).add(opening2)
	
def Q5b():  
	# Ecriture avec mélange de variable et de chaînage   
	section = Section({'width':7, 'height':2.6})
	opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
	opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
	opening3 = Opening({'position': [4, 0, 1.7], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
	
	print(section.canCreateOpening(opening1))
	print(section.canCreateOpening(opening2))    
	print(section.canCreateOpening(opening3))
	return Configuration()    
	
def Q5c1():      
	section = Section({'width':7, 'height':2.6})
	opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
	sections = section.createOpening(opening1)
	configuration = Configuration()
	for x in sections:
		configuration.add(x)    
	return configuration     
	
def Q5c2():      
	section = Section({'width':7, 'height':2.6})
	opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
	sections = section.createNewSections(opening2)
	configuration = Configuration()
	for section in sections:
		configuration.add(section)    
	return configuration    

def Q5d():      
	wall1 = Wall({'width':7, 'height':2.6,}) 
	opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
	section = wall1.findSection(opening1)

def main():
	    house=House()
    window = Window({'position': [4, 0.14, 1.2]})
    door = Door({'position': [2, 0.15,0]})
    wall = Wall({'width':7, 'height':2.6}).add(window).add(door)
    house.add(wall)
    house.objects.append(Wall({'position': [0, 4.2, 0], 'width':4, 'height':2.6, 'edges': True, 'orientation': -90}))
    house.objects.append(Wall({'position': [0, 4.2, 0], 'width':7, 'height':2.6, 'edges': True, 'orientation': 0}))
    house.objects.append(Wall({'position': [7 , 0.2, 0], 'width':4, 'height':2.6, 'edges': True, 'orientation': 90}))
    Configuration().add(house).display()


		 
# Calls the main function
if __name__ == "__main__":
	main()    
