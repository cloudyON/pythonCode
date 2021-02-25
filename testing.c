#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>



int main(){
    /*
    char 형태 완전정복
    포인터 char 는  %s 포멧팅을 한다. + 큰따옴표
    char 는 %c 포멧팅을 한다. + 작은 따옴표
    배열 형태의 char는 %s 한다. + 큰따옴표
    배열은 %c 포멧팅을 사용한다. + 작은따옴표

    끝
    */

    
    char ab[5] = "abc";
    char ac = 'a';

    const char *abPtr = "abc";
    char *abcPtr = "ab";

    char *abd = (char*)malloc(100000);

    abd = "ha";

    char b[3] = "c";

    char cl[] = {'a', 'b','a','d','e','b','c'};

    printf("b : %s \n", b);
    printf("ac : %c \n", ac);
    printf("abPtr : %s\n", abPtr);
    printf("ab : %s\n", ab);
    printf("abd : %s\n", abd);

    printf("abcPtr : %s\n",abcPtr );
    abcPtr = "bcaolskdjfkjl";
    printf("abcPtr : %s\n",abcPtr );

    int one = 123512;
    int *onePtr = &one;

    ac = 'b';

    abcPtr = "bb";




    printf("one : %d\n", one);
    printf("onePtr : %d\n", *onePtr );
    printf("changed ac : %c\n",ac );
    printf("changed abcPtr : %s\n",abcPtr );


    printf("%c\n", cl[1]);
    for (int i = 0; i < (sizeof(cl)/sizeof(char)); i++){
      printf("%c\n",cl[i]);
    };

    cl[1] = 'b';
    printf("changed cl[1] : %c\n", cl[1]);


    return 0;
}
