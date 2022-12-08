# Day 7

Today's problem was a simulated filesystem that we needed to install and update to but we didn't have enough disk space! The puzzle input is the output from a console with commands and their outputs. We have to build a model filesystem by reading the console commands and interpreting them. When using `ls` it displays files with their size.

Parsing the input was the easy part...the rest took me about 2 hours. Some of that was with a bug that caused my example input to give me the right answer, but the real input was incorrect. It was really hard to find the bug because I was trying to solve it recursivley and that can get pretty confusing. These are the two functions that I used to solve part 1.
```python
def getSize(dir: Dir):
    size = 0
    for item in dir.contents:
        if type(item) is File:
            size += item.size
        else:
            size += getSize(item)
    return size

def getSizeLimit(dir: Dir, limit, totalSize = 0):
    for item in dir.contents:
        if type(item) is Dir:
            s = getSize(item)
            if s <= limit:
                totalSize += s
            totalSize = getSizeLimit(item, limit, totalSize)
    return totalSize

root = parseFileSystem(file)
print(getSizeLimit(root, 100000))
```
I call `getSizeLimit` to get the total size of all directories that are no larger than `100000`.

For part 2, we found out that the update needs `30000000` of unused space. So we're tasked with finding the smallest directory that can be deleted to give enough free space. The `findSpace` function is similar to the `getSizeLimit` function.
```python
def findSpace(dir: Dir, dirToDelete = float('inf')):
    for item in dir.contents:
        if type(item) is Dir:
            s = getSize(item)
            if s >= needToDelete and s < dirToDelete:
                dirToDelete = s
            dirToDelete = findSpace(item, dirToDelete)
    return dirToDelete

root = parseFileSystem(file)
totalSize = getSize(root)
maxUsedSpace = 70000000 - 30000000
needToDelete = totalSize - maxUsedSpace
dirToDelete = findSpace(root)
print(dirToDelete)
```
