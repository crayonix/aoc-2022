class Directory:
    def __init__(self, name, parent):
        self.items = []
        self.name = name
        self.parent = parent

    def get_size(self):
        total_size = 0
        for item in self.items:
            if isinstance(item, Directory):
                total_size += item.get_size()
            else:
                total_size += item.size
        return total_size

    # part 1 start

    def get_sperate_directory_sizes_by_max(self, sizes_arr, size_max=100000):
        total_size = 0
        for item in self.items:
            if isinstance(item, Directory):
                size = item.get_sperate_directory_sizes_by_max(
                    sizes_arr, size_max)
                total_size += size
                if size < size_max:
                    sizes_arr.append(size)
            else:
                total_size += item.size
        return total_size

    # part 1 end

    # part 2 start

    def get_sperate_directory_sizes_by_min(self, arr, size_min):
        total_size = 0
        for item in self.items:
            if isinstance(item, Directory):
                size = item.get_sperate_directory_sizes_by_min(
                    arr, size_min)
                total_size += size
                if size >= size_min:
                    arr.append((size, item.name))
            else:
                total_size += item.size
        return total_size

    # part 2 end

    def add_item(self, item):
        self.items.append(item)

    def get_directory(self, name):
        for item in self.items:
            if isinstance(item, Directory) and item.name == name:
                return item
        return None

    def get_file(self, name):
        for item in self.items:
            if isinstance(item, File) and item.name == name:
                return item
        return None


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


input_file = open("input.txt", "r")
lines = input_file.readlines()

root = Directory("/", None)
pwd = root

for line in lines:
    line = line.strip()
    if line.startswith("$"):
        command = line.split(" ")[1]
        if "ls" in command:
            continue
        elif "cd" in command:
            directory = line.split(" ")[-1]
            if directory == "..":
                pwd = pwd.parent
            elif directory == "/":
                pwd = root
            else:
                pwd = pwd.get_directory(directory)
    else:
        item = line.split(" ")
        if "dir" in item[0]:
            directory = pwd.get_directory(item[1])
            if not directory:
                new_directory = Directory(item[1], pwd)
                pwd.add_item(new_directory)
        else:
            _file = pwd.get_file(item[1])
            if not _file:
                new_file = File(item[1], int(item[0]))
                pwd.add_item(new_file)

# part 1

sizes_arr = []
root.get_sperate_directory_sizes_by_max(sizes_arr)
print("Part 1: " + str(sum(sizes_arr)))

# part 2

unused_space = 70000000 - root.get_size()
space_needed = 30000000 - unused_space
arr = []
root.get_sperate_directory_sizes_by_min(arr, space_needed)
print("Part 2: " + str(min(arr)))
