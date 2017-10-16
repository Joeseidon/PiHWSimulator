#include <SPI.h>

//Opcode defintions
volatile byte WRENop = 0x06;
volatile byte READop = 0x03;
volatile byte WRITEop = 0x02;

volatile byte TestData = 0x25;

volatile uint32_t TestAddress = 0x14543;
/*
//SPI pins
int SS = 10;
int MOSI = 11;
int MISO = 12;
int SCLK = 13;*/


void setup (void)
{

  digitalWrite(SS, HIGH);  // ensure SS stays high for now
/*
  // Put SCK, MOSI, SS pins into output mode
  // also put SCK, MOSI into LOW state, and SS into HIGH state.
  pinMode(MOSI, OUTPUT);
  digitalWrite(MOSI, LOW);
  pinMode(MISO, INPUT);
  digitalWrite(MISO, LOW);
  pinMode(SCLK, OUTPUT);
  digitalWrite(SCLK, LOW);*/

  // Then put SPI hardware into Master mode and turn SPI on
  SPI.begin();

  SPI.setDataMode(SPI_MODE1);

  SPI.setBitOrder(MSBFIRST);

  // Slow down the master a bit
  SPI.setClockDivider(SPI_CLOCK_DIV8);
  
  Serial.begin(9600);
  
  Serial.write("Enter 1 to start");
  
  while(Serial.available()==0){}
    

}  // end of setup

void testWrite(void){

  // enable Slave Select
  digitalWrite(SS, LOW);    // SS is pin 10

  SPI.transfer(WRENop);

  SPI.transfer(WRITEop);

  SPI.transfer(TestData);

  digitalWrite(SS,HIGH)
}

void testRead(void){
  digitalWrite(SS, LOW);

  SPI.transfer(READop);
}

void loop (void)
{

  char c;

  // enable Slave Select
  digitalWrite(SS, LOW);    // SS is pin 10

  // send test string
  for (const char * p = "Hello, world!\n" ; c = *p; p++)
    SPI.transfer (c);

  // disable Slave Select
  digitalWrite(SS, HIGH);

  delay (1000);  // 1 seconds delay
}  // end of loop
