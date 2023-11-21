write a c program to perform addition, subtraction, multiplication and division. 

#include <stdio.h>

int main() {
    float num1, num2, result;
    char operator;

    // Input
    printf("Enter first number: ");
    scanf("%f", &num1);

    printf("Enter operator (+, -, *, /): ");
    scanf(" %c", &operator);

    printf("Enter second number: ");
    scanf("%f", &num2);

    // Calculation and Output
    switch (operator) {
        case '+':
            result = num1 + num2;
            printf("Result: %.2f\n", result);
            break;

        case '-':
            result = num1 - num2;
            printf("Result: %.2f\n", result);
            break;

        case '*':
            result = num1 * num2;
            printf("Result: %.2f\n", result);
            break;

        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                printf("Result: %.2f\n", result);
            } else {
                printf("Error: Division by zero is undefined.\n");
            }
            break;

        default:
            printf("Error: Invalid operator.\n");
            break;
    }

    return 0;
}


Write a C program that accepts the principle, rate of interest, and time and calculates simple interest.

#include <stdio.h>

int main() {
    float principal, rate, time, simple_interest;

    // Input
    printf("Enter the principal amount: ");
    scanf("%f", &principal);

    printf("Enter the rate of interest (in percentage): ");
    scanf("%f", &rate);

    printf("Enter the time (in years): ");
    scanf("%f", &time);

    // Calculation
    simple_interest = (principal * rate * time) / 100;

    // Output
    printf("Simple Interest: %.2f\n", simple_interest);

    return 0;
}



Write a C program to find quotient and remainder of two numbers.
#include <stdio.h>

int main() {
    int dividend, divisor, quotient, remainder;

    // Input
    printf("Enter the dividend: ");
    scanf("%d", &dividend);

    printf("Enter the divisor: ");
    scanf("%d", &divisor);

    // Calculation
    quotient = dividend / divisor;
    remainder = dividend % divisor;

    // Output
    printf("Quotient: %d\n", quotient);
    printf("Remainder: %d\n", remainder);

    return 0;
}


write a c program to swap the values of two variables.
#include <stdio.h>

int main() {
    int a, b, temp;

    // Input
    printf("Enter the value of a: ");
    scanf("%d", &a);

    printf("Enter the value of b: ");
    scanf("%d", &b);

    // Swapping
    temp = a;
    a = b;
    b = temp;

    // Output
    printf("After swapping:\n");
    printf("a: %d\n", a);
    printf("b: %d\n", b);

    return 0;
}

write a c program to find average of 2 numbers
#include <stdio.h>

int main() {
    float num1, num2, average;

    // Input
    printf("Enter the first number: ");
    scanf("%f", &num1);

    printf("Enter the second number: ");
    scanf("%f", &num2);

    // Calculation
    average = (num1 + num2) / 2;

    // Output
    printf("Average: %.2f\n", average);

    return 0;
}

write a c program to find speed .
#include <stdio.h>

int main() {
    float distance, time, speed;

    // Input
    printf("Enter the distance (in kilometers): ");
    scanf("%f", &distance);

    printf("Enter the time taken (in hours): ");
    scanf("%f", &time);

    // Calculation
    speed = distance / time;

    // Output
    printf("Speed: %.2f km/h\n", speed);

    return 0;
}


Write a C program that accepts two integers from the user and calculates the sum of the two
integers.
#include <stdio.h>

int main() {
    int num1, num2, sum;

    // Input
    printf("Enter the first integer: ");
    scanf("%d", &num1);

    printf("Enter the second integer: ");
    scanf("%d", &num2);

    // Calculation
    sum = num1 + num2;

    // Output
    printf("Sum: %d\n", sum);

    return 0;
}


Write a C program to display ASCII  values of characters 'a' to 'z' and the characters 'A' to 'Z'.
#include <stdio.h>

int main() {
    char lowercase, uppercase;

    // Display ASCII values for lowercase letters
    printf("ASCII values for lowercase letters:\n");
    for (lowercase = 'a'; lowercase <= 'z'; ++lowercase) {
        printf("%c: %d\n", lowercase, lowercase);
    }

    // Display ASCII values for uppercase letters
    printf("\nASCII values for uppercase letters:\n");
    for (uppercase = 'A'; uppercase <= 'Z'; ++uppercase) {
        printf("%c: %d\n", uppercase, uppercase);
    }

    return 0;
}

