
#!/usr/bin/env python3

import sys

import Ice

Ice.loadSlice('drobots.ice')
import drobots


class DetectorControllerI(drobots.DetectorController):

    def alert(self, pos, detections, current=None ):

    	print("Chato¡¡¡ El detector {} has encontrado {} enemigos en la posicion {}. \n".format(self.id,detections,pos))

    	self.counter=1

    	while self.counter<=4






        pass


