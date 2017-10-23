#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <pigpio.h>

#define CE0 5
#define CE1 6
#define MISO 13
#define MOSI 19
#define SCLK 12

#define serialGPIO
#define serialBaud
#define data_bits

/**
*Test Spi connection and gpiowaveread as a possible solution to spi read
*/
int main(int argc, char const *argv[]) {
  int fd = 0;

  char cmd1[] = {0, 0};
  char cmd2[] = {12, 0};
  char cmd3[] = {1, 128, 0};

  unsigned char inBuf[3];

  /*
    0001000000000000000000
  */

  if (gpioInitialise() < 0)
  {
     fprintf(stderr, "pigpio initialisation failed.\n");
     return 1;
  }

  uint32_t spiflag = 0x40000;

  fd = spiOpen(0, 320000, spiFlags);

  int status;

  status = spiWrite(fd, cmd3, 3);

  if(status == 3){
    //all bytes transfered
  }


  status = spiRead(fd, imBuf, 3);

  if(status == 3){
    //all bytes transfered
  }

  size_t bufsize = 32;
  char serialBuf[15][bufsize];
  //Serial read test
  status = gpioSerialReadOpen(serialGPIO, serialBaud, data_bits);
  printf("Status: %i\n", &status);

  for(int i = 0; i < 15; i++){
    status = gpioSerialRead(serialGPIO, serialBuf[i], bufsize);
  }
  status = gpioSerialReadClose(serialGPIO);

  printf("Serial Data: \n");
  for(int i = 0; i < 15; i++){
    for(int j = 0; j < 32; j++){
      printf("%c",serialBuf[i][j]);
    }
    printf("\n");
  }

}