Write a C program to find the sum of the series  1 square +  2 square  upto n square. The program takes the value of "n" and input and produce the sum of series as output.
#include <stdio.h>

int main() {
    int n, i, sum = 0;

    // Input
    printf("Enter the value of n: ");
    scanf("%d", &n);

    // Calculation
    for (i = 1; i <= n; ++i) {
        sum += i * i;
    }

    // Output
    printf("Sum of the series 1^2 + 2^2 + ... + %d^2: %d\n", n, sum);

    return 0;
}


Write a C program to check vowel or consonent using switch case.
#include <stdio.h>

int main() {
    char ch;

    // Input
    printf("Enter a character: ");
    scanf(" %c", &ch);

    // Switch case to check vowel or consonant
    switch(ch) {
        case 'a':
        case 'A':
        case 'e':
        case 'E':
        case 'i':
        case 'I':
        case 'o':
        case 'O':
        case 'u':
        case 'U':
            printf("%c is a vowel.\n", ch);
            break;
        default:
            printf("%c is a consonant.\n", ch);
    }

    return 0;
}


Write a C program to check Even or Odd number using switch case.
#include <stdio.h>

int main() {
    int num;

    // Input
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Switch case to check even or odd
    switch (num % 2) {
        case 0:
            printf("%d is an even number.\n", num);
            break;
        case 1:
            printf("%d is an odd number.\n", num);
            break;
        default:
            printf("Invalid input.\n");
    }

    return 0;
}

Write a C program to check positive negative or zero using switch case.
#include <stdio.h>

int main() {
    int num;

    // Input
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Switch case to check positive, negative, or zero
    switch ((num > 0) - (num < 0)) {
        case 1:
            printf("%d is a positive number.\n", num);
            break;
        case -1:
            printf("%d is a negative number.\n", num);
            break;
        case 0:
            printf("%d is zero.\n", num);
            break;
        default:
            printf("Invalid input.\n");
    }

    return 0;
}


Write a C program to check positive negative or zero using switch case.
#include <stdio.h>

int main() {
    int num;

    // Input
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Switch case to check positive, negative, or zero
    switch (num > 0) {
        case 1:
            printf("%d is a positive number.\n", num);
            break;
        case 0:
            switch (num < 0) {
                case 1:
                    printf("%d is a negative number.\n", num);
                    break;
                case 0:
                    printf("%d is zero.\n", num);
                    break;
            }
            break;
        default:
            printf("Invalid input.\n");
    }

    return 0;
}


Write a C program to print all Even and Odd numbers from 1 to 100
#include <stdio.h>

int main() {
    int i;

    // Print even numbers
    printf("Even numbers from 1 to 100:\n");
    for (i = 2; i <= 100; i += 2) {
        printf("%d ", i);
    }

    // Print a new line for better formatting
    printf("\n");

    // Print odd numbers
    printf("Odd numbers from 1 to 100:\n");
    for (i = 1; i <= 100; i += 2) {
        printf("%d ", i);
    }

    // Print a new line for better formatting
    printf("\n");

    return 0;
}


Write a C program to print Fibonacci series up to n terms.
#include <stdio.h>

int main() {
    int n, first = 0, second = 1, next, i;

    // Input
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    // Print Fibonacci series
    printf("Fibonacci series up to %d terms:\n", n);

    for (i = 0; i < n; ++i) {
        printf("%d, ", first);
        next = first + second;
        first = second;
        second = next;
    }

    printf("\n");

    return 0;
}


Write a C program to calculate and print simple interest for three different set of values to principal
#include <stdio.h>

