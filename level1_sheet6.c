#include <stdio.h>

int main() {
    int choice, n, m, i, j, k;

    printf("Enter your choice (1 to 25): ");
    scanf("%d", &choice);

    printf("Enter value of N: ");
    scanf("%d", &n);

    printf("Enter value of M (if needed): ");
    scanf("%d", &m);

    switch(choice) {

        // Problem 1: Square Pattern 4x4
        case 1:
            for(i=0;i<4;i++){
                for(j=0;j<4;j++) printf("* ");
                printf("\n");
            }
            break;

        // Problem 2: Rectangle M x N
        case 2:
            for(i=0;i<m;i++){
                for(j=0;j<n;j++) printf("* ");
                printf("\n");
            }
            break;

        // Problem 3: Right Triangle Stars Increasing
        case 3:
            for(i=1;i<=n;i++){
                for(j=1;j<=i;j++) printf("* ");
                printf("\n");
            }
            break;

        // Problem 4: Right Triangle Numbers
        case 4:
            for(i=1;i<=n;i++){
                for(j=1;j<=i;j++) printf("%d ", j);
                printf("\n");
            }
            break;

        // Problem 5: Same Number Each Row
        case 5:
            for(i=1;i<=n;i++){
                for(j=1;j<=i;j++) printf("%d ", i);
                printf("\n");
            }
            break;

        // Problem 6: N Stars in One Line
        case 6:
            for(i=0;i<n;i++) printf("* ");
            break;

        // Problem 7: N x N Stars
        case 7:
            for(i=0;i<n;i++){
                for(j=0;j<n;j++) printf("* ");
                printf("\n");
            }
            break;

        // Problem 8: Inverted Triangle Stars
        case 8:
            for(i=n;i>=1;i--){
                for(j=1;j<=i;j++) printf("* ");
                printf("\n");
            }
            break;

        // Problem 9: Column Pattern Numbers
        case 9:
            for(i=1;i<=n;i++){
                for(j=1;j<=n;j++) printf("%d ", i);
                printf("\n");
            }
            break;

        // Problem 10: 1 to N, N times
        case 10:
            for(i=1;i<=n;i++){
                for(j=1;j<=n;j++) printf("%d ", j);
                printf("\n");
            }
            break;

        // Problem 11: Continuous Numbers Triangle
        case 11:
            k = 1;
            for(i=1;i<=n;i++){
                for(j=1;j<=i;j++) printf("%d ", k++);
                printf("\n");
            }
            break;

        // Problem 12: Reverse Numbers
        case 12:
            for(i=1;i<=n;i++){
                for(j=i;j>=1;j--) printf("%d ", j);
                printf("\n");
            }
            break;

        // Problem 13: Alphabet Pattern
        case 13:
            for(i=1;i<=n;i++){
                for(j=1;j<=i;j++) printf("A ");
                printf("\n");
            }
            break;

        // Problem 14: Multiplication Table Grid
        case 14:
            for(i=1;i<=4;i++){
                for(j=1;j<=4;j++) printf("%d ", i*j);
                printf("\n");
            }
            break;

        // Problem 15: Horizontal Stars
        case 15:
            for(i=0;i<n;i++) printf("* ");
            break;

        // Problem 16: Vertical Stars
        case 16:
            for(i=0;i<n;i++) printf("*\n");
            break;

        // Problem 17: Hollow Square
        case 17:
            for(i=1;i<=n;i++){
                for(j=1;j<=n;j++){
                    if(i==1 || i==n || j==1 || j==n)
                        printf("* ");
                    else
                        printf("  ");
                }
                printf("\n");
            }
            break;

        // Problem 18: M rows, 1 to N
        case 18:
            for(i=1;i<=m;i++){
                for(j=1;j<=n;j++) printf("%d ", j);
                printf("\n");
            }
            break;

        // Problem 19: Pyramid
        case 19:
            for(i=1;i<=n;i++){
                for(j=1;j<=n-i;j++) printf(" ");
                for(j=1;j<=2*i-1;j++) printf("*");
                printf("\n");
            }
            break;

        // Problem 20: Continuous Stars (No Space)
        case 20:
            for(i=1;i<=n;i++){
                for(j=1;j<=i;j++) printf("*");
                printf("\n");
            }
            break;

        // Problem 21: Square with Row Numbers
        case 21:
            for(i=1;i<=n;i++){
                for(j=1;j<=n;j++) printf("%d ", i);
                printf("\n");
            }
            break;

        // Problem 22: Inverted Numbers Triangle
        case 22:
            for(i=n;i>=1;i--){
                for(j=1;j<=i;j++) printf("%d ", j);
                printf("\n");
            }
            break;

        // Problem 23: Stars Equal to Row Number
        case 23:
            for(i=1;i<=n;i++){
                for(j=1;j<=i;j++) printf("* ");
                printf("\n");
            }
            break;

        // Problem 24: Diagonal Pattern
        case 24:
            for(i=1;i<=n;i++){
                for(j=1;j<=n;j++){
                    if(i==j) printf("* ");
                    else printf("  ");
                }
                printf("\n");
            }
            break;

        // Problem 25: Plus Pattern
        case 25:
            for(i=1;i<=n;i++){
                for(j=1;j<=n;j++){
                    if(i==n/2+1 || j==n/2+1)
                        printf("* ");
                    else
                        printf("  ");
                }
                printf("\n");
            }
            break;

        default:
            printf("Invalid choice!");
    }

    return 0;
}