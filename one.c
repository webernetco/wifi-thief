#include <stdio.h>

main(){
    // run System command
    system("cls");
    // make a constant variable (static variable it value never be change)
    const float PI = 3.14;
    printf("Enter the radius:");
    getchar();
    // get user input
    int no1;
    scanf("%d",&no1); /* & meaning is a scanf data stored a this variable..
    if you remove & keyword , user input never  stored in this variable*/
    printf("%d",no1);


    getch();
    // arithmetic operator
    printf("adding %d \n",50+2);
    printf("substraction  %d\n",50-2);
    printf("multiplication  %d\n",50*2);
    printf("Division %d \n",50/2);
    printf("module %d \n",2%50);

    int x = 2;
    printf("%d \n",x++); // adding one after print / post increment x-- (print value = 2,bring to next line x value=3)
    printf("%d \n",x);
    printf("%d \n",++x); // adding one before print / pre increment --x (print value = 4,bring to next line x value=4)
    printf("%d \n",x);


    getch();
    // variable declaration
    int integ = 21; // integer data type
    char charec = "A"; // character value
    float floating = 79.9; //floating point value
    double doubles =175.56521; // extra long floating point value

    //format Specifiers
    printf("print int %d \n",integ); // format integer
    printf("print char %c \n",charec); // format character
    printf("print float %f \n",floating); // format float
    printf("print float %0.2f \n",floating); // format float length
    printf("print double %lf \n",doubles); // format double

    /* get variable bit size
    (how many size get to ram declare each variable size) */
    printf("size of  int %d \n",sizeof(integ));

    // print something in console
    printf("\n\n hello mr,weber \n");

    // stay wait to user press key for print system data
    getch();
}
