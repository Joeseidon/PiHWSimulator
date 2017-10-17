#include <SPI.h>

int CS = 10;
int DOUT = 11;
int SCLK = 13;

byte data = 0;

void setup(){
  SPI.begin();
  SPI.setBitOrder(MSBFIRST);
  pinMode(CS, OUTPUT);
  pinMode(DOUT, OUTPUT);
  pinMode(SCLK, OUTPUT);
  
  Serial.begin(9600);
  delay(500);
  
}

void loop(){
  for(data = 0; data<256; data++)
  {
    digitalWrite(CS, LOW);
    SPI.transfer(data);
    Serial.println(data);
    digitalWrite(CS, HIGH);
    digitalWrite(CS, LOW);
    SPI.transfer(0x00);
    digitalWrite(CS, HIGH);
    delay(500);
  }
}