int main() {
    float principal[3], rate, time, simple_interest;
    int i;

    // Input
    for (i = 0; i < 3; ++i) {
        printf("Enter principal amount for set %d: ", i + 1);
        scanf("%f", &principal[i]);
    }

    printf("Enter the rate of interest (in percentage): ");
    scanf("%f", &rate);

    printf("Enter the time (in years): ");
    scanf("%f", &time);

    // Calculate and print simple interest for each set
    for (i = 0; i < 3; ++i) {
        simple_interest = (principal[i] * rate * time) / 100;
        printf("Simple Interest for set %d: %.2f\n", i + 1, simple_interest);
    }

    return 0;
}


Write a C program to calculate the sum of following series using function. Sum = 1 + 1/x + 1/x2 + 1/x3 + 1/x4 +…………
#include <stdio.h>

// Function to calculate the sum of the series
double calculateSum(int x, int n) {
    double sum = 0;
    int i;
    
    for (i = 0; i < n; ++i) {
        sum += 1.0 / pow(x, i);
    }

    return sum;
}

int main() {
    int x, n;

    // Input
    printf("Enter the value of x: ");
    scanf("%d", &x);

    printf("Enter the number of terms (n): ");
    scanf("%d", &n);

    // Calculate and print the sum using the function
    double result = calculateSum(x, n);
    printf("Sum of the series: %lf\n", result);

    return 0;
}


Write a 'C' program to convert decimal number to binary number. (using function). 
#include <stdio.h>

// Function to convert decimal to binary
void decimalToBinary(int decimalNumber) {
    int binary[32];
    int i = 0;

    // Convert decimal to binary
    while (decimalNumber > 0) {
        binary[i] = decimalNumber % 2;
        decimalNumber /= 2;
        i++;
    }

    // Print binary representation in reverse order
    printf("Binary representation: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binary[j]);
    }
    printf("\n");
}

int main() {
    int decimalNumber;

    // Input
    printf("Enter a decimal number: ");
    scanf("%d", &decimalNumber);

    // Call the function to convert and print binary representation
    decimalToBinary(decimalNumber);

    return 0;
}


Write a C program to accept a number and check whether it is perfect or not.(using function)
#include <stdio.h>

// Function to check if a number is perfect
int isPerfect(int number) {
    int sum = 0;

    // Find divisors and calculate sum
    for (int i = 1; i < number; ++i) {
        if (number % i == 0) {
            sum += i;
        }
    }

    // Check if the number is perfect
    return (sum == number);
}

int main() {
    int num;

    // Input
    printf("Enter a number: ");
    scanf("%d", &num);

    // Check if the number is perfect using the function
    if (isPerfect(num)) {
        printf("%d is a perfect number.\n", num);
    } else {
        printf("%d is not a perfect number.\n", num);
    }

    return 0;
}


Write a C Program to calculate factorial of given number by using recursion.
#include <stdio.h>

// Function to calculate factorial using recursion
unsigned long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int num;

    // Input
    printf("Enter a number: ");
    scanf("%d", &num);

    // Check if the number is non-negative
    if (num < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        // Calculate and print the factorial using the recursive function
        printf("Factorial of %d = %llu\n", num, factorial(num));
    }

    return 0;
}


Write a function which uses recursion to find the GCD of given two 
integers. Take the input from user.

#include <stdio.h>

// Function to find GCD using recursion
int findGCD(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return findGCD(b, a % b);
    }
}

int main() {
    int num1, num2;

    // Input
    printf("Enter the first integer: ");
    scanf("%d", &num1);

    printf("Enter the second integer: ");
    scanf("%d", &num2);

    // Calculate and print the GCD using the recursive function
    int gcd = findGCD(num1, num2);
    printf("GCD of %d and %d is: %d\n", num1, num2, gcd);

    return 0;
}


Given two integers x and n, write a function to compute x^n using 
recursion. We may assume that x and n are small and overflow 
doesn’t happen. Take input from user.
#include <stdio.h>

// Function to compute x^n using recursion
double power(int x, int n) {
    if (n == 0) {
        return 1;
    } else if (n > 0) {
        return x * power(x, n - 1);
    } else {
        // For negative exponent, compute reciprocal
        return 1.0 / (x * power(x, -n - 1));
    }
}

