#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include "hw.h"



int int main(int argc, char const *argv[]) {
  if(!raspi_map_hw()){
    perror("Could not map hardware registers.");
    exit(1);
  }

  printf("Synchronizing SPI");

  spisl_synchronize();

  if(spisl_poll(1) == 1){
    uint8_t[] rtn = spisl_read();
    printf("Data available.");
    printf("\tData: %i", &rtn[0]);
  }
}
