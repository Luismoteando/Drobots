#!/usr/bin/env python3

import sys

import Ice

Ice.loadSlice('drobots.ice')
import drobots

class DetectorControllerI(drobots.DetectorController):

    def alert(self, pos, detections, current):
    	pass
        	