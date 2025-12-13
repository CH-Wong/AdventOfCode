#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define NUM_INPUT_ROWS 4

int main() {
    FILE *file = fopen("./inputs/day6.txt", "r");
    if (file == NULL) {
        printf("Could not open input file\n");
        return 1;
    }
    
    int num_counter = 0;
    char line[4096];
    int num;
    int n;

    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';
        char *ptr = line;  // Create a moving pointer
    
        while (sscanf(ptr, "%d%n", &num, &n) == 1) {
            num_counter++;
            ptr += n;  // <-- Move pointer forward!
        }
        // Only count the numbers in the first line.
        break;
    }
    rewind(file);
    
    printf("Numbers per line: %d\n", num_counter);
    
    // Dynamically allocate 2D array
    int **input_numbers = malloc(NUM_INPUT_ROWS * sizeof(int *));
    for (int i = 0; i < NUM_INPUT_ROWS; i++) {
        input_numbers[i] = malloc(num_counter * sizeof(int));
    }

    // Allocate operators array
    char *operators = malloc(num_counter + 1);  // +1 for null terminator if needed
    
    int cur_row = 0;
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';
        // strtok modifies the original string
        char *token = strtok(line, " \t\n\r");  // Space, tab, newline, carriage return
        
        int cur_col = 0;
        while (token != NULL && cur_col < num_counter) {

            if (cur_row < NUM_INPUT_ROWS) {
                input_numbers[cur_row][cur_col] = atoi(token);
            } else {
                operators[cur_col] = token[0];
            }
            cur_col++;
            token = strtok(NULL, " \t\n\r");
        }
        cur_row++;
    }
    operators[num_counter] = '\0'; 
    fclose(file);

    for (int i = 0; i < NUM_INPUT_ROWS; i++) {
        for (int j = 0; j < num_counter; j++) {
            printf("%d ", input_numbers[i][j]);
        }
        printf("\n");
    }

    printf("%s\n\n\n", operators);

    long long grand_total = 0;
    for (int j = 0; j < num_counter; j++) {
        long long result;
        if (operators[j] == '+') {
            result = 0;
            for (int i = 0; i < NUM_INPUT_ROWS; i++) {
                printf("%d ", input_numbers[i][j]);

                result += input_numbers[i][j];
            }
        } else if (operators[j] == '*') {
            result = 1;
            for (int i = 0; i < NUM_INPUT_ROWS; i++) {
                printf("%d ", input_numbers[i][j]);
                result *= input_numbers[i][j];
            }
        } else {
            printf("ERROR: UNKNOWN OPERATOR");
            return EXIT_FAILURE;
        }
        printf("%c",operators[j]);

        printf("\n");
        printf("Result: %lld\n", result);
        grand_total += result;
    }
    
    printf("\nGrand Total: %lld\n", grand_total);

}