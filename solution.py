class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        flippedAxiesGrid = self.flipAxies(grid)
        totalIncrease = 0
        for rowNumber, row in enumerate(grid):
            for columnNumber, buildingHeight in enumerate(row):
                maxHeight = min(max(row), max(flippedAxiesGrid[columnNumber]))
                totalIncrease += self.findBuildingIncrease(maxHeight, buildingHeight)
        return totalIncrease
                
    #could just use zip() as shortcut
    def flipAxies(self, oldGrid):
        newGrid = []
        for oldRow in range(len(oldGrid)):
            newRow = []
            for oldColumn in range(len(oldGrid[0])):
                newRow.append(oldGrid[oldColumn][oldRow])
            newGrid.append(newRow)
        return newGrid
    
    def findBuildingIncrease(self, maxHeight, buildingHeight):
        buildingIncrease = maxHeight - buildingHeight
        return buildingIncrease
