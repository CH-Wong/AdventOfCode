#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct {
    long long start;
    long long end;
} Range;

// Comparison function for qsort (ascending by start)
int compareByStart(const void* a, const void* b) {
    const Range* rangeA = (const Range*)a;
    const Range* rangeB = (const Range*)b;
    
    if (rangeA->start < rangeB->start) return -1;
    if (rangeA->start > rangeB->start) return 1;
    return 0;
}

int main() {
    FILE *file = fopen("./inputs/day5.txt", "r");
    if (file == NULL) {
        printf("Could not open input file\n");
        return 1;
    }
    
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
    fclose(file);

    // Sort by start (ascending)
    qsort(ranges, range_count, sizeof(Range), compareByStart);
    
    printf("ORIGINAL: \n");
    printf("%lld - %lld\n",ranges[0].start, ranges[0].end);
    int overlap;
    for (int i = 1; i < range_count; i++) {
        overlap = 0;
        printf("%lld - %lld\n",ranges[i].start, ranges[i].end);
        if (ranges[i].start <= ranges[i-1].end) {
            ranges[i].start = ranges[i-1].start;
            overlap = 1;
        }

        if (ranges[i].end <= ranges[i-1].end) {
            ranges[i].end = ranges[i-1].end;
            overlap = 1;
        }

        if (overlap) {
            ranges[i-1].start = 0;
            ranges[i-1].end = 0;
        }
    }

    long long fresh_index_count = 0;
    printf("MERGED: \n");
    for (int i = 0; i < range_count; i++) {
        printf("%lld - %lld\n",ranges[i].start, ranges[i].end);
        if (ranges[i].start != 0 && ranges[i].end != 0) {
            fresh_index_count += ranges[i].end - ranges[i].start + 1;
        }
    }
    
    printf("\nFresh Index Count: %lld\n", fresh_index_count);

}