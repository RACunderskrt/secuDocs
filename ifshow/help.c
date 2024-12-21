/**
Class Help
 */
void displayDefaultMsg(){
    printf("ifshow [OPTION] - Displays information about the computer's network interfaces.\n");
    printf("Use\t-h | --help\tTo display the help.\n");
}

void displayHelp(){
    printf("ifshow [OPTION]\n");
    printf("OPTIONS :\n");
    printf("\t-a | --all\t\t\tTo display every network interfaces.\n");
    printf("\t-h | --help\t\t\tTo display the help.\n");
    printf("\t-i | --interface <name>\t\tEnter the interface's name.\n");
}

void displayWrongParam(){
    printf("Error : Wrong parameter.\nUse\t-h | --help\tTo display the help.\n");
}

void displayNoName(){
    printf("Error : No name given for the interface.\nUse\t-h | --help\tTo display the help.\n");
}

void displayWrongName(){
    printf("Error : There is no interface with this name.\nUse\t-h | --help\tTo display the help.\n");
}
