#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BATTERIES 12

int main() {
    FILE *file = fopen("./inputs/day3.txt", "r");
    if (file == NULL) {
        printf("Could not open input file\n");
        return 1;
    }
    
    // Initialize variables. 

    long long output_joltage = 0;
    char line[110]; // Needs to be atleast five because the line contains a newline and a null terminator.
    while (fgets(line, sizeof(line), file)) {
    // Remove newline character if present
        line[strcspn(line, "\n")] = '\0';
        printf("Bank: %s\n", line);        
        int battery_joltages[MAX_BATTERIES] = {0};
        int highest_jolt_ind = 0;
        int line_length = strlen(line);

        for (int battery_index = MAX_BATTERIES-1; battery_index >= 0; battery_index--){
            int current_jolt; 
            // Skip the last number (line_length-2), because if we take the last number, no second number can be chosen!
            for (int i = highest_jolt_ind; i < line_length-battery_index; i++) {
                current_jolt = line[i] - '0'; // Using ASCII trick!!
                if (current_jolt > battery_joltages[battery_index]) {
                    battery_joltages[battery_index] = current_jolt;
                    highest_jolt_ind = i+1;
                } 
            }

        } 
        
        long long power = 1;
        int length = sizeof(battery_joltages) / sizeof(battery_joltages[0]);  // Best practice

        for (int i = length-1; i >=0; i--) {
            printf("%d ", battery_joltages[i]);
        }
        printf("\n");

        for (int i = 0; i < length; i++) {
            output_joltage += battery_joltages[i]*power;
            power *= 10;
        }
        printf("Output Joltage: %lld\n", output_joltage);

    }
    fclose(file);

    printf("Output Joltage: %lld\n", output_joltage);
    return 0; // indicates succesful function, can also return EXIT_SUCCESS or EXIT_FAILURE
}