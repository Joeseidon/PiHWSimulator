#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include "raspi/hw.h"
#include "raspi/hw.c"

#ifdef __XENO__
#include <sys/mman.h>
#include <rtdk.h>
#define printf rt_printf
#endif

int main(int argc, char *argv[]){
  uint32_t speed = ?????;
  int destination =???;
  uint8_t data = 0x15;

  spi_init(speed);

  spi_start(destination);

  spi_write(data);

  uint8_t rtn = spi_read();

  if(spi_poll(1)){
    uint8_t rtn = spi_read();
    printf("%i",&rtn);
  }
  spi_stop();
}
