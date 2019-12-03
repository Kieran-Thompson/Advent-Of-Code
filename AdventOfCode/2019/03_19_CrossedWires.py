###Kieran Thompson (based on Jonathan Paulson one)
###03/12/19

wire1,wire2 = open("input.txt").read().split('\n')
  
wire1,wire2 = [x.split(',') for x in [wire1,wire2]]



DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
def get_points(A):
     x = 0
     y = 0
     length = 0
     grid = {}
     for command in A:
         d = command[0]
         movement = int(command[1:])
         for i in range(movement):
             x += DX[d]
             y += DY[d]
             length += 1
             if (x,y) not in grid:
                 grid[(x,y)] = length
     return grid

path1 = get_points(wire1)
path2= get_points(wire2)
both = set(path1.keys())&set(path2.keys())
part1 = min([abs(x)+abs(y) for (x,y) in both])
part2 = min([path1[point]+path2[point] for point in both])
print(part1)
print(part2)
