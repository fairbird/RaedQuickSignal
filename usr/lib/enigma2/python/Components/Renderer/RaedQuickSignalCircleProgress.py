# by digiteng...11.2020, 04.2022, 12.2024

from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, ePoint, eWidget, eLabel, eSize, loadPNG, gFont, eDVBVolumecontrol, eTimer
from skin import parseColor
import os
from Components.Converter.Poll import Poll

class RaedQuickSignalCircleProgress(Poll, Renderer):
	def __init__(self):
		Renderer.__init__(self)
		Poll.__init__(self)
		
		self.scale = 1
		self.modex = 0
		self.timer = eTimer()

		self.poll_interval = 1000
		self.poll_enabled = True
		
	GUI_WIDGET = eWidget

	def applySkin(self, desktop, screen):
		attribs = self.skinAttributes[:]
		for (attrib, value) in self.skinAttributes:
			if attrib == 'size':
				self.szX = int(value.split(',')[0])
				self.szY = int(value.split(',')[1])
			elif attrib == 'backgroundColor':
				self.backgroundColor = value
			elif attrib == 'mode':
				self.modex = value
			elif attrib == 'scale':
				self.scale = int(value)
			elif attrib == 'pixmapCircle':
				self.pixmapCirclex = value
			elif attrib == 'pixmapCircleBack':
				self.pixmapCircleBack = value
		self.skinAttributes = attribs
		
		self.prgrsPxmp.setPixmap(loadPNG("{}".format(self.pixmapCirclex)))
		self.prgrsPxmp.setScale(self.scale)
		self.prgrsPxmp.setBackgroundColor(parseColor(self.backgroundColor))
		self.prgrsPxmp.resize(eSize(self.szX, self.szY))
		self.prgrsPxmp.setZPosition(2)
		self.prgrsPxmp.setTransparent(1)
		self.prgrsPxmp.setAlphatest(2)

		self.prgrsPxmpBack.setPixmap(loadPNG("{}".format(self.pixmapCircleBack)))
		self.prgrsPxmpBack.setScale(self.scale)
		self.prgrsPxmpBack.setBackgroundColor(parseColor(self.backgroundColor))
		self.prgrsPxmpBack.resize(eSize(self.szX, self.szY))
		self.prgrsPxmpBack.setTransparent(1)
		self.prgrsPxmpBack.setAlphatest(2)
		self.prgrsPxmpBack.setZPosition(5)

		self.prgrsBack.setBackgroundColor(parseColor(self.backgroundColor))
		self.prgrsBack.resize(eSize(self.szX, self.szY))
		self.prgrsBack.move(ePoint(0, 0))
		self.prgrsBack.setTransparent(0)
		self.prgrsBack.setZPosition(0)
		
		self.prgrsText.setBackgroundColor(parseColor(self.backgroundColor))
		self.prgrsVal.setBackgroundColor(parseColor(self.backgroundColor))
		self.prgrsValR.setBackgroundColor(parseColor(self.backgroundColor))
		ret = Renderer.applySkin(self, desktop, screen)
		return ret

	def changed(self, what):

		val = None
		try:
			if self.modex == "event":
				val = self.source.text
			elif self.modex == "service":
				val = self.source.value 
				if val is not None :
					val = val / 100
			elif self.modex == "value":
				val = self.source.value 
			elif self.modex == "volume":
				val = eDVBVolumecontrol.getInstance().getVolume()
			elif self.modex == "snr-agc":
				# val = (int(self.source.value) * 100) // 65536
				val = self.source.text
				# open("/tmp/snragc.txt", "a+").write("{}\n".format(val))
			elif self.modex == "scan":
				if os.path.exists("/tmp/scan"):
					with open("/tmp/scan", "r") as f:
						val = f.readlines()[0]
			elif self.modex == "Processing":
				if os.path.exists("/tmp/processing-progress"):
					with open("/tmp/processing-progress", "r") as f:
						val = f.readlines()[0]

			# elif self.modex == "ipk_aslider":
				# iv = rv = 0
				# if os.path.exists("/tmp/ipkg-aslider"):
					# with open("/tmp/ipkg-aslider", "r") as f:
						# rv = f.readlines()[0]
					# val = val * int(rv)
			# elif self.modex == "ipk_slider":
				# all = rv = 0
				# if os.path.exists("/tmp/ipkg_all"):
					# with open("/tmp/ipkg_all", "r") as f:
						# all = f.readlines()[0]
				# if os.path.exists("/tmp/ipkg-aslider"):
					# with open("/tmp/ipkg-aslider", "r") as f:
						# rv = f.readlines()[0]
				# n = 100 / int(all)
				# val = n * int(rv)

		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
		if val is not None:
			self.timer.callback.append(self.getCircle(val))
			self.timer.start(100, True)

	def getCircle(self, val):
		try:
			val = int(val)
			x, y = 0, 0
			if val >= 0 and val <= 50:
				x = 0
				y = (float(50) / float(self.szY) ) * 100
				y = ((float(val) / float(self.szY)) * float(self.szY)) / y * 100
				y = int(-y)
				
				p = (self.szY / 2 - self.szY / 4) + (self.szY / 20)
				s = (self.szY / 4) + (self.szY / 10)
				f = (self.szY / 3)

				self.prgrsText.setText(str(val))
				self.prgrsText.setBackgroundColor(parseColor(self.backgroundColor))
				self.prgrsText.resize(eSize(self.szX, int(s)))
				self.prgrsText.move(ePoint(0, int(p)))
				self.prgrsText.setFont(gFont("Console", int(f)))
				self.prgrsText.setHAlign(eLabel.alignCenter)
				self.prgrsText.setTransparent(1)
				self.prgrsText.setZPosition(99)
				self.prgrsText.show()
				
				self.prgrsVal.setBackgroundColor(parseColor(self.backgroundColor))
				self.prgrsVal.resize(eSize(int(self.szX / 2), self.szY))
				self.prgrsVal.move(ePoint(x, y))
				self.prgrsVal.setTransparent(0)
				self.prgrsVal.setZPosition(3)
				self.prgrsVal.show()
				
				self.prgrsValR.setBackgroundColor(parseColor(self.backgroundColor))
				self.prgrsValR.resize(eSize(int(self.szX / 2), self.szY))
				self.prgrsValR.move(ePoint(int(self.szX / 2), 0))
				self.prgrsValR.setTransparent(0)
				self.prgrsValR.setZPosition(3)
				self.prgrsValR.show()
			elif val >= 51 and val <= 100:
				x = self.szX // 2
				y = (float(50) / float(self.szY) ) * 100
				y = (float(val) / float(self.szY) * float(self.szY)) / y * 100
				y = y - self.szY + self.szY / 10
				y = int(y)

				p = (self.szY / 2-self.szY / 4)+(self.szY / 20)
				s = (self.szY / 4)+(self.szY / 10)
				f = (self.szY / 3)

				self.prgrsText.setText(str(val))
				self.prgrsText.setBackgroundColor(parseColor(self.backgroundColor))
				self.prgrsText.resize(eSize(self.szX, int(s)))
				self.prgrsText.move(ePoint(0, int(p)))
				self.prgrsText.setFont(gFont("Console", int(f)))
				self.prgrsText.setHAlign(eLabel.alignCenter)
				self.prgrsText.setTransparent(1)
				self.prgrsText.setZPosition(99)
				self.prgrsText.show()
				
				self.prgrsValR.clearBackgroundColor()
				self.prgrsValR.hide()
				self.prgrsVal.clearBackgroundColor()
				self.prgrsVal.setBackgroundColor(parseColor(self.backgroundColor))
				self.prgrsVal.resize(eSize(x, self.szY))
				self.prgrsVal.move(ePoint(x, y))
				self.prgrsVal.setTransparent(0)
				self.prgrsVal.setZPosition(3)
				self.prgrsVal.show()
			else:
				return
		except Exception as err:
			from Tools.NachtWeatherUpdate import errorlog
			errorlog(err, __file__)

	def GUIcreate(self, parent):
		self.instance = eWidget(parent)
		self.prgrsVal = eLabel(self.instance)
		self.prgrsValR = eLabel(self.instance)
		self.prgrsText = eLabel(self.instance)
		self.prgrsBack = eLabel(self.instance)
		self.prgrsPxmp = ePixmap(self.instance)
		self.prgrsPxmpBack = ePixmap(self.instance)

	def GUIdelete(self):
		self.prgrsVal = None
		self.prgrsValR = None
		self.prgrsText = None
		self.prgrsBack = None
		self.prgrsPxmp = None
		self.prgrsPxmpBack = None
