/**
Class Vector IPv6
*/
typedef struct vector{
    char** array;
    int* secondArray;
    int size;
}vectorIPv6;

vectorIPv6 init_vectorIPv6(){
    vectorIPv6 res;
    res.size = 0;
    res.array  = malloc(INET6_ADDRSTRLEN);
    res.secondArray = malloc(sizeof(int));
    return res;
}

void addIPv6(vectorIPv6* v, char* f, int m){
    printf("test : %d\n", m);
    if(!v->size){
        v->array[0] = f;
        v->secondArray[0] = m;
    }
    else{
        char** res = realloc(v->array, (v->size+1)*INET6_ADDRSTRLEN);   
        res[v->size] = f;
        v->array = res;

        int* secondRes = realloc(v->secondArray, (v->size+1)*sizeof(int));   
        secondRes[v->size] = m;
        printf("test : %d %d\n",  secondRes[v->size], v->size);
        v->secondArray = secondRes;

    }
    v->size++;   
}

void displayVectorIPv6(vectorIPv6 v){
    printf("\t IPv6 :");
    for(int i = 0; i < v.size; i++){
        printf("\t%s/%d\n", v.array[i], v.secondArray[i]);
    }
}

void deleteVectorIPv6(vectorIPv6* v){
    v->size = 0;
    free(v->array);
    free(v->secondArray);
}