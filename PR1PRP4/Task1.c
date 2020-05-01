/*
Programmieren 1 - Praktikum 3
Autoren: Florian Tietjen und Eric Antosch
Beschreibung: Dieses Programm geht die verschiedenen Aktionen mit Arrays durch und wendet den BubbleSort an,
um das Array der Größe nach zu ordnen.
*/
//Includes
#include <stdio.h>

void swap(int *a, int *b)
{ //Tauscht die Werte von zwei Variablen im Array

    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
//Gibt die Werte des Arrays der Reihe nach aus
void arrPrint(int *arr, int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%d ", *(arr + i));
    }
    printf("\n");
}

void bubbleSort(int *arr, int length)
{

    for (int i = 0; i < length - 1; i++)
    {
        if (*(arr + i) > *(arr + i + 1))
        {
            swap((arr + i), (arr + i + 1));
        }
    }
}

int main(void)
{
    //Deklaration des Arrays
    int arr[10];
    //Initialisierung des Arrays durch den User
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        printf("Bitte geben Sie die %d.te Zahl ein:", i);
        scanf("%d", &arr[i]);
    }
    //Zeiger zum ersten Element des Arrays und die Größe des Arrays
    printf("Ausgabe des Arrays\n");
    arrPrint(&arr[0], sizeof(arr) / sizeof(arr[0]));
    //Verschiebung der Arrayelemente um eine Stelle nach vorne
    int temp = arr[sizeof(arr) / sizeof(arr[0]) - 1];
    for (int i = sizeof(arr) / sizeof(arr[0]) - 1; i > -1; i--)
    {
        if (i == 0)
        {

            arr[i] = temp;
        }
        else
        {
            arr[i] = arr[i - 1];
        }
    }
    printf("Verschiebung nach Vorne\n");
    arrPrint(&arr[0], sizeof(arr) / sizeof(arr[0]));
    int tempB = arr[0];

    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        if (i == sizeof(arr) / sizeof(arr[0]) - 1)
        {
            arr[i] = tempB;
        }
        else
        {
            arr[i] = arr[i + 1];
        }
    }
    printf("Verschiebung nach Hinten\n");
    arrPrint(arr, sizeof(arr) / sizeof(arr[0]));

    //Tauschen des zweiten und des neunten Elements
    swap(&arr[1], &arr[8]);
    printf("Tausche das zweite und neunte Element\n");
    arrPrint(arr, sizeof(arr) / sizeof(arr[0]));

    //Nur einmal nicht sortierte Nachbarn tauschen
    bubbleSort(&arr[0], sizeof(arr) / sizeof(arr[0]));
    printf("Nicht sortierte Arraynachbarn genau einmal tauschen\n");
    arrPrint(&arr[0], sizeof(arr) / sizeof(arr[0]));

    //Bubble Sort
    for (int t = 0; t < sizeof(arr) / sizeof(arr[0]) - 1; t++)
    {
        bubbleSort(&arr[0], sizeof(arr) / sizeof(arr[0]));
    }

    printf("Komplettes Array mit BubbleSort sortieren\n");
    arrPrint(arr, sizeof(arr) / sizeof(arr[0]));
    getch();
    return 0;
}