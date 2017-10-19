#include <SPI.h>

int CS = 10;
int DOUT = 11;
int SCLK = 13;

byte dataMarker = 0x81;
byte rtnval = 0x00;

void setup(){
  SPI.begin();
  SPI.setBitOrder(MSBFIRST);
  pinMode(CS, OUTPUT);
  
  Serial.begin(9600);
  delay(500);
}

void loop(){
  while(rtnval != dataMarker)
  {
    digitalWrite(CS, LOW);
    rtnval = SPI.transfer(dataMarker);
    digitalWrite(CS, HIGH);
    delay(500);
  }
  Serial.println("Synchronized");
  digitalWrite(CS,LOW);
  SPI.transfer(0xff);
  digitalWrite(CS, HIGH);
  while (1 == 1){}
}
