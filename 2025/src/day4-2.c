#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BATTERIES 12

int main() {
    FILE *file = fopen("./inputs/day4.txt", "r");
    if (file == NULL) {
        printf("Could not open input file\n");
        return 1;
    }
    
    // Initialize variables. 
    char line[200]; // Needs to be atleast five because the line contains a newline and a null terminator.
    int num_cols;
    int num_rows=0;
    while (fgets(line, sizeof(line), file)) {
        // Remove newline character if present
        line[strcspn(line, "\n")] = '\0';
        printf("%s\n", line);  
        if (num_rows == 0) {
            // First line determines column count
            num_cols = strlen(line);
        }  
        num_rows++;
    }
    printf("num_cols: %d\nnum_rows: %d\n", num_cols, num_rows);
    rewind(file);
    
    // Dynamically allocate 2D array
    int **current_map = malloc((num_rows+2) * sizeof(int *));
    int **next_map = malloc((num_rows+2) * sizeof(int *));
    for (int i = 0; i < num_rows+2; i++) {
        current_map[i] = malloc((num_cols+2) * sizeof(int));
        next_map[i] = malloc((num_cols+2) * sizeof(int));
    }

    
    // Create an empty layer of padding to make sure we don't go out-of-bounds when checking neighbours later.
    // Initialize all to 0: edges donot count as rolls.
    for (int i = 0; i < num_rows+2; i++) {
        for (int j = 0; j < num_cols+2; j++) {
            current_map[i][j] = 0;
        }
    }

    // Second pass: populate the array
    // We start at row 1 because first row is a empty buffer row
    int cur_row = 1;
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';
        
        for (int cur_col = 1; cur_col < num_cols+1; cur_col++) {
            if (line[cur_col-1] == '@') {
                current_map[cur_row][cur_col] = 1;
            }
        }
        cur_row++;
    }
    fclose(file);
    
    int accessible_rolls = 1;
    int rolls_removed = 0;
    while (accessible_rolls > 0) {
        accessible_rolls = 0;
        // Loop through each position and see if roll can be removed.
        for (int cur_row = 0; cur_row < num_rows+2; cur_row++) {
            for (int cur_col = 0; cur_col < num_cols+2; cur_col++) {
                int adjacent_roll_count;
                // with the buffer, we can simply count up all the adjacent fields to find the number 
                if (current_map[cur_row][cur_col] == 1) {
                    adjacent_roll_count = current_map[cur_row+1][cur_col] 
                                        + current_map[cur_row+1][cur_col+1] 
                                        + current_map[cur_row][cur_col+1] 
                                        + current_map[cur_row-1][cur_col+1] 
                                        + current_map[cur_row-1][cur_col] 
                                        + current_map[cur_row-1][cur_col-1] 
                                        + current_map[cur_row][cur_col-1] 
                                        + current_map[cur_row+1][cur_col-1];

                    if (adjacent_roll_count < 4) {
                        accessible_rolls++;
                        next_map[cur_row][cur_col] = 0;
                        // printf("x");
                    } else {
                        // printf("%d",adjacent_roll_count);
                        next_map[cur_row][cur_col] = 1;
                    }
                } else {
                    next_map[cur_row][cur_col] = 0;
                    // printf(".");
                }

            }
            // printf("\n");
        }
        // Swap pointers (FAST - no copying!)
        int **temp = current_map;
        current_map = next_map;
        next_map = temp;
        printf("Accessible Rolls: %d\n", accessible_rolls);
        rolls_removed += accessible_rolls;
        printf("Rolls removed so far:%d\n", rolls_removed);

    }

    // Free allocated memory
    for (int i = 0; i < num_rows+2; i++) {
        free(current_map[i]);
        free(next_map[i]);
    }
    free(current_map);
    free(next_map);

    return EXIT_SUCCESS; // indicates succesful function, can also return EXIT_SUCCESS or EXIT_FAILURE
}