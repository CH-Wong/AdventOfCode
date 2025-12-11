#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

char* read_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Error opening file");
        return NULL;
    }
    
    // Determine file size
    fseek(file, 0, SEEK_END);  // Move to end of file
    long file_size = ftell(file);  // Get position (which is file size)
    fseek(file, 0, SEEK_SET);  // Reset to beginning
    
    // Allocate memory (plus 1 for null terminator)
    char* buffer = (char*)malloc(file_size + 1);
    if (!buffer) {
        fclose(file);
        perror("Memory allocation failed");
        return NULL;
    }
    
    // Read file into buffer
    size_t bytes_read = fread(buffer, 1, file_size, file);
    buffer[bytes_read] = '\0';  // Null-terminate
    
    fclose(file);
    return buffer;
}


// Use long long for large numbers
long long get_first_digits(long long num, int n) {
    if (num == 0 || n <= 0) return 0;
    if (num < 0) num = -num;
    
    // Count digits without log10
    long long temp = num;
    int total_digits = 0;
    while (temp > 0) {
        temp /= 10;
        total_digits++;
    }
    
    if (n >= total_digits) return num;
    
    // Calculate divisor
    long long divisor = 1;
    for (int i = 0; i < total_digits - n; i++) {
        divisor *= 10;
    }
    
    return num / divisor;
}

long long get_last_digits(long long num, int n) {
    if (n <= 0) return 0;
    if (num < 0) num = -num;
    
    long long divisor = 1;
    for (int i = 0; i < n; i++) {
        divisor *= 10;
    }
    
    return num % divisor;
}

int count_digits(long long num) {
    if (num == 0) return 1;
    int count = 0;
    while (num > 0) {
        num /= 10;
        count++;
    }
    return count;
}


long long raise_to_power(long num, int power) {
    int i;
    long long result = num;
    for (i = 0; i < power; i++) {
        result = result * 10;
    }
    return result;
}

int main() {
    char* content = read_file("./inputs/day2.txt");
    char *range;
    long long start, end;
    long long sum_matching_numbers = 0;

    if (content) {
        printf("File content:\n%s\n", content);
        // First call with the string
        range = strtok(content, ",");
        
        // Subsequent calls with NULL
        while (range != NULL) {
            // sscanf parses formatted input
            if (sscanf(range, "%lld-%lld", &start, &end) == 2) {
                printf("Start: %lld, End: %lld\n", start, end);
            } else {
                printf("Failed to parse\n");
            }

            long long number;
            for (number=start; number<end+1; number++) {
                // printf("number: %lld\n", number);
                int num_digits = count_digits(number);
                // printf("n_digits: %d\n", num_digits);
                
                int split;
                for (split=1; split <= num_digits/2; split++){
                    long long check_number = number;
                    long last_digits;
                    if (num_digits%split == 0){
                        last_digits = get_last_digits(number, split);
                        // printf("last digits:%ld\n", last_digits);

                        int power;
                        for (power=0; power < num_digits; power += split) {
                            check_number -= raise_to_power(last_digits, power);
                        }
                        // printf("Check number result: %lld\n",check_number);
                        if (check_number == 0) {
                            sum_matching_numbers += number;
                            // printf("\tMatching Number: %lld\n", number);
                            break;
                        }
                    }
                }


            }
            range = strtok(NULL, ",");
        }
        free(content);  // Don't forget to free!
    }
    printf("Sum of matching numbers: %lld", sum_matching_numbers);

}