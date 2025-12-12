#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *file = fopen("./inputs/day3.txt", "r");
    if (file == NULL) {
        printf("Could not open input file\n");
        return 1;
    }
    
    // Initialize variables. 

    int output_joltage = 0;
    char line[110]; // Needs to be atleast five because the line contains a newline and a null terminator.
    while (fgets(line, sizeof(line), file)) {
    // Remove newline character if present
        line[strcspn(line, "\n")] = '\0';
        printf("Bank: %s\n", line);        int highest_jolt = 0;
        int highest_jolt_ind=0;
        int current_jolt; 
        int line_length = strlen(line);
        printf("Final number: %c\n", line[line_length-1]);
        // Skip the last number (line_length-2), because if we take the last number, no second number can be chosen!
        for (int i = 0; i < line_length-1; i++) {
            current_jolt = line[i] - '0'; // Using ASCII trick!!
            if (current_jolt > highest_jolt) {
                highest_jolt = current_jolt;
                highest_jolt_ind = i;
            } 
        }
        // printf("Found highest: %d, %d\n", highest_jolt, highest_jolt_ind);
        
        int second_highest_jolt = 0;
        for (int j = highest_jolt_ind+1; j < line_length; j++) {
            current_jolt = line[j] - '0'; // Using ASCII trick!!
            if (current_jolt > second_highest_jolt) {
                second_highest_jolt = current_jolt;
            } 
        }
        output_joltage += highest_jolt*10 + second_highest_jolt;
        printf("jolts: %d%d\n",highest_jolt, second_highest_jolt);

    }
    fclose(file);

    printf("Output Joltage: %d", output_joltage);
    return 0; // indicates succesful function, can also return EXIT_SUCCESS or EXIT_FAILURE
}