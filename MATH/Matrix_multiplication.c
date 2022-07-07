#include<stdio.h>
#include<stdlib.h>

int rows1 = 0;
int columns1 = 0;

int rows2 = 0;
int columns2 = 0;


int multiply(int matrix1[rows1][columns1], int matrix2[columns2][rows2]){

    int i, j, k;
    int final_matrix[rows1][columns2];

    for(i=0; i<rows1; i++){
        for(j=0; j<columns2; j++){
            int sum = 0;
            for(k=0; k<columns1; k++){
                sum += matrix1[i][k]*matrix2[j][k];
            }
            final_matrix[i][j] = sum;
        }
    }

    printf("-------------------------------------------\n");
    printf("\n");

    for(i=0; i<rows1; i++){
        for(j=0; j<columns2; j++){
            printf(" %d ", final_matrix[i][j]);
        }
        printf("\n");
        printf("\n");
    }

    printf("-------------------------------------------\n");

    return 0;
}


int main(){
    printf("-------------------------------------------\n");
    printf("\n");
    printf("Enter dimensions of the matrix-1\n");
    printf("rows columns: ");
    scanf("%d %d", &rows1, &columns1);
    printf("\n");

    printf("-------------------------------------------\n");

    printf("\n");
    printf("Enter dimensions of the matrix-2\n");
    printf("rows columns: ");
    scanf("%d %d", &rows2, &columns2);
    printf("\n");

    printf("-------------------------------------------\n");


    int ar[rows1][columns1], ar2[rows2][columns2], mat[columns2][rows2];
    int i, k, j;

    if(columns1 != rows2){
        printf("Illegal dimentions for multiplication\n");
        printf("-------------------------------------------\n");

        exit(0);
    }

    printf("Please enter contents for first matrix\n");
    printf("\n");
    for(i=0; i<rows1; i++){
        printf("row %d - ", i+1);
        for(k=0; k<columns1; k++){
            scanf("%d", &ar[i][k]);
        }
        printf("\n");
    }

    printf("-------------------------------------------\n");

    printf("Please enter contents for second matrix\n");
    printf("\n");
    for(i=0; i<rows2; i++){
        printf("row %d - ", i+1);
        for(k=0; k<columns2; k++){
            scanf("%d", &ar2[i][k]);
        }
        printf("\n");
    }

    printf("-------------------------------------------\n");

    for(i=0; i<columns2; i++){
        for(j=0; j<rows2; j++){
            mat[i][j] = ar2[j][i];
        }
    }

    multiply(ar, mat);

}