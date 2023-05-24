// ConsoleApplication1.cpp : Ce fichier contient la fonction 'main'. L'exécution du programme commence et se termine à cet endroit.
//

#include <stdio.h>

void Personnage(char Race,char Classe);

int main()
{
    int var1,var2,var3;
    printf("Rentrer une valeur \n");
    scanf_s("%d",&var1);
    printf("Rentrer une 2e valeur \n");
    scanf_s("%d",&var2);
    printf("Rentrer une 3e valeur \n");
    scanf_s("%d", &var3);
    char mot1 = 'Bonjour';
    char mot2 = 'Elfe';
    char mot3 = 'Ranger';
    printf("%s", mot2);
    Personnage(mot2, mot3);
}

void Personnage(char Race, char Classe) {
    printf("%s %s a prit une quête d'aveturier", Race, Classe);
}
