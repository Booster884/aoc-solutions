# jakkie bah
file = open("in", "r")

fs = {}
pwd = []

lines = file.read().split('\n')[1:-1]
listing = False

def get_dir(fs, pwd):
    res = fs
    for x in pwd:
        res = res[x]
    return res

for line in lines:
    line = line.split(' ')

    if line[0] == '$':
        listing = False

    if listing:
        _fs = get_dir(fs, pwd)
        if line[0] == "dir":
            _fs[line[1]] = {}
        else:
            _fs[line[1]] = int(line[0])

    if line[1] == "cd":
        if line[2] == "..":
            pwd.pop()
        else:
            pwd.append(line[2])
 
    if line[1] == "ls":
        listing = True

s1 = 0
def calc_dir_size(fs):
    global s1

    dir_size = 0
    for val in fs.values():
        if type(val) is dict:
            dir_size += calc_dir_size(val)
        else:
            dir_size += val
 
    if dir_size <= 100000:
        s1 += dir_size

    return dir_size

unused_size = 70000000 - calc_dir_size(fs)
size_to_free = 30000000 - unused_size

s2 = []
def find_deleteable_dirs(fs, size_to_free):
    global s2

    dir_size = 0
    for val in fs.values():
        if type(val) is dict:
            dir_size += find_deleteable_dirs(val, size_to_free)
        else:
            dir_size += val
 
    if dir_size >= size_to_free:
        s2.append(dir_size)

    return dir_size

find_deleteable_dirs(fs, size_to_free)

print("1:", s1)
print("2:", min(s2))
