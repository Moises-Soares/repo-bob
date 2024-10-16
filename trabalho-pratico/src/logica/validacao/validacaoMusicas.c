#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "include/infra/entidades.h"        //escachado

// hh:mm:ss
int validaEstruturaHoras(char* duracaoMusica) {

    if (strlen (duracaoMusica) != 8)
        return 0;
    if (duracaoMusica[2] != ':' || duracaoMusica[5] != ':')
        return 0;
    if (!isdigit(duracaoMusica[0]) || !isdigit(duracaoMusica[1]) ||   // hh
        !isdigit(duracaoMusica[3]) || !isdigit(duracaoMusica[4]) ||   // mm
        !isdigit(duracaoMusica[6]) || !isdigit(duracaoMusica[7])) {   // ss
        return 0;
    }
    return 1;
}

int validaValoresHoras (char* duracaoMusica) {
    //TODO: atoi
    int horas = (duracaoMusica[0] - '0')*10 + (duracaoMusica[1] - '0');
    int minutos = (duracaoMusica[3] - '0') * 10 + (duracaoMusica[4] - '0');
    int segundos = (duracaoMusica[6] - '0') * 10 + (duracaoMusica[7] - '0');

    if (horas < 0 || horas > 99) 
        return 0;
    if (minutos < 0 || minutos > 59) 
        return 0;
    if (segundos < 0 || segundos > 59) 
        return 0;
    return 1;
}


int validaDuracao(char* duracaoMusica) {
    if (!validaEstruturaHoras(duracaoMusica))
        return 0;
    if (!validaValoresHoras(duracaoMusica))
        return 0;
    return 1;
}

