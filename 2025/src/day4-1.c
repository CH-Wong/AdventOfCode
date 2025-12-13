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
    int **map = malloc(num_rows * sizeof(int *));
    for (int i = 0; i < num_rows; i++) {
        map[i] = malloc(num_cols * sizeof(int));
    }
    
    // Initialize all to 0
    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            map[i][j] = 0;
        }
    }

    // Second pass: populate the array
    int cur_row = 0;
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';
        
        for (int cur_col = 0; cur_col < num_cols; cur_col++) {
            if (line[cur_col] == '@') {
                map[cur_row][cur_col] = 1;
            }
        }
        cur_row++;
    }
    fclose(file);
    
    int accessible_rolls = 0;
    // Print the map
    for (int cur_row = 0; cur_row < num_rows; cur_row++) {
        for (int cur_col = 0; cur_col < num_cols; cur_col++) {
            int adjacent_roll_count = 0;
            if (map[cur_row][cur_col] == 1) {
                if (cur_col + 1 < num_cols && map[cur_row][cur_col+1] == 1){
                    adjacent_roll_count++;
                    // printf("a");
                }
                if (cur_col - 1 >= 0 && map[cur_row][cur_col-1] == 1) {
                    adjacent_roll_count++;
                    // printf("b");
                }
                if (cur_row + 1 < num_rows && map[cur_row+1][cur_col] == 1) {
                    adjacent_roll_count++;
                    // printf("c");
                }
                if (cur_row - 1 >= 0 && map[cur_row-1][cur_col] == 1) {
                    adjacent_roll_count++;
                    // printf("d");
                }
                if (cur_row + 1 < num_rows && cur_col + 1 < num_cols && map[cur_row+1][cur_col+1] == 1) {
                    adjacent_roll_count++;
                    // printf("e");
                }
                if (cur_row - 1 >= 0 && cur_col + 1 < num_cols && map[cur_row-1][cur_col+1] == 1) {
                    adjacent_roll_count++;
                    // printf("f");
                }
                if (cur_row + 1 < num_rows && cur_col -1 >= 0 && map[cur_row+1][cur_col-1] == 1) {
                    adjacent_roll_count++;
                    // printf("g");
                }
                if (cur_row - 1 >= 0 && cur_col - 1 >= 0 && map[cur_row-1][cur_col-1] == 1) {
                    adjacent_roll_count++;
                    // printf("h");
                } 
                if (adjacent_roll_count < 4) {
                    accessible_rolls++;
                    printf("x");
                } else {
                    printf("%d",adjacent_roll_count);
                }
            } else {
                printf(".");
            }

        }
        printf("\n");
    }
    
    // Free allocated memory
    for (int i = 0; i < num_rows; i++) {
        free(map[i]);
    }
    free(map);

    printf("Accessible Rolls: %d", accessible_rolls);

    return 0; // indicates succesful function, can also return EXIT_SUCCESS or EXIT_FAILURE
}