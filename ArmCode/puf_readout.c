#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/mman.h>

#define PUF_BASE_ADDRESS 0xFF240000

#define CONTROL_REG 0x00000000
#define CTRL_REG_RST 0x80000000
#define CTRL_REG_ENA 0x00000001
#define CRTL_REG_DONE 0x00000002

#define READ_REG 0x00000001

#define WRITE_REG_MSW 0x00000001
#define WRITE_REG_2   0x00000002
#define WRITE_REG_1   0x00000003
#define WRITE_REG_LSW 0x00000004

typedef struct {
    unsigned int baseAddr;
    int pufHandler;
    unsigned int* pufVirtualAddress;
} puf_handle;

int puf_setup(puf_handle *handle, unsigned int baseAddr) {
    handle->baseAddr=baseAddr;
    handle->pufHandler = open("/dev/mem", O_RDWR | O_SYNC);
    handle->pufVirtualAddress = (unsigned int*)mmap(NULL, 65535, PROT_READ | PROT_WRITE, MAP_SHARED, handle->pufHandler, (off_t)handle->baseAddr);
    if(handle->pufVirtualAddress == MAP_FAILED) {
        perror("pufVirtualAddress mapping for absolute memory access failed.\n");
        return -1;
    }
    return 0;
}

void puf_halt(puf_handle *handle) {
    //puf_set(handle, OFFSET_VDMA_S2MM_CONTROL_REGISTER, VDMA_CONTROL_REGISTER_RESET);
    munmap((void *)handle->pufVirtualAddress, 65535);
    close(handle->pufHandler);
}

unsigned int puf_get(puf_handle *handle, int reg) {
    return handle->pufVirtualAddress[reg];
}

void puf_set(puf_handle *handle, int reg, unsigned int val) {
    handle->pufVirtualAddress[reg]=val;
}

int main() {
  FILE* fpi;
  FILE* fpo;
    char line[50];
    puf_handle handle;
    int index = 0;

    fpi = fopen("test_vectors.dat", "r");
    if(fpi == NULL) {
      perror("The test vector file could not be opened.\n");
      return -1;
    }
    fpo = fopen("results.dat", "w");
    if(fpo == NULL) {
      perror("The results file could net be opened.\n");
      return -1;
    }

    // Setup VDMA handle and memory-mapped ranges
    puf_setup(&handle, PUF_BASE_ADDRESS);

    while(fgets(line, sizeof line, fpi) != NULL) {
      char *p_line_val;
      unsigned int value[4];
      int i = 0;

      p_line_val = strtok(line, ",");
      while(p_line_val != NULL) {
        value[i] = atoi(p_line_val);
        p_line_val = strtok(NULL, ",");
        i++;
      }

      puf_set(&handle, CONTROL_REG, CTRL_REG_RST);
    puf_set(&handle, CONTROL_REG, 0);
    printf("The current test vector is %d\n", index);

    puf_set(&handle, WRITE_REG_MSW, value[0]);
    puf_set(&handle, WRITE_REG_2, value[1]);
    puf_set(&handle, WRITE_REG_1, value[2]);
    puf_set(&handle, WRITE_REG_LSW, value[3]);

    puf_set(&handle, CONTROL_REG, CTRL_REG_ENA);

    sleep(1);

    fprintf(fpo, "%8x\n", puf_get(&handle, READ_REG));

    index++;
    }

    printf("Finished\n");
  fclose(fpi);
  fclose(fpo);
  puf_halt(&handle);
  return 0;
}
