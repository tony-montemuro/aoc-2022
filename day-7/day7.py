# object that defines a directory
class Directory:
    # size attribute, only keep track of files
    size = 0

    # constructor
    def __init__(self, par, name):
        self.parent = par
        self.name = name
        self.children = []

# function that returns the total size of a directory
def getTotalSize(dir):
    size = dir.size
    # base case: directory has no children. if so, simply return the size of directory
    if len(dir.children) == 0:
        return size

    # general case: directory one or more children directories. we add the size of each
    # child directory to the current size, and then return
    for child_dir in dir.children:
        size += getTotalSize(child_dir)
    return size

def create_dir_list(dir, dir_list):
    # base case: dir has no children. this implies that it is a child directory
    # thus, we can simply append the directory to the list of directories, and return
    if len(dir.children) == 0:
        dir_list.append(dir)
        return

    # general case: directory has children directory. if this is the case, recursively call
    # this function for each child directory, print the current directory, and return
    else:
        for child in dir.children:
            create_dir_list(child, dir_list)
        dir_list.append(dir)
        return

def main():
    # open file
    f = open("puzzle.txt", "r")
    terminal = f.read().split('\n')

    # set up a dictionary that will keep track of what is contained within each directory
    head = Directory(None, '/')
    curr_dir = head

    # parse terminal
    for instr in terminal:
        # first, we need to initalize variables
        words = instr.split(' ')
        instr, dir, size = None, None, None
        # first, let's handle an instruction
        if words[0] == '$':
            instr = words[1]
            if instr == 'cd':
                dir = words[2]

        # now, let's handle a directory or file
        else:
            if words[0] == 'dir':
                dir = words[1]
            else:
                size = int(words[0])
        
        # now that we have parsed the terminal line, we can decide what to do

        # either cd or ls (NOTE: ls really does not need to be handeled)
        if instr:
            # cd ..
            if dir == '..':
                curr_dir = curr_dir.parent
            
            # cd dirName
            elif instr == 'cd':
                for child in curr_dir.children:
                    if child.name == dir:
                        curr_dir = child

            # ls
            else:
                continue

        # this is either a file or a directory
        else:
            # dir dirName
            if dir != None:
                child_dir = Directory(curr_dir, dir)
                curr_dir.children.append(child_dir)
            
            # fileSize fileName
            else:
                curr_dir.size += size

    # now, we need to create the list of dir. we can do this by recursively going through file structure
    # and generating the list of directories
    dir_list = []
    create_dir_list(head, dir_list)

    # finally, we can calculate the sum of directories whose total size is less than or equal to 100,000
    total = 0
    size_dict = {} # used in part 2
    for dir in dir_list:
        dir_total_size = getTotalSize(dir)
        if (dir_total_size <= 100000):
            total += dir_total_size
        size_dict[dir] = dir_total_size
    size_dict = dict(sorted(size_dict.items(), key=lambda item: item[1]))
    print(total)

    # for part 2, we need to find the minimum directory to delete that will free up enough space to
    # run the update
    total_space, update_unused = 70000000, 30000000
    outermost_size = getTotalSize(head)
    curr_unused = total_space-outermost_size

    # now, we can loop through the dictionary of directories sorted by size, and determine the
    # size of the first directory large enough that if deleted, would allow the update to run
    found = False
    smallest_size = None
    for dir, dir_size in size_dict.items():
        if curr_unused+dir_size > update_unused and not found:
            smallest_size = dir_size
            found = True
    print(smallest_size)

    # close file
    f.close()

if __name__ == '__main__':
    main()