# magic square

"""
3x3 square that can add up to 15:
1 9 5 center: 5 => appear 4 times so it has to be in center
2 8 5 edge: 1,3,7,9 => appear 2 times so it has to be an edge
3 7 5 corner: 2,4,6,8 => appear 3 times so it has to be at the corner
4 6 5
4 3 8
6 2 7
6 1 8
9 2 4
"""
def formingMagicSquare(s):
    possible_magic_squares = [
        [[8,1,6], [3,5,7], [4,9,2]],
        [[6,1,8], [7,5,3], [2,9,4]],
        [[4,9,2], [3,5,7], [8,1,6]],
        [[2,9,4], [7,5,3], [6,1,8]],
        [[8,3,4], [1,5,9], [6,7,2]],
        [[4,3,8], [9,5,1], [2,7,6]],
        [[6,7,2], [1,5,9], [8,3,4]],
        [[2,7,6], [9,5,1], [4,3,8]]
        ]

    min_cost = float('inf')
    for p in possible_magic_squares: #loop through each box of possible_magic_squares
        cur_cost = 0
        for i in range(len(p)): #iterate the rows of p
            
                


s = [[5,3,4], [1,5,8], [6,4,2]]
formingMagicSquare(s)