import re
from dataclasses import dataclass, field


@dataclass
class File:
    weight: int
    name: str


@dataclass
class Folder:
    name: str
    parent: "Folder"
    file_list: list[File] = field(default_factory=list)
    folder_list: list["Folder"] = field(default_factory=list)

    def read_from_ls(self, instruction_list: list[str], parent_folder: "Folder"):
        for instruction in instruction_list:
            part1, part2 = instruction.split(" ")
            if part1.isnumeric():
                self.file_list.append(File(weight=int(part1), name=part2))
            elif part2 not in self.get_folder_names():
                self.folder_list.append(Folder(name=part2, parent=parent_folder))

    def get_folder_names(self) -> set[str]:
        return {folder.name for folder in self.folder_list}

    def get_from_folder_list_by_name(self, name: str, parent_folder: "Folder"):
        folder_list = [folder for folder in self.folder_list if folder.name == name]

        if not folder_list:
            folder = Folder(name=name, parent=parent_folder)
            self.folder_list.append(folder)
        else:
            folder = folder_list[0]

        return folder

    def get_all_subfolders(self) -> list["Folder"]:
        folder_list = []

        for folder in self.folder_list:
            folder_list += folder.get_all_subfolders()

        folder_list += self.folder_list

        return folder_list

    def get_total_weight(self):
        total_weight = 0
        for file in self.file_list:
            total_weight += file.weight

        for folder in self.folder_list:
            total_weight += folder.get_total_weight()

        return total_weight


with open("./day7/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.read().splitlines()

# remove cd /
instruction_list = instruction_list[1:]

folder = Folder(name="/", parent=None)
i = 0
folder_tmp = folder

while i != len(instruction_list):
    instruction = instruction_list[i]

    if instruction.startswith("$ ls"):
        j = i + 1
        while (j != len(instruction_list)) and (
            not instruction_list[j].startswith("$")
        ):
            j += 1
        folder_tmp.read_from_ls(instruction_list[i + 1 : j], parent_folder=folder_tmp)
        i = j

    elif instruction.startswith("$ cd"):
        folder_name = re.search(r"\$ cd (.*)", instruction).group(1)

        if folder_name == "..":
            folder_tmp = folder_tmp.parent
        else:
            folder_tmp = folder_tmp.get_from_folder_list_by_name(
                folder_name, parent_folder=folder_tmp
            )

        i += 1

res: int = 0

folder_list = folder.get_all_subfolders()
folder_list.append(folder)

for subfolder in folder_list:
    weight = subfolder.get_total_weight()
    if weight < 100000:
        res += weight

print(f"Part 1: {res}")

#################### PART 2 ####################

TOTAL_DISK_SIZE = 70000000
SPACE_NEEDED = 30000000

OUTERMOST_DIR_SPACE = folder.get_total_weight()
SEARCHING_SPACE = SPACE_NEEDED - (TOTAL_DISK_SIZE - OUTERMOST_DIR_SPACE)

print(f"The outermost directory takes: {OUTERMOST_DIR_SPACE}")
print(f"We are searching to free {SEARCHING_SPACE}")

res_folder_space = TOTAL_DISK_SIZE

folder_list = folder.get_all_subfolders()
for subfolder in folder_list:
    weight = subfolder.get_total_weight()
    if SEARCHING_SPACE < weight < res_folder_space:
        res_folder_space = weight
        print(f"Dir {subfolder.name} free {weight}")

print(f"Part 1: {res_folder_space}")
