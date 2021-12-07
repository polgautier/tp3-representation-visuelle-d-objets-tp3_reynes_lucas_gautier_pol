# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017
@author: lfoul
"""
import OpenGL.GL as gl

class Section:
	# Constructor
	def __init__(self, parameters = {}) :  
		# Parameters
		# position: position of the wall 
		# width: width of the wall - mandatory
		# height: height of the wall - mandatory
		# thickness: thickness of the wall
		# color: color of the wall        

		# Sets the parameters
		self.parameters = parameters
		
		# Sets the default parameters
		if 'position' not in self.parameters:
			self.parameters['position'] = [0, 0, 0]        
		if 'width' not in self.parameters:
			raise Exception('Parameter "width" required.')   
		if 'height' not in self.parameters:
			raise Exception('Parameter "height" required.')   
		if 'orientation' not in self.parameters:
			self.parameters['orientation'] = 0              
		if 'thickness' not in self.parameters:
			self.parameters['thickness'] = 0.2    
		if 'color' not in self.parameters:
			self.parameters['color'] = [0.5, 0.5, 0.5]       
		if 'edges' not in self.parameters:
			self.parameters['edges'] = False             
			
		# Objects list
		self.objects = []

		# Generates the wall from parameters
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
		self.vertices = [ 
			# devant
			[0, 0, 0],
			[0, 0, self.parameters['height']], 
			[self.parameters['width'], 0, self.parameters['height']],
			[self.parameters['width'], 0, 0],
			# derriere
			[0, self.parameters['thickness'], 0], 
			[self.parameters['width'], self.parameters['thickness'], 0], 
			[self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
			[0, self.parameters['thickness'], self.parameters['height']]	 
		]
		self.faces = [ # sens anti-horaire
			[0, 3, 2, 1], # devant
			[4, 7, 6, 5], # derriere
			[0, 1, 7, 4], # gauche
			[2, 3, 5, 6], # droite
			[1, 2, 6, 7], # haut
			[3, 0, 4, 5]  # bas
		]    

	# Checks if the opening can be created for the object x
	def canCreateOpening(self, x):
        if self.parameters['position'][0]<=x.parameters['position'][0] and \
           self.parameters['position'][2]<=x.parameters['position'][2] and \
           self.parameters['position'][0]+self.parameters['width']>=x.parameters['position'][0]+x.parameters['width'] and \
           self.parameters['position'][2]+self.parameters['height']>=x.parameters['position'][2]+x.parameters['height']:
            return True
        else: 
            return False
    
		
	# Creates the new sections for the object x
	def createNewSections(self, x):
	    def  createNewSections(self, x):
        #test possibilité d'ouvertures
        if self.canCreateOpening(x):

            #création liste de sortie
            L_section=[]

            #création des variables
            x1,y,z=self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2]
            w=self.parameters['width']
            h=self.parameters['height']
            xs,ys,zs=x.parameters['position'][0],x.parameters['position'][1],x.parameters['position'][2]
            ws=x.parameters['width']
            hs=x.parameters['height']

            #test de création de la section droite
            if  xs-x1>0:
                L_section.append(Section({'position':[x1,y,z], \
                                      'width': xs-x1, \
                                      'height': h}))

            #test de création de la section gauche
            if  (x1+w)-(xs+ws)>0:
                position=[xs+ws,y,0]
                L_section.append(Section({'position':position, \
                                      'width': (x1+w)-(xs+ws), \
                                      'height': h}))

            #test de création de la section basse
            if  (zs)-(z)>0:
                position=[xs,y,0]
                L_section.append(Section({'position':position, \
                                      'width': ws, \
                                      'height': (zs)-(z)}))

            #test de création de la section haute
            if  (z+h)-(zs+hs)>0:
                position=[xs,y,(zs)-(z)+hs]
                L_section.append(Section({'position':position, \
                                      'width': ws, \
                                      'height':  (z+h)-(zs+hs)}))

        return L_section

		          
		
	# Draws the edges
	def drawEdges(self):
		# A compléter en remplaçant pass par votre code
		gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE) 
		for face in self.faces:
			gl.glBegin(gl.GL_QUADS) 
			gl.glColor3fv([0]*3)
			for pointInd in face: 
				gl.glVertex3fv(self.vertices[pointInd])
			gl.glEnd()           
					
	# Draws the faces
	def draw(self):
		gl.glPushMatrix()
		#gl.glTranslatef(...self.parameters['position']) # pas de spread syntax ;(
		gl.glTranslatef(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2])
		gl.glRotatef(self.parameters["orientation"], 0,0,1)
		# A compléter en remplaçant pass par votre code
		if self.parameters['edges'] : self.drawEdges()
		
		gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
		for face in self.faces:
			gl.glBegin(gl.GL_QUADS) 
			gl.glColor3fv(self.parameters['color'])
			for pointInd in face: 
				gl.glVertex3fv(self.vertices[pointInd])
			gl.glEnd()
		
		gl.glPopMatrix()
