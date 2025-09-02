#!/usr/bin/python
# -*- coding: utf-8 -*-
# <widget source="session.CurrentService" render="AglareBoxImage" position="1103,642" size="550,155" alphatest="on" scale="1" zPosition="99" />
from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, loadPNG
import os

class RaedQuickSignalAglareBoxImage(Renderer):
    def __init__(self):
        Renderer.__init__(self)
        self.image_path = None
        
    GUI_WIDGET = ePixmap
    
    def changed(self, what):
        if not self.instance:
            return
            
        # Only proceed if we haven't set the image yet or if forced to update
        if what[0] != self.CHANGED_CLEAR:
            self.updateImage()
    
    def updateImage(self):
        if self.image_path is None:
            # Get hostname
            try:
                with open("/etc/hostname", "r") as f:
                    hostname = f.read().strip()
            except IOError:
                hostname = "default"
                
            # Construct image path
            self.image_path = f"/usr/share/enigma2/{hostname}.png"
            
            # Fallback to default.png if the specific image doesn't exist
            if not os.path.exists(self.image_path):
                self.image_path = "/usr/share/enigma2/default.png"
        
        # Load and display the image
        if os.path.exists(self.image_path):
            self.instance.setPixmap(loadPNG(self.image_path))
            self.instance.show()
        else:
            self.instance.hide()
    
    def onShow(self):
        self.updateImage()
    
    def onHide(self):
        self.instance.hide()