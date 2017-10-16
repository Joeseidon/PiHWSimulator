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
#ifdef __XENO__
    struct sched_param param = { 99 };
    mlockall(MCL_CURRENT | MCL_FUTURE);
    pthread_setschedparam(pthread_self(), SCHED_FIFO, &param);
#endif

  if (!raspi_map_hw()) {
    perror("Could not map hardware registers");
    exit(1);
  }

#ifdef __XENO__
    pthread_set_mode_np(0, PTHREAD_WARNSW|PTHREAD_PRIMARY);
#endif

    spisl_init()

    spisl_synchronize()
}
