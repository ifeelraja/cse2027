write a c program to print the ascii value of a character 

#include<stdio.h>
int main(){
    char ch = 'a';
    int a=ch;
    printf("the ASCII value pf %c is %d",ch,a);  
    return 0;
}


wap to convert temp from degree celsius to farenheit.

#include<stdio.h>
int main()
{
    int temp = 28;
    double faren=(1.8*temp)+32;
    printf("the temp in farenheit is %f ",faren);
    return 0;
}

wap to calculate area of ecllipse

#include<stdio.h>
int main(){
    int a=5;
    int b=6;
    float area=3.14*a*b;
    printf("the area of ellipse is %f",area);
    return 0;
}

wap to convert km to miles

#include<stdio.h>
int main(){
    double km=43.8;
    double miles=43.8*0.62;
    printf("the distance in miles is %f ",miles);
    return 0;
}

wap to check whether the no is armstrong number

#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int temp=n;
    int p=0;

    while(n>0){
        int rem = n%10;
        p = (p)+(rem*rem*rem);
        n=n/10;
    }
    if(temp==p){
        printf("yes,it is an armstrong number");
    }
    else{
        printf("no,it is not armstrong number");
    }
   return 0;
}

wap to check whether a number is palindrome or not

#include<stdio.h>
int main(){
    int num;
    printf("enter the number");
    scanf("%d",&num);
    int rev=0,a;
    int p=num;
    while(p!=0)
    {
        a=p%10;
        rev=rev*10+a;
        p/=10;
    }
    if(rev==num)
    printf("palindrome number");
    else
    printf("not palindrome number");
}

wap to find lcm nd hcf.

#include<stdio.h>
int main(){
    int a,b,x,y,t,hcf,lcm;
    printf("enter two integers\n");
    scanf("%d",&x,&y);
    a=x;
    b=y;
    while(b!=0){
        t=b;
        b=a%b;
        a=t;
    }
    hcf=a;
    lcm=(x*y)/hcf;
    printf("hcf of two numbers is = %d\n",hcf);
    printf("lcm of two numbers is = %d",lcm);
    return 0;
}

wap to print the multiplication of a table.

#include<stdio.h>
int main(){
    int num;
    printf("enter the number");
    scanf("%d",&num);
    int i;
    for(i=1;i<=10;i++)
    {
        int p=num*i;
        printf("%d x %d = %d\n",num,i,p);
    }
}

 wap  to find the factorial of a number

#include<stdio.h>
int main(){
    int num;
    printf("enter the number");
    scanf("%d",&num);
    int i,p=1;
    for(i=1;i<=num;i++){
        p=p*i;
    }
    printf("the factorial of number is %d",p);
}

wap to find all the prime numbers from 1 to 50.

#include<stdio.h>
int main(){
int i,num,count;
printf("the prime numbers are");
for(num=1;num<=50;num++){
    count=0;
    for(i=2;i<=num/2;i++){
        if(num%i==0){
            count++;
            break;
        }
    }
    if(count==0 && num!=1)
    printf("%d\n",num);
}
return 0;
}

wap to find the sum of series 1+11+111...n

#include<stdio.h>
int main(){
    int n;
    printf("enter any number");
    scanf("%d",&n);
    int i,j=0,sum=0;
    for(i=1;i<=n;i++){
        j=j*10+1;
        sum=sum+j;
    }
    printf("sum of the series is =%d",sum);
}

wap to print all leap year from 1 to 150.
#include<stdio.h>
int main(){
    int i;
    for(i=1;i<=150;i++){
        if(i%100==0){
            if(i%400==0)
            printf("%d\n",i);
        }
        else if (i%4==0){
            printf("%d\n",i);
        }
    }
}

wap to read weekday number and print weekday

#include<stdio.h>
int main(){
    int weekday;
    printf("enter the weekday number");
    scanf("%d",&weekday);
    switch(weekday){
        case 1:
        printf("monday");
        break;
        case 2:
        printf("tuesday");
        break;
        case 3:
        printf("wednesday");
        break;
        case 4:
        printf("thursday");
        break;
        case 5:
        printf("friday");
        break;
        case 6:
        printf("saturday");
        break;
        case 7:
        printf("sunday");
        break;
    }
}

wap to find maximum two numbers using switch case

#include<stdio.h>
int main(){
    int a,b;
    printf("enter a\n");
    scanf("%d",&a);

    printf("enter b\n");
    scanf("%d",&b);

    switch(a>b)
    {
        case 0:
        printf("%d is maximum",b);
        break;
        case 1:
        printf("%d is maximum",a);
        break;
    }
    }

