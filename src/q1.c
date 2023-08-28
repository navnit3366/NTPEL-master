
/*Given two arrays of integers output the smallest number in the
first array not present in the second one.

Input Specification: 
The first line contains the size N1 of the first array.
Next line give the contents of the first array.
Next line contains the size N2 of the second array.
Next line give the contents of the second array.

Output Format:
Output must be a single number which is the smallest number occurring
in the first array that does not occur in the second. In case there is
no such number, output NO.

Variable Constraints:
The sizes of the arrays are smaller than 20.
Each array entry is an integer which fits an int data type.

Example:
Input:
3
2 3 4
4
1 3 5 7

Output: 2                                               */

#include<stdio.h>

void main(){
    int var1,size1,var2,size2,a[20],b[20],key,flag=0,flag2=0;
    
    scanf("%d",&size1);
    for(var1=0;var1<size1;var1++)
        scanf("%d",&a[var1]);

    scanf("%d",&size2);
    for(var1=0;var1<size2;var1++)
        scanf("%d",&b[var1]);

    for(var1=0;var1<size1;var1++){ 
        for(var2=0;var2<size2;var2++){
            if(a[var1]==b[var2]){
                flag=1;
            }    
        }

        if(flag!=1){

            if(flag2==0){
                key=a[var1]; //printf("\n%d",&key);
                flag2=1;
            }
            else
            {
                if(key>a[var1]){
                    key=a[var1];    // printf("\n%d",&key);
                }    
            }
        }flag=0;
    }

    if(flag2==0){
            printf("NO");
    }    
    else
    {
            printf("%d",key);
    }
}
