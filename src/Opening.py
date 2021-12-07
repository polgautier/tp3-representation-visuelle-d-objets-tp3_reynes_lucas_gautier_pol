# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017
@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
	# Constructor
	def __init__(self, parameters = {}) :  
		# Parameters
		# position: mandatory
		# width: mandatory
		# height: mandatory
		# thickness: mandatory
		# color: mandatory        

		# Sets the parameters
		self.parameters = parameters

		# Sets the default parameters 
		if 'position' not in self.parameters:
			raise Exception('Parameter "position" required.')       
		if 'width' not in self.parameters:
			raise Exception('Parameter "width" required.')
		if 'height' not in self.parameters:
			raise Exception('Parameter "height" required.')
		if 'thickness' not in self.parameters:
			raise Exception('Parameter "thickness" required.')    
		if 'color' not in self.parameters:
			raise Exception('Parameter "color" required.')  
		if 'orientation' not in self.parameters:
            		self.parameters['orientation'] = 0 

			
		# Generates the opening from parameters
		self.generate()  

		# Getter
		def getParameter(self, parameterKey):
			return self.parameters[parameterKey]
	
		# Setter
		def setParameter(self, parameterKey, parameterValue):
		self.parameters[parameterKey] = parameterValue
		return self        

		# Defines the vertices and faces        
		def generate(self):
		x,y,z=self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2]
       		w=self.parameters['width']
        	h=self.parameters['height']
        	t=self.parameters['thickness']
        	angle_deg=self.parameters['orientation']
        	a=angle_deg*pi/180
        
        	self.vertices = [ 
                	[x,y,z],
                	[x,y,z+h],
        	        [x+w*cos(a),y+w*sin(a),z+h],
	                [x+w*cos(a),y+w*sin(a),z],
                	[x-t*sin(a),y+t*cos(a),z],
        	        [x-t*sin(a),y+t*cos(a),z+h],
 	                [x+w*cos(a)-t*sin(a),y+w*sin(a)+t*cos(a),z+h],
                	[x+w*cos(a)-t*sin(a),y+w*sin(a)+t*cos(a),z]
                ]
        	self.faces = [
                	[0,1,4,5],
               		[2,3,6,7],
                	[0,4,3,7],
                	[1,5,2,6]
                ]   

	# Draws the faces                
	def draw(self):        
        for elem in self.objects:
            elem.draw()

