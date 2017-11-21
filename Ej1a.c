#include "stdio.h"

int suma= 0;
int i;
int main() 
{
     int n = 1000;

     for(i = 0; i < n; i++) 
     { 
         if(i%3==0 || i%5==0){
              suma += i;}
     }
     printf(" %d\n", suma);
return 0;
}
