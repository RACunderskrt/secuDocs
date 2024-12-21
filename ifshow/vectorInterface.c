/**
Class Vector Interfaces
*/

typedef struct vectorip{
    interface* array;
    int size;
}vectorInterface;

vectorInterface init_vectorInterface(){
    vectorInterface res;
    res.size = 0;
    res.array  = malloc(sizeof(interface));
    return res;
}

void addInterface(vectorInterface* v, interface f){
    if(!v->size)
        v->array[0] = f;
    else{
        interface* res = realloc(v->array, (v->size+1)*sizeof(interface));   
        res[v->size] = f;
        v->array = res;
    }
    v->size++; 
}

void displayVectorInterface(vectorInterface v){
    printf("==============================\n");
    printf("Interface : %d\n", v.size);
    for(int i = 0; i < v.size; i++){
        printf("%d - %s\n\t IPv4 : %s/%d\n", i, v.array[i].name, v.array[i].ipv4, v.array[i].maskIpv4);
        displayVectorIPv6(v.array[i].ipv6);
    }
    printf("==============================\n");
}

interface* getInterface(vectorInterface* v, char* name){
    for(int i = 0; i < v->size; i++){
        if(!strcmp(v->array[i].name, name))
            return &(v->array[i]);
    }
}

int existInVectorInterface(vectorInterface* v, char* name){
    for(int i = 0; i < v->size; i++){
        if(!strcmp(v->array[i].name, name))
            return 1;
    }
    return 0;
}

void deleteVectorInterface(vectorInterface* v){
    for(int i = 0; i < v->size; i++)
        deleteVectorIPv6(&(v->array[i].ipv6));
    
    v->size = 0;
    free(v->array);
}