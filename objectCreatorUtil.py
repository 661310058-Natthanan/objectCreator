import maya.cmds as cmds

def createObject(obj_type, obj_name):

	if obj_type == 'cube':
		return cmds.polyCube(name=obj_name)

	elif obj_type == 'sphere':
		return cmds.polySphere(name=obj_name)

	elif obj_type == 'cone':
		return cmds.polyCone(name=obj_name)

	elif obj_type == 'torus':
		return cmds.polyTorus(name=obj_name)