wap to print number pyramid pattern

#include<stdio.h>
int main(){
    int n;
    printf("enter a number");
    scanf("%d",&n);
    int i,j;
    for(i=n;i>0;i--){
        for(j=1;j<=n;j++)
        {
            if(j<1)
            printf(" ");
            else if (j>=i)
            printf("*");

        }
        printf("\n");
    }
}

#include<stdio.h>
int main(){
    int i,j,k,l,m,n;
    printf("enter a number");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        for(k=(n-1);k>=i;k--){
            printf(" ");
        }
        for(j=1;j<=i;j++){
            printf("%d",j);
        }
        for(m=(i-1);m>0;m--){
            printf("%d",m);
        }
        for(l=(n-1);l>=i;l--){
            printf(" ");
        }
    }
    return 0;
}


find the transpose of given matrix

#include<stdio.h>
int main()
{
int mat[3][4]={1,5,6,8,2,7,6,8,7,8,9,6};
int transpose[4][3];
for(int i=0;i<3;i++)
{
for(int j=0;j<4;j++)
{
transpose[j][i]=mat[i][j];
}
}
for(int i=0;i<4;i++)
{
for(int j=0;j<3;j++)
{
printf("%d",transpose[i][j]);
}
printf("\n");
}
}


write a program to print the lower and upper triangular matrix for the given input

#include<stdio.h>
int main()
{
int mat[3][3]={1,7,8,7,6,5,2,3,9};
int upper[3][3]={0};
int lower[3][3]={0};
for(int i=0;i<3;i++)
{
for(int j=0;j<=1;j++)
{
lower[i][j]=mat[i][j];
}
}
for(i=0;i<3;i++)
{
for(j=i;j<3;j++)
{
upper[i][j]=mat[i][j];
}
}
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
printf("%d\t",lower[i][j]);
}
printf("\n");
}
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
printf("%d\t",upper[i][j]);
}
printf("\n");
}
}


3.write a program to calculate the sum of diagonal element from left to right and right to left 

#include<stdio.h>
int main()
{
int mat[3][3]={1,7,8,6,5,2,3,9};
int sum1=0;
int sum2=0;
for(int i=0;i<3;i++)
{
sum1=sum1+mat[i][j];
sum2=sum2+mat[i][2-i];
}
printf("left to right sumof diagonal elements is %d\n",sum1);
printf("right to left sum of diagonal elements is %d",sum2);
}

4.write a program to perform matrix multiplication using 2D array.take input from user

#include<stdio.h>
int main()
{
int r1,c1,r2,c2;
printf("enter the no. of rows and columns of first matrix");
scanf("%d %d",&r1,&c1);
printf("enter the no. of rows and columns of second matrix");
scanf("%d%d",&r2,&c2);
int m1[r1][c1];
int m2[r2][c2];
int result[r1][c2];
for(int i=0;i<r1;i++)
{
for(int j=0;j<r2;j++)
{
result[i][j]=0;
}
}
printf("enter the elements of matrix 2");
for(int i=0;i<r2;i++)
{
for(int j=0;j<c2;j++)
{
scanf("%d",&m2[i][j]);
}
}
for(int i=0;i<r1;i++)
{
for(int j=0;j<c2;j++)
{
for(int k=0;k<c1;k++)
{
if(c1==r2)
{
result[i][j]=result[i][j]+m1[i][k];
}
else
printf("these matrices cannot be mltiplied");
}
}
for(int i=0;i<r1;i++)
{
for(int j=0;j<c2;j++)
{
printf("%d\t",result[i][j]);
}
printf("\n");
}
}

5.write a program to identify the given two strings are similar or not without using strcmp()

#include<stdio.h>
int main()
{
char s1[10]="abcD",s2[10]="abcd";
int similar=1;
int i=0;
while(s1[i]!='\0'||s2[i]!='\0')
{
if(s1[i]!=s2[i])
{
similar=0
break;
}
i++;
}
if(similar==0)
printf("%s and %s are not similar",s1,s2);
else
printf("%s and %s are similar",s1,s2);
}




6.write a program to include all the string function in a string program such as strcmp(),strcat90,strlen(),strcpy()


#include<stdio.h>
#include<string.h>
int main()
{
char str[10]="abc",str[10]="ABC";
printf("%d\n",strlen(str1));
printf("%s\n",strcpy(str1,str2));
printf("%d\n",strcmp(str1,str2));
printf("%s\n",strcat(str1,str2));
}

7.use puts and gets in a strinng program
#include<stdio.h>
#include<string.h>
int main()
{
char str[10];
printf("enter a string");
gets(str);
printf("your extetended string is");
puts(str);
}

8.write a program to print all negative elements of array

#include<stdio.h>
int main()
{
int length;
printf("enter the length of array\n");
scanf("%d",&length);
int array[length];
printf("enter the elements of array");
for(int i=0;i<length;i++)
{
scanf("%d",&array[i]);
}
for(int i=0;i<length;i++)
{
if(array[i]<0)
printf("%d",array[i]);
}
}

9.write a program to input a 2D matrix and perform the folllowinng operations
i)reverse the elements of each row of the matrix
ii)reverse the elements of each column of the matrix