int main() {
    int base, exponent;

    // Input
    printf("Enter the base (x): ");
    scanf("%d", &base);

    printf("Enter the exponent (n): ");
    scanf("%d", &exponent);

    // Calculate and print x^n using the recursive function
    double result = power(base, exponent);
    printf("%d^%d = %.4lf\n", base, exponent, result);

    return 0;
}


Write a function that computes Fibonacci numbers using 
recursion. Take input from user.
#include <stdio.h>

// Function to compute Fibonacci number using recursion
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int terms;

    // Input
    printf("Enter the number of terms in the Fibonacci series: ");
    scanf("%d", &terms);

    // Print Fibonacci series using the recursive function
    printf("Fibonacci series up to %d terms:\n", terms);
    for (int i = 0; i < terms; ++i) {
        printf("%d ", fibonacci(i));
    }

    return 0;
}


Write a function that computes the combinations of possibilities of 
‘r’ selections out of ‘n’ objects recursively.
#include <stdio.h>

// Function to compute combinations using recursion
unsigned long long combinations(int n, int r) {
    if (r == 0 || r == n) {
        return 1;
    } else {
        return combinations(n - 1, r - 1) + combinations(n - 1, r);
    }
}

int main() {
    int n, r;

    // Input
    printf("Enter the value of n: ");
    scanf("%d", &n);

    printf("Enter the value of r: ");
    scanf("%d", &r);

    // Check if n and r are non-negative and r <= n
    if (n < 0 || r < 0 || r > n) {
        printf("Invalid input. Ensure n >= 0, r >= 0, and r <= n.\n");
    } else {
        // Calculate and print combinations using the recursive function
        unsigned long long result = combinations(n, r);
        printf("C(%d, %d) = %llu\n", n, r, result);
    }

    return 0;
}


Write a program in C to read n number of values in an array and display them in reverse order. 
#include <stdio.h>

int main() {
    int n;

    // Input: Read the number of elements
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // Check if n is non-negative
    if (n < 0) {
        printf("Invalid input. Please enter a non-negative value for n.\n");
        return 1; // Return 1 to indicate an error
    }

    // Declare an array of size n
    int arr[n];

    // Input: Read values into the array
    printf("Enter %d values:\n", n);
    for (int i = 0; i < n; ++i) {
        printf("Value %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Display values in reverse order
    printf("Values in reverse order:\n");
    for (int i = n - 1; i >= 0; --i) {
        printf("%d ", arr[i]);
    }

    printf("\n");

    return 0;
}


34.  WAP to enter 2D matrices and perform multiplication operation between them.
#include<stdio.h>
int main(){
      // input rows and columns
    int m;
    printf("enter m : ");
    scanf("%d",&m);

     int n;
    printf("enter n : ");
    scanf("%d",&n);

     int r;
    printf("enter r : ");
    scanf("%d",&r);
   
    //input element

    // 1st matrix element
     int arr[m][n];
    for(int i=0; i<m;i++){
        for(int j=0; j<n; j++){
            scanf("%d",&arr[i][j]);
        }
    }
    // 2nd matrix element
       int brr[n][r];
    printf("\n");
     for(int i=0; i<n;i++){
        for(int j=0; j<r; j++){
            scanf("%d",&brr[i][j]);
        }
    }
    // resultant matrix
    int crr[m][r];

    printf("\n");

    for(int i=0; i<m; i++){
        for(int j=0; j<r; j++){
            int sum=0;
            for(int k=0; k<n; k++){
                sum = sum + arr[i][k]*brr[k][j];
            }
            crr[i][j] = sum; // store bhi kar liya
            printf("%d ",sum);
        }
        printf("\n");
    }
    printf("\n");

   // output

    for(int i=0; i<m; i++){
        for(int j=0; j<r; j++){
           printf("%d ",crr[i][j]);
        }
        printf("\n");
    }

    return 0;
}


32. WAP to add two numbers using recursion.
#include<stdio.h>

// Function to add two numbers recursively
int add_recursive(int a, int b) {
    // Base case: if the second number is 0, return the first number
    if (b == 0) {
        return a;
    } else {
        // Recursive case: add 1 to the first number and decrement the second number
        return add_recursive(a + 1, b - 1);
    }
}

int main() {
    // Input two numbers
    int num1, num2;
    printf("Enter the first number: ");
    scanf("%d", &num1);
    printf("Enter the second number: ");
    scanf("%d", &num2);

    // Call the recursive function to add the two numbers
    int result = add_recursive(num1, num2);

    // Display the result
    printf("The sum of %d and %d is: %d\n", num1, num2, result);

    return 0;
}


WAP to enter 2D matrices and perform the following operations.
A. Matrix addition
#include <stdio.h>

// Function to add two matrices
void addMatrices(int firstMatrix[10][10], int secondMatrix[10][10], int result[10][10], int rows, int columns) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            result[i][j] = firstMatrix[i][j] + secondMatrix[i][j];
        }
    }
}

