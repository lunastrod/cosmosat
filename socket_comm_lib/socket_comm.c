#include "socket_comm.h"

//connects client to server
//returns: int sockfd
int setup_client(char* ip, int port) {
    // create socket
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        err(1,"Socket creation failed\n");
    }
    else {
        printf("Socket successfully created\n" );
    }
    // assign ip and port
    struct sockaddr_in servaddr;
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr(ip);
    servaddr.sin_port = htons(port);

    // connect client to server
    while((connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr))) < 0) {
        warn("Connection with the server failed, retrying");
        sleep(1);
    }
    printf("Client conected to server\n");
    return sockfd;
}

void send_uplink_msg_data(int sockfd, struct uplink_msg_data * msg){
    //TODO: error handling
    int ret_send=send(sockfd,msg,sizeof(struct uplink_msg_data),0);
}

/*
converts a downlink_msg_str into a compressed downlink_msg_data
downlink_msg_str example:
0.000000 1.000000 2.000000 3.000000 4.000000 5.000000 6.000000 7.000000 8.000000 9.000000 10.000000 11.000000 12.000000 13.000000 14.000000 15.000000 16.000000 17.000000 18.000000 19.000000 20.000000 21.000000 22.000000 23.000000 24.000000 25.000000 26.000000 27.000000 28.000000 29.000000 30.000000 00010000101111110000100011111101
*/
void convert_downlink_str_to_data(struct downlink_msg_str * str, struct downlink_msg_data * msg){
    char * parse;
    char * ptr;
    for(int i=0; i<31; i++){//parse floats from string
        msg->data[i]=strtod(parse,&ptr);
        parse=ptr;
    }
    parse++;//ignore the next char (space)
    int32_t bitfield;
    for(int i=0; i<32; i++){//parse bitfield from string
        if(parse[i]=='1'){
            bitfield=bitfield<<1|1;
        }
        else{
            bitfield=bitfield<<1|0;
        }
    }
    msg->bitfield=bitfield;
}

void recv_downlink_msg_data(int sockfd, struct downlink_msg_data * msg){
    struct downlink_msg_str str;

    //TODO: error handling
    int ret_recv=recv(sockfd,msg,sizeof(struct downlink_msg_data),0);

    convert_downlink_str_to_data(&str,msg);
}

//use example
int main(int argc, char const* argv[]){
    int sockfd=setup_client("127.0.0.1",PORT);
    while(1){
        struct uplink_msg_data up_msg;//msg from ground
        up_msg.data[0]=0xCA;
        up_msg.data[1]=0xFE;
        up_msg.data[2]=0xBA;
        up_msg.data[3]=0xCA;
        send_uplink_msg_data(sockfd,&up_msg);
        struct downlink_msg_data down_msg;
        recv_downlink_msg_data(sockfd, &down_msg);
        //fprintf(stderr,"%s", down_msg.data);
    }
    return 0;
}