import RPi.GPIO as GPIO

class test:
	count = 0
	SCLK = 11
	dataline = 13
	data = []
	CS = 15
	chipSelected = False
	

	def readData(self,channel):
		if(channel == 11 and self.chipSelected):
			#self.count += 1
			self.data.append(GPIO.input(self.dataline))
			print("Count: ",self.count, self.data)
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.SCLK, GPIO.IN)
		GPIO.setup(self.dataline, GPIO.IN)
		GPIO.setup(self.CS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.CS, GPIO.FALLING, callback = self.chipselect)
		GPIO.add_event_detect(self.SCLK, GPIO.RISING, callback = self.readData)
	
	def chipselect(self,channel):
		
		if(channel == 15):
			GPIO.remove_event_detect(self.CS)
			if(not self.chipSelected):
				print('chip selected')
				self.chipSelected = True
				self.count+=1
				print(str(self.count))
				GPIO.add_event_detect(self.CS, GPIO.RISING, callback = self.chipselect)
			else:
				self.chipSelected = False
				GPIO.add_event_detect(self.CS, GPIO.FALLING, callback = self.chipselect)
			
			
	def main(self):	
		while True:
			pass
if __name__ == "__main__":
	#tester = test()
	#tester.main()
	count = 0
	SCLK = 11
	dataline = 13
	data = []
	CS = 15
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(SCLK, GPIO.IN)
	GPIO.setup(dataline, GPIO.IN)
	while True:

		channel = GPIO.wait_for_edge(SCLK, GPIO.RISING)
		if not(channel == None):
			print(GPIO.input(dataline))
			