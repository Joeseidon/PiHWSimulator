'''
Raspberry Pi simulation of F-RAN Device (CY15B102Q).
Communication performed using SPI Protocol:
GPIO PINS USED:
    SCLK = PIN 11
    MISO = PIN 12
    MOSI = PIN 13
    CS = PIN 15

These pins were not dedicated SPI pins as indicate by the datasheet becasue
the Rasberry PI cannot be configured as a slave using the current libraries.
Thus it was created here.
'''

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")

class CY15B102Q_SIM:
    data = 0x0
    opcodes = {'WREN':0x6,'READ': 0x3, 'WRITE': 0x2}

    #used to obtain opcode from input data
    OPCODEMASK = 0xff00000000
    #used to obtain address from input data
    ADDRESSMASK = 0x3ffff00
    #used to extract data from input
    DATAMASK = 0xff


    def __init__(self):
        #Set SPI pin values
        self.SCLK = 11
        self.MISO = 3
        self.MOSI = 13
        self.CS = 15

        self.chipSelect = False
        self.analyze = False

        #Create List for data storage
            #data stored in a dictionary to mimic address value lookup
        sim_RAM = {}

        #Set up Pi to be an SPI slave device
        self.SPI_slave_init()

        #Wait for Master device to signal this device
        while True:
            #main loop
            print("Waiting")
	    pass

    def sortDictionary(self,dic):
        #sorts the data in the provided dictionary by key value (sim_memory address)
        keylist = sorted(self.dic.iterkeys())
        return keylist

    def setCS(self, channel):
        if(channel == self.CS):
            self.chipSelect = False

    def SPI_slave_init(self):
        #Set up GPIO Pins
        GPIO.setmode(GPIO.BOARD)

        #Set up chip select with pull up as master should pull CS low during interaction
        GPIO.setup(self.CS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #Add event to this pin so that when it is pull low the opcode is considered
        GPIO.add_event_detect(self.CS, GPIO.FALLING, callback=self.chipSelected)


        #Set up MOSI (SI) as input
        GPIO.setup(self.MOSI, GPIO.IN)

        #Set up MISO (SO) as output
        GPIO.setup(self.MISO, GPIO.OUT)

        #Set up SCLK as input
        GPIO.setup(self.SCLK, GPIO.IN)
        #Create event for clk signal. This will indicate when to read data.
        GPIO.add_event_detect(self.SCLK, GPIO.RISING, callback=self.readMasterData)

    def chipSelected(self, channel):
        if(channel == self.CS):
            #Used by other programs to order operations
            self.chipSelect = True

            #Must remove previous edge detection
            GPIO.remove_event_detect(self.CS)

            #This interrupt will indicate when the master deselects this device
            GPIO.add_event_detect(self.CS, GPIO.RISING, callback=self.setCS)

            #active low
            while self.chipSelect:
                #While chip select is held interupts will be triggered to start data read

                #After all data has been read trigger analyze
                if(self.analyze):
                    self.analyzeData()
                pass

            #After CS is released data register will be cleared
            self.data = 0x0
            #After CS is released all flags should be reset
            self.analyze = False

    def readMasterData(self, channel):
        if(channel == self.SCLK):
            if(self.chipSelect):
                self.data << GPIO.input(self.MOSI)
            if(bits == 23):
                self.analyze == True
                #Remove SCLK event so this input can be used for read/write events
                GPIO.remove_event_detect(self.SCLK)

    def analyzeData(self):
        #inspect first 8 bits for opcode

        ##WREN opcode sent after CS pulled low
            ##If so wait for WRITE opcode and perform task

            ##Else wait for next opcode
                ##If opecode == READ opcode
                    #data is sent out in 8bit chuncks while sckl is issued and CS is low
                    if self.data & OPCODEMASK == opcodes['READ']:
                        start_address = ADDRESSMASK & self.data
                        self.sendData(start_address)

    def sendData(self,address):
        #Create event for clk signal. This will indicate when to write data.
        GPIO.add_event_detect(self.SCLK, GPIO.RISING)
        #sorted list of keys
        keylist = self.sortDictionary(sim_RAM)
        while self.chipSelect:
            bdata=bin(sim_Ram[address])
            #If there is data left to send and clk is on the rising edge
            while bdata:
                #if clk on rising edge send a bit of data
                if GPIO.event_detected(self.SCLK):
                    if(0x01 & bdata):
                        GPIO.ouput(self.MISO, GPIO.HIGH)
                    else:
                        GPIO.output(self.MISO, GPIO.LOW)
                    bdata = bdata >> 1

            #increment address becasue HW should send data until master releases CS
            newIndex = keylist.index(address)+1
            if(newIndex >= len(keylist)):
                newIndex = 0
            address = keylist[newIndex]

        #Action is no longer required on rising clock cycles
        GPIO.remove_event_detect(self.SCLK)
if __name__ == "__main__":
	controler = CY15B102Q_SIM()