#include<stdio.h>
int main()
{
int r1,c1;
printf("enter the no. of rows and columns of matrix ");
scanf("%d%d",&r1,&c1);
int mat[r1][c1];
printf("enter the elements of matrix");
for(int i=0;i<r1;i++)
{
for(int j=0;j<r1;j++)
{
scanf("%d",&mat[i][j]);
}
}
printf("matrix after reversing the elements of each row");
for(int i=0,i<r1;i++)
{
for(int j=0;j<c1;j++)
{
printf("%d\t",mat[i][c1-1-i]);
}
printf("\n");
}
printf("matrix after reversing the elements of each column");
for(int i=0;i<r;i++)
{
for(int j=0;j<c1;j++)
{
printf("%d\t",mat[r1-1-i][j]);
}
printf("\n");
}
}








ASSIGNMENT 7
wap to identify smallest ,second largest and second smallest number from unsorted array

#include<stdio.h>
int main()
{
int a[10]={13,4,8,6,2,9,23,46,38,12};
for(int i=0;i<10;i++)
{
int temp;
for(int j=i+1;j<10;j++)
{
if(a[i]<a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}
printf("largest=%d\n",a[0]);
printf("smallest=%d\n",a[9]);
printf("second largest=%d\n",a[1]);
printf("second samllest=%d\n",a[8]);
}

2.wap to perform string operstion in ascending and descesinding order using array

#include<stdio.h>
int main()
{
int a[10]={13,4,8,6,2,9,23,46,38,12};
for(int i=0;i<10;i++)
{
int temp;
for(int j=i+1;j<10;j++)
{
if(a[i]<a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}
for(int i=0;i<10;i++)
{
printf("%d\t",a[i]);
}
}

3. wap to find the position of an element required by user usinng array

#include<stdio.h>
int main()
{
int a[8]={2,3,5,7,6,8,9,10};
int s;
printf("enter a no.");
scanf("%d",&s);
for(int i=0;i<8;i++)
{
if(a[i]==s)
printf("%d",i);
}
}

4.wap to raed n names ,store them in form of array and then sort them in alphabeticatal order 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n;
    char names[100][100];

    printf("Enter the number of names: ");
    scanf("%d", &n);

    printf("Enter the names: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%s", names[i]);
    }

    // Sort the names in alphabetical order
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (strcmp(names[i], names[j]) > 0)
            {
                char temp[100];
                strcpy(temp, names[i]);
                strcpy(names[i], names[j]);
                strcpy(names[j], temp);
            }
        }
    }

    // Print the sorted names
    printf("The sorted names are: ");
    for (int i = 0; i < n; i++)
    {
        printf("%s ", names[i]);
    }

    return 0;
}


5.wap to merge the first name,middle name,and last name with or without using strcat()

#include<stdio.h>
#include<string.h>
int main()
{
char s[40],s1[10],s2[20];
printf("enter first name\n");
scanf("%s",&s);
printf("enter middle name\n");
scanf("%s",&s1);
printf("enter last name\n");
scanf("%s",&s2);
strcat(s,s1);
strcat(s,s2);
printf("%s",s);
return 0;
}

6.wap to sort strinng in alphabetical order

#include<stdio.h>
#include<string.h>
int main()
{
char string[100];
printf("\n\tenter the string");
scanf("%s",string);
char temp;
int i,j;
int n=strlen(string);
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(string[i]>string[j])
{
temp=string[i];
string[i]=string[j];
string[j]=temp;
}
}
}
printf("the sorted string is %s",string);
return 0;
}

