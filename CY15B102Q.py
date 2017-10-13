'''
Raspberry Pi simulation of F-RAN Device (CY15B102Q).
Communication performed using SPI Protocol:
GPIO PINS USED:
    SCLK = PIN 11
    MISO = PIN 12
    MOSI = PIN 13
    CE0 = PIN 15

These pins were not dedicated SPI pins as indicate by the datasheet becasue
the Rasberry PI cannot be configured as a slave using the current libraries.
Thus it was created here.
'''

class CY15B102Q_SIM:
    def __init__(self):
        #Set SPI pin values
        self.SCLK = 11
        self.MISO = 12
        self.MOSI = 13
        self.CE = 15

        #Create List for data storage
            #data stored in tuples (adress,data)
            #to allow for quick look up given address from SPI Communication
        sim_RAM = []

        #Set up Pi to be an SPI slave device
        self.SPI_slave_init()

        #Wait for Master device to signal this device
        self.waitForMaster()

    def SPI_slave_init(self):


    def waitForMaster(self):
        ##Wait for CS pulled low

        ##Establish SPI Mode based on first SCLK read

        ##WREN opcode sent after CS pulled low
            ##If so wait for WRITE opcode and perform task

            ##Else wait for next opcode
                ##If opecode == READ opcode
                    #data is sent out in 8bit chuncks while sckl is issued and CS is low



    def readCMDIssued(self,address):

    def writeCMDIssued(self,address,data):
