from enum import Enum, auto
from typing import Union, List
from dataclasses import dataclass

with open("../inputs/day07", "r") as f:
    seq = f.read()
    lines = seq.split("\n")


@dataclass
class File:
    name: str
    size: int


@dataclass
class Folder:
    name: str
    parent: "Folder"
    files: List[File]
    folders: List["Folder"]

    @property
    def size(self) -> int:
        return sum([f.size for f in self.files]) + sum([f.size for f in self.folders])

    def __repr__(self) -> str:
        return f"{self.name} ({self.size})"


def build_folders(lines: List[str]) -> Folder:
    root = Folder("/", None, [], [])
    current_folder = root

    for line in lines[1:]:
        c = line.split(" ")
        if c[0] == "$" and c[1] == "cd" and c[2] == "..":
            current_folder = current_folder.parent
        elif c[0] == "$" and c[1] == "cd" and c[2] != "..":
            new_folder = Folder(c[2], current_folder, [], [])
            current_folder.folders.append(new_folder)
            current_folder = new_folder
        elif c[0] == "$" and c[1] == "ls":
            pass
        elif len(c) == 2 and c[0].isdigit():
            current_folder.files.append(File(c[1], int(c[0])))

    return root


root = build_folders(lines)


def find_all_folder_sizes(root: Folder) -> List[int]:
    """Recursively find all folder sizes."""
    result = [root.size]
    for folder in root.folders:
        result.extend(find_all_folder_sizes(folder))

    return result


all_folder_sizes = find_all_folder_sizes(root)
total_size_of_small_folders = sum(filter(lambda s: s < 100000, all_folder_sizes))
print(f"Total size of small folders: {total_size_of_small_folders}")

available_space = 70000000
current_unused_space = available_space - root.size
required_unused_space = 30000000
required_space_to_free = required_unused_space - current_unused_space

smallest_possible_size = min(
    filter(lambda s: s >= required_space_to_free, all_folder_sizes)
)
print(f"Smallest possible size: {smallest_possible_size}")
