# by digiteng...10.2020, 02.2022, 03.2022
from Components.Converter.Converter import Converter
from Components.Element import cached

class RaedQuickSignal(Converter):

	def __init__(self, type):
		Converter.__init__(self, type)
		self.type = type

	@cached
	def getText(self):

		if self.type == "SNR":
			sr = self.source.snr or 0
			if sr:
				return "{}".format(sr * 100 // 65536)
			else:
				return "0"
		if self.type == "SNR_LABEL":
			sr = self.source.snr or 0
			if sr:
				return "SNR : {}%".format(sr * 100 // 65536)
			else:
				return "0%"
		if self.type == "AGC":
			ac = self.source.agc or 0
			if ac:
				return "{}".format(ac * 100 // 65536)
			else:
				return "0"
		elif self.type == "AGC_LABEL":
			ac = self.source.agc or 0
			if ac:
				return "AGC : {}%".format(ac * 100 // 65536)
			else:
				return "0%"

		elif self.type == "BER":
			br = self.source.ber
			if br:
				return str(br)
			else:
				return
		elif self.type == "Event":
			from time import time
			event = self.source.event
			if event:
				prgrs = int((int(time()) - event.getBeginTime()) * 100 // event.getDuration())
				return str(prgrs)
			else:
				return None
		elif self.type == "Event_Percent":
			from time import time
			event = self.source.event
			if event:
				prgrs = int((int(time()) - event.getBeginTime()) * 100 // event.getDuration())
				return "{}%".format(prgrs)
			else:
				return None		
	text = property(getText)

	@cached
	def getBool(self):
		if self.type == "BER":
			ber = self.source.ber
			if ber:
				return True
			else:
				return False
		if self.type == "LOCK":
			lock = self.source.lock
			if lock:
				return True
			else:
				return False

	boolean = property(getBool)
	