// Function to display a matrix
void displayMatrix(int matrix[10][10], int rows, int columns) {
    printf("Resultant Matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int firstMatrix[10][10], secondMatrix[10][10], result[10][10];
    int rows, columns;

    // Input matrix dimensions
    printf("Enter the number of rows and columns for the matrices: ");
    scanf("%d %d", &rows, &columns);

    // Input elements of the first matrix
    printf("Enter the elements of the first matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%d", &firstMatrix[i][j]);
        }
    }

    // Input elements of the second matrix
    printf("Enter the elements of the second matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%d", &secondMatrix[i][j]);
        }
    }

    // Call the function to add matrices
    addMatrices(firstMatrix, secondMatrix, result, rows, columns);

    // Display the resultant matrix
    displayMatrix(result, rows, columns);

    return 0;
}

. Matrix substraction
#include <stdio.h>

// Function to subtract two matrices
void subtractMatrices(int firstMatrix[10][10], int secondMatrix[10][10], int result[10][10], int rows, int columns) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            result[i][j] = firstMatrix[i][j] - secondMatrix[i][j];
        }
    }
}

// Function to display a matrix
void displayMatrix(int matrix[10][10], int rows, int columns) {
    printf("Resultant Matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int firstMatrix[10][10], secondMatrix[10][10], result[10][10];
    int rows, columns;

    // Input matrix dimensions
    printf("Enter the number of rows and columns for the matrices: ");
    scanf("%d %d", &rows, &columns);

    // Input elements of the first matrix
    printf("Enter the elements of the first matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%d", &firstMatrix[i][j]);
        }
    }

    // Input elements of the second matrix
    printf("Enter the elements of the second matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("Enter element [%d][%d]: ", i, j
            scanf("%d", &secondMatrix[i][j]);
        }
    }

    // Call the function to subtract matrices
    subtractMatrices(firstMatrix, secondMatrix, result, rows, columns);

    // Display the resultant matrix
    displayMatrix(result, rows, columns);

    return 0;
}



TRANSPOSE 
#include <stdio.h>

// Function to find the transpose of a matrix
void transposeMatrix(int matrix[10][10], int transpose[10][10], int rows, int columns) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            transpose[j][i] = matrix[i][j];
        }
    }
}

// Function to display a matrix
void displayMatrix(int matrix[10][10], int rows, int columns) {
    printf("Matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int matrix[10][10], transpose[10][10];
    int rows, columns;

    // Input matrix dimensions
    printf("Enter the number of rows and columns for the matrix: ");
    scanf("%d %d", &rows, &columns);

    // Input elements of the matrix
    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%d", &matrix[i][j]);
        }
    }

    // Call the function to find the transpose
    transposeMatrix(matrix, transpose, rows, columns);

    // Display the original matrix
    printf("Original ");
    displayMatrix(matrix, rows, columns);

    // Display the transpose matrix
    printf("Transpose ");
    displayMatrix(transpose, columns, rows);

    return 0;
}

Write a program in C to read n number of values in an array and display them in reverse order. 
#include <stdio.h>

int main() {
    int n;

    // Input the number of elements in the array
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];

    // Input array elements
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; ++i) {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Display array elements in reverse order
    printf("Array elements in reverse order:\n");
    for (int i = n - 1; i >= 0; --i) {
        printf("%d\n", arr[i]);
    }

    return 0;
}








