class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def to_string(self, level):
        def indent():
            return ' '*(level*2)
        return indent() + "- %s (file, size=%d)\n" % (self.name, self.size)

class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.items = []
        self.folders = []
        self.files = []
        self.parent = parent

    def get_folders(self):
        folder_list = []
        self.get_foldersR(folder_list)
        return folder_list

    def get_foldersR(self, folder_list):
        folder_list.append(self)
        for folder in self.folders:
            folder.get_foldersR(folder_list)

    def get_folders2(self):

        folder_list = []
        stack = []
        currentfolder = self
        stack.append(currentfolder)

        while len(stack) > 0:
            folder_list.append(currentfolder)
            for f in currentfolder.folders:
                stack.append(f)

            currentfolder = stack.pop()

        return folder_list

    def add_folder(self, folder):
        self.folders.append(folder)
        self.items.append(folder)

    def add_file(self, file):
        self.files.append(file)
        self.items.append(file)

    def find_folder(self, folder_name):
        for folder in self.folders:
            if folder_name == folder.name:
                return folder

    def get_size(self):
        sum = 0
        for item in self.items:
            sum += item.get_size()
        return sum

    def to_string(self, level):
        msg = '%s- %s (dir, size=%d)\n' % (' '*(level*2), self.name, self.get_size())
        for item in self.items:
            msg += item.to_string(level+1)
        return msg;


class Exercise:
    COMMAND_STATE = 1
    LIST_STATE = 2

    def __init__(self):
        self.root_folder = Folder('/', None)
        self.current_folder = self.root_folder

    def get_folder(self, folder_name):
        folder = self.current_folder.find_folder(folder_name)
        if folder is None:
            folder = Folder(folder_name, self.current_folder)
            self.current_folder.add_folder(folder)
        return folder

    def print(self):
        print(self.root_folder.to_string(level=0))

    def read_file(self, filename):
        with open(filename) as f:
            self.lines = [line.strip() for line in f.readlines()]

        state = Exercise.COMMAND_STATE
        i = 0
        while i < len(self.lines):
            line = self.lines[i]
            tokens = line.split()

            if state == Exercise.COMMAND_STATE:
                if line.startswith('$'):
                    if tokens[1] == 'cd':
                        if tokens[2] == '/':
                            self.current_folder = self.root_folder
                        elif tokens[2] == '..':
                            self.current_folder = self.current_folder.parent
                        else:
                            self.current_folder = self.get_folder(tokens[2])

                    elif tokens[1] == 'ls':
                        state = Exercise.LIST_STATE
                i += 1

            elif state == Exercise.LIST_STATE:
                if line.startswith('$'):
                    state = Exercise.COMMAND_STATE
                elif tokens[0] == 'dir':
                    self.get_folder(tokens[1])
                    i += 1
                else:
                    self.current_folder.add_file(File(tokens[1], int(tokens[0])))
                    i += 1
    def get_score(self):
        folder_list = filter(lambda folder: folder.get_size() <= 100000, self.root_folder.get_folders())
        folder_sum = sum([folder.get_size() for folder in folder_list])
        return folder_sum

    def get_score2(self):
        total_space = 70000000
        used_space = self.root_folder.get_size()
        unused_space = total_space - used_space
        required_unused_space = 30000000

        minimum_deleted_space = required_unused_space - unused_space
        folder_list = filter(lambda folder: folder.get_size() >= minimum_deleted_space, self.root_folder.get_folders())
        smallest_folder = min(folder_list, key=lambda folder: folder.get_size())
        return smallest_folder.get_size()


def score(filename):
    ex = Exercise()
    ex.read_file(filename)
    #ex.print()
    print(ex.get_score())

def score2(filename):
    ex = Exercise()
    ex.read_file(filename)
    #ex.print()
    print(ex.get_score2())

score('sample.txt')
score('input.txt')

score2('sample.txt')
score2('input.txt')
