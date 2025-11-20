import numpy as np

with open("input_day8.txt") as datafile:
    treedata = datafile.read().split("\n")

for rownum, row_of_trees in enumerate(treedata):
    treedata[rownum] = [int(height) for height in row_of_trees]

treedata = np.array(treedata)
num_rows, num_columns = np.shape(treedata)

scenic_score_table = np.zeros((num_rows, num_columns))

for row in range(1, num_rows-1):
    for col in range(1, num_columns-1):
        scenic_score_table[row][col] = 1
        tree_height = treedata[row, col]
        
        trees_right = treedata[row, col+1:]
        trees_left = np.flip(treedata[row, :col])
        trees_top = np.flip(treedata[:row, col])
        trees_bot = treedata[row+1:, col]

        for tree_set in [trees_right, trees_left, trees_top, trees_bot]:
            
            scenic_score_set = 0
            for tree in tree_set:
                if tree < tree_height:
                    scenic_score_set += 1
                elif tree >= tree_height:
                    scenic_score_set += 1
                    break
                else:
                    print("????!?!!!?!?!?!")
            if row == 1 and col == 2:
                print(scenic_score_set)


            scenic_score_table[row][col] *= scenic_score_set

print(scenic_score_table)
print(int(np.max(scenic_score_table)))