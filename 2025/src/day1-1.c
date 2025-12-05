#include <stdio.h>
#include <stdlib.h>

#define INPUT_FILE "inputs/day1.txt"
const int STARTING_DIAL = 50;


int main() {
    printf("Hello Advent of Code 2025!\n");
    
    // Example: Read from file
    FILE *file = fopen("./inputs/day1.txt", "r");
    if (file == NULL) {
        printf("Could not open input file\n");
        return 1;
    }
    
    // Initialize variables. 
    int dial_setting = STARTING_DIAL;
    int zero_counter = 0;
    
    char line[10]; // Needs to be atleast five because the line contains a newline and a null terminator.
    while (fgets(line, sizeof(line), file)) {
        printf("Dial setting: %d\n", dial_setting);
        
        // Identify left/right
        int direction;        
        if (line[0] == 'R') {
            direction = 1;
        }
        else if (line[0] == 'L') {
            direction = -1;
        }
        else {
            fprintf(stderr, "Unexpected error: Invalid direction '%c'\n", line[0]);
            exit(EXIT_FAILURE);
        }
        
        
        // get number of turns required.
        int turns_required = atoi(line+1);
        
        // turn dial
        dial_setting += direction*turns_required;
        dial_setting = ((dial_setting % 100) + 100) % 100;
        // Count 0's.
        
        if (dial_setting == 0) {
            zero_counter += 1;
        }
        
        // printf("\tRead: %s", line);
        // printf("\tDirection: %d\n", direction);
        // printf("\tTurns required: %d\n", turns_required);
    }
    
    printf("Zero counter: %d\n", zero_counter);
    fclose(file);

    // printf("%d", zero_counter)
    return 0; // indicates succesful function, can also return EXIT_SUCCESS or EXIT_FAILURE
}