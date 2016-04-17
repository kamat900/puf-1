#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/mman.h>

#define PUF_BASE_ADDRESS 0xFF240000

#define CONTROL_REG 0x00000000
#define CTRL_REG_RST_MASK 0x80000000
#define CTRL_REG_ENA_MASK 0x00000001
#define CRTL_REG_DONE_MASK 0x00000002

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

void vdma_halt(puf_handle *handle) {
    puf_set(handle, OFFSET_VDMA_S2MM_CONTROL_REGISTER, VDMA_CONTROL_REGISTER_RESET);
    munmap((void *)handle->pufVirtualAddress, 65535);
    close(handle->pufHandler);
}

unsigned int puf_get(puf_handle *handle, int num) {
    return handle->pufVirtualAddress[num];
}

void puf_set(puf_handle *handle, int num, unsigned int val) {
    handle->pufVirtualAddress[num]=val;
}

int main() {
	FILE* fp;
    int j, i;
    puf_handle handle;

    fp = fopen("results.dat", "w");

    // Setup VDMA handle and memory-mapped ranges
    puf_setup(&handle, PUF_BASE_ADDRESS);


    printf("Finished\n");
	fclose(fp);
	puf_halt(&handle);
	return 0;
}