ASSIGNMENT 8
1.wap to convert decimal into binary using direct recursion

#include <stdio.h>
 
// Decimal to binary conversion
// using recursion
int find(int decimal_number)
{
    if (decimal_number == 0) 
        return 0; 
    else
        return (decimal_number % 2 + 10 * 
                find(decimal_number / 2));
}
 
// Driver code 
int main()
{
    int decimal_number;
    printf("enter the decimal");
    scanf("%d",&decimal_number);
    printf("%d", find(decimal_number));
    return 0;
}


2.wap to multiply two matrices using recursion
///matrix multiplication

#include<stdio.h>
#define N 50
int main    (){
    int i,j,k, a[N][N], b[N][N], c[N][N], sum, m,n,p,q;

printf("Enter rows and coloumns of 1st matrix\n");
scanf("%d %d", &m, &n);
printf("rows %d coloumns %d\n", m,n);


    printf("Enter elemnts of 1st matrix\n");
for ( i = 0; i < m; i++)
{
    for ( j = 0; j < n; j++)
    {
       scanf("%d", &a[i][j]);
    }
}
printf("The first matrix is\n");
for ( i = 0; i < m; i++)
{
    for ( j = 0; j < n; j++)
    {
        printf("%d\t" , a[i][j]);
    }
    printf("\n");
}
printf("Enter rows and coloumns of 2nd matrix\n");
scanf("%d %d", &p,&q);
printf("rows %d coloumns %d\n", p,q);

printf("Enter elements of 2nd matrix\n");
for ( i = 0; i < p; i++)
{
    for ( j = 0; j < q; j++)
    {
       scanf("%d", &b[i][j]);
    }
    
}
printf("The second matrix is\n");
for ( i = 0; i < p; i++)
{
    for ( j = 0; j < q; j++)
    {
        printf("%d\t" , b[i][j]);
    }
    printf("\n");
}
if (n!= p)
{
    printf("you cannot multiply\n");
}

else{

for ( i = 0; i < m; i++)
{
    for (j = 0; j < q; j++)
    {
        sum = 0;
        for ( k = 0; k < m;k++)
        {
           sum = sum +( a[i][k]*b[k][j] );
           c[i][j]=sum;

        }
        
    }
    
}
    printf("MATRIX MULTPLICATION\n");
    for ( i = 0; i < m; i++)
    {
        for ( j = 0; j < q; j++)
            {
             printf("%d\t", c[i][j]);
            }
        printf("\n");
    }
}

return 0;
}

5.wap to print natural no. from 1 to n using indirect recursion

#include<stdio.h>
void increasing(int n){
    if(n==0) return; //base case
    increasing(n-1);//call
    printf("%d\n", n);//code
    return;
}
int main(){
    int n;
    printf("Enter the number : ");
    scanf("%d",&n);
    increasing(n);
    return 0;
}


4. wap to identify fibonacci no. using two numbers

#include <stdio.h>
int isFibonacci(int num, int a, int b) {
    if (num == a || num == b) {
        return 1;
    } else if (num < b) {
        return 0;
    } else {
        return isFibonacci(num, b, a + b);
    }
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (isFibonacci(num, 0, 1)) {
        printf("%d is a Fibonacci number.\n", num);
    } else {
        printf("%d is not a Fibonacci number.\n", num);
    }

    return 0;
}


5.wap to identify the key element that is present inside the array using binary search.if element is present inside the array ,then display the positionof that key element insisde the array (using recursion)

#include<stdio.h>
int binarysearch(int arr[1],int l,int r,int x)
{
if(r>=1)
{
int mid=l+(r-1)/2;
if(arr[mid]==x)
return mid;
if(arr[mid]>x)
return binarysearch(arr,l,mid-1,x);
return binarysearch(arr,mid+1,r,x);
}
return -1;
}
int main()
{
int arr[]={2,3,4,10,40};
int size=sizeof(arr)/sizeof(arr[0]);
int x;
printf("enter elements to be searched");
scanf("%d",&x);
int index=binarysearch(arr,0,size-1,x);
if(index==-1)
{
printf("element is not present");
}
else
{
printf("element is presnt at index %d ",index);
}
return 0;
}


6. wap to implement linear search using iterative and recursion approach

#include<stdio.h>
int main()
{
int arr[10]={3,4,1,7,5,8,11,42,3,13};
int key=4;
int index;
int i;
for(int i=0;i<10;i++)
{
if(arr[i]==key)
{
index=1;
}
}
if(index==1)
printf("the element is  present");
else
printf("not");
return 0;
}

