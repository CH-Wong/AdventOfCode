#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main() {
    FILE *file = fopen("./inputs/day5.txt", "r");
    if (file == NULL) {
        printf("Could not open input file\n");
        return 1;
    }
    
    typedef struct {
        long long start;
        long long end;
    } Range;

    Range *ranges = NULL;
    int range_count = 0;
    char line[64];

    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';
        
        if (strlen(line) == 0) break;
        
        Range r;
        if (sscanf(line, "%lld-%lld", &r.start, &r.end) == 2) {
            // Resize array
            ranges = realloc(ranges, (range_count + 1) * sizeof(Range));
            
            // Store the range
            ranges[range_count] = r;
            range_count++;
        }
    }
    for (int i = 0; i < range_count; i++) {
        printf("%lld - %lld\n",ranges[i].start, ranges[i].end);
    }

    long long cur_num;
    int fresh_count = 0;
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';

        if (sscanf(line, "%lld", &cur_num) == 1) {
            printf("%lld", cur_num);
            for (int i = 0; i < range_count; i++) {
                if (cur_num >= ranges[i].start && cur_num <= ranges[i].end) {
                    fresh_count++;
                    printf("Fresh!");
                    break;
                } 
            }
            printf("\n");
        }
    }

    fclose(file);
    printf("Fresh Product Count: %d", fresh_count);

}