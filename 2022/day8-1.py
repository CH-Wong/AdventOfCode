import numpy as np

with open("input_day8.txt") as datafile:
    treedata = datafile.read().split("\n")

for rownum, row_of_trees in enumerate(treedata):
    treedata[rownum] = [int(height) for height in row_of_trees]

treedata = np.array(treedata)
num_rows, num_columns = np.shape(treedata)

visibility_table = np.ones((num_rows, num_columns))

for row in range(1, num_rows-1):
    for col in range(1, num_columns-1):
        right_visible = all(treedata[row, col] > treedata[row, col+1:]) 
        left_visible = all(treedata[row, col] > treedata[row, :col]) 
        top_visible = all(treedata[row, col] > treedata[:row, col])
        bottom_visible = all(treedata[row, col] > treedata[row+1:, col])

        visibility_table[row][col] = any([right_visible, left_visible, top_visible, bottom_visible])

print(int(np.sum(visibility_table)))