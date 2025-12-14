#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define NUM_INPUT_ROWS 5

int main() {
    FILE *file = fopen("./inputs/day6.txt", "r");
    if (file == NULL) {
        printf("Could not open input file\n");
        return EXIT_FAILURE;
    }
        
    char **input_data = malloc(NUM_INPUT_ROWS * sizeof(char *));
    for (int i = 0; i < NUM_INPUT_ROWS; i++) {
        input_data[i] = malloc(4096 * sizeof(char));
    }
        
    char line[4096];
    int line_num = 0;
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';
        strcpy(input_data[line_num], line);
        line_num++;
    }
    fclose(file);

    long long grand_total = 0;
    char number_string[NUM_INPUT_ROWS+1];
    char operator = '@';
    long long result = 0;
    int cur_num;
    int line_length = strlen(input_data[0]);
    for (int cur_col = 0; cur_col < line_length; cur_col++) {
        // Recognize a blank space where all lines are spaces. This means a new set of operations are here.
        // Count the blanks. 
        int blanks = 0;
        for (int cur_row = 0; cur_row < NUM_INPUT_ROWS; cur_row++){
            if (input_data[cur_row][cur_col] == ' '){
                blanks++;
            }
        }
        // If indeed all lines are blank at this column, reset variables and continue
        if (blanks == NUM_INPUT_ROWS) {
            grand_total += result;
            operator = '@';

            printf("Result: %lld\n", result);
            printf("Grand Total: %lld\n\n", grand_total);
            continue;
        }
        
        // This should only run once for a new operation. 
        if (operator == '@') {
            if (input_data[NUM_INPUT_ROWS-1][cur_col] == '*') {
                result = 1; 
                operator = '*';
            } else if (input_data[NUM_INPUT_ROWS-1][cur_col] == '+') {
                result = 0;
                operator = '+';
            } else {
                printf("ERROR: UNKNOWN OPERATOR\n");
                return EXIT_FAILURE;
            }
            printf("Found operator: %c\n", operator);
        }

        for (int cur_row = 0; cur_row < NUM_INPUT_ROWS-1; cur_row++){
            printf("%c", input_data[cur_row][cur_col]);
            number_string[cur_row] = input_data[cur_row][cur_col];
        }
        printf("Number_found: %s, ", number_string);
        cur_num = atoi(number_string);
        if (operator == '*') {
            printf("%d\n", cur_num);
            result *= cur_num;
        } else if (operator == '+') {
            printf("%d\n", cur_num);
            result += cur_num;
        } else {
            printf("ERROR: UNKNOWN OPERATOR\n");
            return EXIT_FAILURE;
        }            
        for (int i = 0; i < NUM_INPUT_ROWS+1; i++) {
            number_string[i] = '\0';
        }
    }
    grand_total += result;
    printf("\nGrand Total: %lld\n", grand_total);
}