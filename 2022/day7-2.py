import re

total_size = 70000000
required_space = 30000000

with open("input_day7.txt") as datafile:
    terminal_output = datafile.read().split("\n")

# Create nested dict if files
def process_commands(line_num, current_dir):
    while True:
        if line_num < len(terminal_output):                
            line = terminal_output[line_num]
            # print(line_num, line)

            file_match = re.match("(?P<size>\d+) (?P<filename>\S+)", line)
            cd_match = re.match("\$ cd (?P<dir_name>\S+)", line)
            
            if line == "$ cd .." :
                # print("Going back up!---------------")
                return current_dir, line_num

            elif file_match is not None:
                # print("Adding file--------------")
                [size, filename] = file_match.groupdict().values()
                current_dir[filename] = int(size)

            elif cd_match is not None:
                # print("Going in!----------------------")
                [dir_name] = cd_match.groupdict().values()
                current_dir[dir_name], line_num = process_commands(line_num + 1, {})

            line_num += 1

        else:
            return current_dir, line_num
    
filesystem, line_num = process_commands(0, {})

size_dict = {}

def dir_size(dir_path, dir_content):
    size_dict[dir_path] = 0
    
    for name, content in dir_content.items():
        if isinstance(content, dict):
            size_dict[dir_path] += dir_size(f"{dir_path}{name}/", content)

        elif isinstance(content, int):
            size_dict[dir_path] += content

        else:
            print("?????????!?!!?!?!??")
    
    return size_dict[dir_path]


dir_size("/", filesystem["/"])

current_size = size_dict["/"]

minimal_directory_size = current_size + required_space - total_size
print(min([size for size in size_dict.values() if size > minimal_directory_size]))



