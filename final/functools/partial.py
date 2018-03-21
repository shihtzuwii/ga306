import maya.cmds as cmds

def createLightRig():
    
    offsetAmount = 20
    lightRotation = 30
    
    newLight = cmds.spotLight(rgb=(1, 1, 1), name="KeyLight")
    lightTransform = cmds.listRelatives(newLight, parent=True)
    keyLight = lightTransform[0]
    
    newLight = cmds.spotLight(rgb=(0.8, 0.8, 0.8), name="FillLight")
    lightTransform = cmds.listRelatives(newLight, parent=True)
    fillLight = lightTransform[0]
    
    newLight = cmds.directionalLight(rgb=(0.2, 0.2, 0.2), name="BackLight")
    lightTransform = cmds.listRelatives(newLight, parent=True)
    backLight = lightTransform[0]
    
    cmds.move(0, 0, offsetAmount, keyLight)
    cmds.move(0, 0, 0, keyLight + ".rotatePivot")
    cmds.rotate(-lightRotation, lightRotation, 0, keyLight)
    
    cmds.move(0, 0, offsetAmount, fillLight)
    cmds.move(0, 0, 0, fillLight + ".rotatePivot")
    cmds.rotate(-lightRotation, -lightRotation, 0, fillLight)
    
    cmds.move(0, 0, offsetAmount, backLight)
    cmds.move(0, 0, 0, backLight + ".rotatePivot")
    cmds.rotate(180 + lightRotation, 0, 0, backLight)
    
    rigNode = cmds.group(empty=True, name="LightRig")
    
    cmds.parent(keyLight, rigNode)
    cmds.parent(fillLight, rigNode)
    cmds.parent(backLight, rigNode)
    
    cmds.select(rigNode, replace=True)
    
createLightRig()