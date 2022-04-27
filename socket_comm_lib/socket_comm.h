//std
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <err.h>

//sockets
#include <arpa/inet.h>
//timestamps
#include <sys/time.h>

//COMPILE:
//use the comand make to compile using the makefile:
//make
//
//you can also compile it using gcc directly:
//gcc -c socket_comm.c -o socket_comm.o -Wall
//gcc socket_comm.o -o client -Wall

#define PORT 65431

#define UPLINK_MSG_DATA_SIZE 4
struct uplink_msg_data{
    char data[UPLINK_MSG_DATA_SIZE];
};

#define DOWNLINK_MSG_STR_SIZE 4096
struct downlink_msg_str{
    char data[DOWNLINK_MSG_STR_SIZE];//null terminated
};

struct downlink_msg_data{
    float data[31];
    int32_t bitfield;
};//128 bytes

int setup_client(char* ip, int port);
void send_uplink_msg_data(int sockfd, struct uplink_msg_data * msg);
void recv_downlink_msg_data(int sockfd, struct downlink_msg_data * msg);