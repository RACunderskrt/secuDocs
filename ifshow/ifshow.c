#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ifaddrs.h>
#include <arpa/inet.h>

#include "vectorIPv6.c"
#include "help.c"

typedef struct ifaddrs ifaddrs;
typedef struct sockaddr sockaddr;
typedef struct sockaddr_in sockaddr_in;
typedef struct sockaddr_in6 sockaddr_in6;

typedef struct interface{
    char* name;
    char* ipv4;
    int maskIpv4;
    vectorIPv6 ipv6;
}interface;

#include "vectorInterface.c"

void displayInterface(interface* i){
    printf("%s\n\t IPv4 : %s/%d truc \n", i->name, i->ipv4, i->maskIpv4);
    displayVectorIPv6(i->ipv6);
}

char* getIPv4(char* res, ifaddrs* address){
    sockaddr_in *ip = (sockaddr_in*)address->ifa_addr;
    inet_ntop(AF_INET, &ip->sin_addr,res, INET_ADDRSTRLEN);
    return res;
}

char* getIPv6(char* res, ifaddrs* address){
    sockaddr_in6 *ip = (sockaddr_in6*)address->ifa_addr;
    inet_ntop(AF_INET6, &ip->sin6_addr,res, INET6_ADDRSTRLEN);
    return res;
}

int getMask(const sockaddr* netmask){
    int mask = 0;
    if(netmask->sa_family == AF_INET){
        sockaddr_in* maskV4 = (sockaddr_in *)netmask;
        uint32_t addr = ntohl(maskV4->sin_addr.s_addr);
        while(addr){
            mask += addr & 1;
            addr >>= 1;
        }
    }
    else if (netmask->sa_family == AF_INET6){
        sockaddr_in6* maskV6 = (sockaddr_in6 *)netmask;
        uint8_t* addr = (uint8_t *)&maskV6->sin6_addr;
        for(int i = 0; i < 16; i++){
            uint8_t byte = addr[i];
            while (byte){
                mask += byte & 1;
                byte >>= 1;
            }
        }
    }
    return mask;
}

void getIPs(ifaddrs* address, interface* i){
    char* res = malloc(INET6_ADDRSTRLEN);
    if(address->ifa_addr->sa_family == AF_INET){
        res = getIPv4(res, address);
        i->ipv4 = res;
        i->maskIpv4 = getMask(address->ifa_netmask);
    }
    else if(address->ifa_addr->sa_family == AF_INET6){
        res = getIPv6(res, address);
        addIPv6(&(i->ipv6), res, getMask(address->ifa_netmask));
    }
}

vectorInterface getAllAddress(){
    ifaddrs* address;
    
    if(getifaddrs(&address) == -1){
        printf("Error, pas d'interface.\n");
        //return NULL;
    }

    vectorInterface vi = init_vectorInterface();

    for(ifaddrs* buf = address; buf != NULL; buf = buf->ifa_next){
        if(buf->ifa_addr == NULL || buf->ifa_addr->sa_family == AF_PACKET)
            continue;

        if(existInVectorInterface(&vi, buf->ifa_name)){
            interface* i2 = getInterface(&vi, buf->ifa_name);    
            i2->name = buf->ifa_name;
            i2->ipv6 = init_vectorIPv6();
            getIPs(buf, i2);
        }
        else{
            interface i2;
            i2.name = buf->ifa_name;
            i2.ipv6 = init_vectorIPv6();
            getIPs(buf, &i2);
            addInterface(&vi, i2);
        }

        //printf("test mask : %d\n", getMask(buf->ifa_netmask));
    }
    freeifaddrs(address);
    return vi;
}

int main(int argc, char** argv){
    if(argc <= 1){ //Si il n'y a pas de param, afficher le msg puis fermer le programme
        displayDefaultMsg();
        return 0;
    }
    else if(!strcmp(argv[1],"-h") || !strcmp(argv[1],"--help")){ //si l'utilisateur veut afficher -h, afficher le msg puis fermer le programme.
        displayHelp();
        return 0;
    }

    vectorInterface res = getAllAddress(); //recup tt les interfaces.
    
    if(!strcmp(argv[1],"-a") || !strcmp(argv[1],"--all")){ //si le param est -a, on affiche tout.
        displayVectorInterface(res);
    }
    else if(!strcmp(argv[1],"-i") || !strcmp(argv[1],"--interface")){
        if(argc <= 2) //check si le param existe
            displayNoName();
        else{
            if(existInVectorInterface(&res, argv[2])){ //check si l'interface existe
                interface* i2 = getInterface(&res, argv[2]);
                displayInterface(i2); //afficher l'interface
            }
            else //ou afficher erreur;
                displayWrongName(); 
        } 
    }
    else{
        displayWrongParam();
    }
    deleteVectorInterface(&res);
    return 0;  
}