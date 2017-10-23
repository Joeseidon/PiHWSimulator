#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <pigpio.h>

#define SPI_CS
#define MOSI
#define MISO
#define BITS 8 //Bits per read

#define BUFFER 250

#define REPEAT_MICROS 40

rawSPI_t rawSPI =
{
   .clk     =  5, // GPIO for SPI clock.
   .mosi    = 12, // GPIO for SPI MOSI.
   .ss_pol  =  1, // Slave select resting level.
   .ss_us   =  1, // Wait 1 micro after asserting slave select.
   .clk_pol =  0, // Clock resting level.
   .clk_pha =  0, // 0 sample on first edge, 1 sample on second edge.
   .clk_us  =  1, // 2 clocks needed per bit so 500 kbps.
};

/*
bsc_control:

 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
 a  a  a  a  a  a  a  -  - IT HC TF IR RE TE BK EC ES PL PH I2 SP EN
*/

/*
SPI GPIOS:
CE0   18
CE1   17
CE2   16
MISO  19
MOSI  20
SCLK  21
*/

/*
CONSIDER : using gpioSerialReadOpen() from pigpio to read incoming data
      data read : using gpioSerialRead
      **caller of this function must read data from cyclic buffer in a timely fashion

*/
int main(int argc, char const *argv[]) {
  //No address since SPI is being used
  bsc_xfer_t xfer;
  xfer.control = (0x00<<16) | 0x303;
  char rtnBuf[BSC_FIFO_SIZE];
  //send
  char rtn[BSC_FIFO_SIZE];
  memcpy(xfer.txBuf, "AB", 2);
  xfer.txCnt = 2;
  //copy recieve
  memcpy(rtn,xfer.rxBuf, 6);

  //Print current RX buffer
  int status;
  status = bscXfer(&xfer);

  if(status >= 0)
  {
    //copy recieve
    memcpy(rtn,xfer.rxBuf, 6);

    //print RX buffer after send
    for(int i = 0; i < rtn.lenth(); i++){
      print("%c",rtn[i]);
    }
  }

  return 0;
}
