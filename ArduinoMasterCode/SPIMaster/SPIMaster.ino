#include <SPI.h>

int CS = 10;
int MOSI = 11;
int SCLK = 13;

byte data = 0;

void setup(){
  SPI.begin()
  SPI.setBitOrder(MSBFIRST);
  pinMode(CS, OUTPUT);
  pinMode(MOSI, OUTPUT);
  pinMode(SCLK, OUTPUT);
  
  delay(500);
  
}

void loop(){
  for(data = 0; data<256; data++)
  {
    digitalWrite(CS, LOW);
    SPI.transfer(data);
    digitalWrite(CS, HIGH);
    delay(500);
  }
}
