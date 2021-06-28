#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
int main()
{ FILE *fptr;
  char filename[100], c;
  
    printf("Enter the filename to open \n");
    
    scanf("%s", filenamefull);
    
    //Opening the said file
    fptr = fopen(filename, "r");
    if (fptr == NULL)
    {  printf("Cannot open file \n");
        exit(0);
    }
  
    // Reading the contents
    c = fgetc(fptr);
    while (c != EOF)
    {
        printf ("%c", c);
        c = fgetc(fptr);
    }
  
    fclose(fptr);
    
    char q;
    
    while(q!='`'){q=getchar();}
    return 0;
}
