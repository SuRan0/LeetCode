# -*-coding:utf-8-*-
"""
You are assigned to put some amount of boxes onto one truck.
You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

boxTypes.sort(key=lambda x: -x[1])  # sort unit from large to small -> [[1, 3], [2, 2], [3, 1]]
units, size = 0, 0
for box in boxTypes:
    if size + box[0] <= truckSize:
        units += box[0] * box[1]
        size += box[0]
    else:
        units += (truckSize - size) * box[1]
        break