by recursion-

#include<stdio.h>
int linearsearch(int arr[],int size,int key)
{
for(int i=0;i<size;i++)
{
if(arr[i]==key)
{
return i;
}
}
return -1;
}
int main()
{
int arr[10]={3,4,1,7,5,8,11,42,3,13};
int size=sizeof(arr)/sizeof(arr[0]);
int key=4;
int index=linearsearch(arr,size,key);
if(index==-1)
printf("the element is not present ");
else
printf("the element is present ");
return 0;
}

wap to implement binary search using iterative and recursive approach

#include<stdio.h>
int binarysearch(int arr[],int x,int low,int high)
{
while(low<=high)
{
int mid=low+(high-low)/2;
if(arr[mid]==x)
return mid;
if(arr[mid]<x)
low=mid-1;
else
high=mid-1;
}
return -1;
}
int main()
{
int arr[]={3,4,5,6,7,8,9};
int  n=sizeof(arr)/sizeof(arr[0]);
int x=4;
int result=binarysearch(arr,x,0,x-1);
if(result==-1)
printf("not found");
else
printf("found");
return 0;
}




8. wap to find the gcd of two no.using recursion


#include<stdio.h>
int hcf(int n1,int n2);
int main()
{
int n1,n2;
printf("enter two positive integers");
scanf("%d%d",&n1,&n2);
printf("gcd of %d and %dis %d ",n1 ,n2,hcf(n1,n2));
return 0;
}
int  hcf(int n1,int n2)
{
if(n2!=0)
return hcf(n2,n1%n2);
else
return n1;
}


9.wap to print the fibonacci series using tail recursion



10.wap to calculate the sum of numbers from 1 to n using recursion(segmentation fault)
#include<stdio.h>
int sum(int n);
int main()
{
int num;
printf("enter a positive integer");
scanf("%d",num);
printf("sum=%d",sum(num));
return 0;
}
int sum(int n)
{
if(n!=0)
return n+sum(n-1);
else
return n;
}

Wap to find sum upto n terms

#include<stdio.h>
int addnumbers(int a);
int main(){
    int n;
    printf("enter number n=");
    scanf("%d",&n);
    printf("sum=%d",addnumbers(n));
}
int addnumbers(int a){
    if(a!=0)
    return a + addnumbers(a-1);
    else 
    return a;
}



ASSIGNMENT 9
1.wap to add two numbers using pointers

#include<stdio.h>
int main()
{
int a=20;
int b=30;
int *p1=&a;
int *p2=&b;
int sum=*p1+*p2;
printf("sum is %d",sum);
}

2.wap to find the maximum numbers between two numbers using a pointer

#include<stdio.h>
int main()
{
int a=20;
int max;
int b=45;
int *p1=&a;
int *p2=&b;
if(*p1>*p2)
max=*p1;
else
max=*p2;
printf("maximum is %d",max);
return 0;
}

3. wap to store n elements in an array and print elements using pointer

