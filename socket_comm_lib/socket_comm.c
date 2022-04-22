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

void recv_downlink_msg_data(int sockfd, struct downlink_msg_data * msg){
    //TODO: error handling
    int ret_recv=recv(sockfd,msg,sizeof(struct downlink_msg_data),0);
}

//use example
int main(int argc, char const* argv[])
{
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
        fprintf(stderr,"%s", down_msg.data);
    }
    return 0;
}