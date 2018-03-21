import maya.cmds as cmds
from functools import partial

class LightBoard():
    
    def __init__(self):
        
        self.lights = []
        self.lightControls = []
        self.lightNum = 0
        
        if (cmds.window("ahLightRig", exists=True)):
            cmds.deleteUI("ahLightRig")
            
        self.win = cmds.window("ahLightRig", title="Light Board")
        cmds.columnLayout()
        
        lights = cmds.ls(lights=True)
        
        for light in lights:
            self.createLightControl(light)
            
        cmds.showWindow(self.win)
        
    def updateColor(self, lightID, *args):
        newColor = cmds.colorSliderGrp(self.lightControls[lightID], query=True, rgb=True)
        cmds.setAttr(self.lights[lightID]+ '.color', newColor[0], newColor[1], newColor[2], type="double3")
        
    def createLightControl(self, lightShape):
        
        parents = cmds.listRelatives(lightShape, parent=True)
        lightName = parents[0]
        
        color = cmds.getAttr(lightShape + '.color')
        changeCommandFunc = partial(self.updateColor,
        self.lightNum)
        
        newSlider = cmds.colorSliderGrp(label=lightName,
        rgb=color[0], changeCommand=changeCommandFunc)
        
        self.lights.append(lightShape)
        self.lightControls.append(newSlider)
        
        self.lightNum +=1
        
LightBoard()