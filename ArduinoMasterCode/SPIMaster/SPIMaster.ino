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
  
  Serial.write("Any Key to Start");
  while(Serial.available()==0){
  }
  
}

void loop(){
  for(data = 0; data<256; data++)
  {
    digitalWrite(CS, LOW);
    //SPI.transfer(data);
    delay(1000);
    Serial.write("Low");
    digitalWrite(CS, HIGH);
    Serial.write("High");
    delay(1500);
    
    //digitalWrite(CS, LOW);
    //SPI.transfer(0x00);
    //delay(1000);
    //digitalWrite(CS, HIGH);
    //delay(500);
  }
}
