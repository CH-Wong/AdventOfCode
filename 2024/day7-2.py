import operator
import itertools

filename = "input_day7.txt"

with open(filename) as datafile:
    data = datafile.readlines()

# || Operator (concat) is essentially: a || b = (a * 10 ** num_digits(b)) + b
def concat(a, b):
    return a * 10 ** len(str(b)) + b

operations = [
    operator.add,
    operator.mul,
    concat,
]

calibration = 0
for linenum, line in enumerate(data):
    result, inputs = line.split(":")

    result = int(result)
    inputs = [int(val) for val in inputs.split()]
    print(f"Line: {linenum+1}/{len(data)}",result, inputs)

    for ops in itertools.product(operations, repeat=len(inputs)-1):

        test_result = inputs[0]
        for num, op in zip(inputs[1:], ops):
            test_result = op(test_result, num)
        if test_result == result:
            calibration += result
            print(f"Correct----------------------------------------{calibration}")
            break
                
print(calibration)