#include<stdio.h>
int main(){
    int n;
    printf("Enter the size of array : ");
    scanf("%d", &n);
    int arr[n]; 
    printf("Enter the elements of the array : \n");
    for(int i = 0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    int* ptr = arr; // initialize
    for(int i = 0; i<n; i++){
        printf("%d ",*ptr);
        ptr++;
    }
}


4. wap to print a string in reverse using pointer

#include<stdio.h>
void revstring(char *str)
{
int l,i;
char *bptr,*eptr,ch;
l=strlen(str);
bptr=str;
eptr=str+l-1;
for(i=0;i<(l-1)/2;i++)
{
ch=*eptr;
*eptr=*bptr;
*bptr=ch;
bptr++;
eptr--;
}
}
int main()
{
char str[100]="india";
revstring(str);
printf("reverse of string =%s\n",str);
return 0;
}

5. wap to count the number of vowels,consonants in given string using a pointer(error)

#include<stdio.h>
#include<string.h>
int main()
{
char str[50];
printf("enter the string \n");
gets(str);
char *p=str;
int b=strlen(str);int countv=0;
int countc=0;
for(int i=0;i<b;i++)
{
if(*(p+i)=='a'||*(p+i)=='e'||*(p+i)=='i'||*(p+i)=='o'||*(p+i)=='u'))
{
countv++;
}
elseif(*(p+i)=='A'||*(p+i)=='E'||*(p+i)=='I'||*(p+i)=='O'||*(p+i)=='U'||)
{
countv++;
}
else
{
countc++;
}
printf("no of vowels %d\n",countv);
printf("no of consonants%d\n",countc);
return 0;
}

6.wap to print all the permutation of given string using pointers(segmentation fault)

#include<stdio.h>
int main()
{
int a,b,c,d;
char str[4]={'a','b','c','d'};
char *f=str;
for(int i=0;i<4;i++)
{
for(int j=0;j<4;j++)
{
for(int k=0;k,4;k++)
{
for(int l=0;l<4;l++)
{
a=*(f+i);
b=*(f+j);
c=*(f+k);
d=*(f+l);
if(a!=b && a!=c && a!=d && b!=c && b!=d && c!=d)
printf("%c%c%c%c",a,b,c,d);
}
}
}
printf("\n");
}
return 0;
}







7.wap to swap two numbers using pointers

#include<stdio.h>
int main()
{
int a,b,*p,*q,temp;
printf("enter a and b");
scanf("%d%d",&a,&b);
p=&a;
q=&b;
temp=*p;
*p=*q;
*q=temp;
printf("after swapping a = %d and b = %d",a,b);
return 0;
}



8.wap to print all the alphabet using pointer

#include<stdio.h>
int main()
{
char ch='a';
int yy=(int)ch;
int *temp=&yy;
char ch1='A';
int yy1=(int)ch1;
int *temp1=&yy1;
for(int i=0;i<2b;i++)
{
printf("%c",temp+i);
}
printf("\n");
for(int i=0;i<26;i++)
{
printf("%c",*temp1+i);
}
printf("\n");
return 0;
}








9.try to implement double pointer in c

#include<stdio.h>
int main()
{
int a=10;int *pa;int **ppa;
pa=7a;ppa=&pa;
printf("%d\n",**ppa);
return 0;
}

10.wap to perform subtraction of two pointers

#include<stdio.h>
int main()
{
int arr[]={2,3,5,7,9,10,12};
int *p=arr;
int *q=arr+2;
printf("subtraction of two pointers is %d \n",*p-*q);
return 0;
}

























wap to calc the length of a string using a pointer
#include<stdio.h>
int main(){
    char str[20]="shubham";
    char*p=str;
    int c=0;
    while(*p!='\0'){
        c++;
        p++;
    }
    printf("the length of string is %d",c);
}

wap to compute the sum of all elements in an array using pointer.

#include<stdio.h>
int main(){
    int arr[5]={1,2,3,4,5};
    int *p=arr;
    int i,sum;
    for(i=0;i<5;i++){
        sum=sum+*(p+i);
    }
    printf("sum of all elements of array is %d",sum);
    return 0;
}

wap to perform the addn and subtraction operation on pointer.

#include<stdio.h>
int main(){
    int a=20;
    int b=30;
    int *p1=&a;
    int *p=&b;
    int sum=*p+*p1;
    int s=*p1-*p;
    printf("the sum is %d\n",sum);
    printf("diff is %d",s);
}
 or
#include<stdio.h>
int main(){
    int n=4;
    int*ptr1,*ptr2;
    ptr1=&n;
    ptr2=&n;
    printf("pointer ptr2 before addition");
    printf("%p\n",ptr2);
    ptr2=ptr2+3;
    printf("pointer ptr2 after addition");
    printf("%p\n",ptr2);

     printf("pointer ptr2 before subtraction");
    printf("%p\n",ptr2);
    ptr2=ptr2-3;
    printf("pointer ptr2 after subtraction");
    printf("%p\n",ptr2);
}

wap to implement the increment and decrement operation on pointer.

#include<stdio.h>
int main(){
    int a;
    int *pt;
    a=10;
    pt=&a;
    (*pt)++;
    printf("\n [1]: increment value of a= %d",a);

    ++(*pt);
    printf("\n [1]: increment value of a= %d",a);

    (*pt)--;
    printf("\n [1]: decrement value of a= %d",a);

    --(*pt);
    printf("\n [1]: decrement value of a= %d",a);
}

wap to implement double pointer

#include<stdio.h>
int main(){
    int var=789;
    int *ptr2;
    int **ptr1;
    ptr2=&var;
    ptr1=&ptr2;
    printf("value of var = %d",var);
    printf("value of var using single pointer = %d\n",*ptr2);
    printf("value of var using double pointer = %d\n",**ptr1);
}








ASSIGNMENT 7.txt


