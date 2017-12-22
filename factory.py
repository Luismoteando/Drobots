

import sys

import Ice

Ice.loadSlice('drobots.ice')
import drobots
from controller import ControllerI
from controller import DetectorControllerI
from player import PlayerI


class RobotCotrollerI(self,bot,id)

	def make(self, bot, id)

		if (robot.ice_isA("::drobots::Attacker")):
			servidor=RobotControllerAdapter(bot)

		else if (robot.ice_isA("::drobots::Defender")):

			servidor=RobotControllerDefender(bot)

		else if (robot.ice_isA("::drobotos::Attacker") and robot.ice_isA("::drobots::Defender")):
			servidor=RobotControllerComplete(bot)


	def makeDetector(self, id)
		if bot==DeterctorController(id)
			servidor=DeterctorController(bot)



class RobotControllerDefender(drobots.RobotControllerDefender)
	def __init__
			self.robot=bot
			self.id=id


class RobotControllerAdapter(drobots.RobotControllerAdapter)
	def __init__
			self.robot=bot
			self.id=id


class RobotControllerComplete(drobots.RobotControllerComplete)
	def __init__
			self.robot=bot
			self.id=id


class DeterctorController()
	def __init__
			self.robot=bot
			self.id=id

	

