
steering = { 'R': {'N':'E', 'E':'S', 'S':'W', 'W':'N'},
             'L': {'N':'W', 'W':'S', 'S':'E', 'E':'N'} }
def walkit(route, x=0, y=0, facing='N'):
	visited={}
	print route
	for p in route.split(', '):
		turn,dist = p[0],p[1:]
		facing = steering[turn][facing]
		for i in range(int(dist)):
			x += { 'N': 0, 'S': 0, 'E': 1, 'W':-1}[facing]
			y += { 'N': 1, 'S':-1, 'E': 0, 'W': 0}[facing]
			if visited.get((x,y)) != None:
				return 'been here before x={} y={}'.format(x,y)
			visited[ (x,y)] = 1
	print('moved to x={}, y={} facing={} walked={}'.format(x,y,facing, abs(x)+abs(y)))

walkit('R2, L3')
walkit('R2, R2, R2')
walkit('R5, L5, R5, R3')
print walkit('R8, R4, R4, R8')
print walkit('L3, R1, L4, L1, L2, R4, L3, L3, R2, R3, L5, R1, R3, L4, L1, L2, R2, R1, L4, L4, R2, L5, R3, R2, R1, L1, L2, R2, R2, L1, L1, R2, R1, L3, L5, R4, L3, R3, R3, L5, L190, L4, R4, R51, L4, R5, R5, R2, L1, L3, R1, R4, L3, R1, R3, L5, L4, R2, R5, R2, L1, L5, L1, L1, R78, L3, R2, L3, R5, L2, R2, R4, L1, L4, R1, R185, R3, L4, L1, L1, L3, R4, L4, L1, R5, L5, L1, R5, L1, R2, L5, L2, R4, R3, L2, R3, R1, L3, L5, L4, R3, L2, L4, L5, L4, R1, L1, R5, L2, R4, R2, R3, L1, L1, L4, L3, R4, L3, L5, R2, L5, L1, L1, R2, R3, L5, L3, L2, L1, L4, R4, R4, L2, R3, R1, L2, R1, L2, L2, R3, R3, L1, R4, L5, L3, R4, R4, R1, L2, L5, L3, R1, R4, L2, R5, R4, R2, L5, L3, R4, R1, L1, R5, L3, R1, R5, L2, R1, L5, L2, R2, L2, L3, R3, R3, R1')
