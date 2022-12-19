from time import perf_counter as pfc

start = pfc()
width = 7
rocks = [tuple((0b00011110,)), (0b00001000, 0b00011100, 0b00001000), (0b00000100, 0b00000100, 0b00011100),
         (0b00010000, 0b00010000, 0b00010000, 0b00010000), (0b00011000, 0b00011000)]
rocks_id = 0
dir_id = 0
directions = ''
with open('input/17.txt') as f:
    directions = f.readline().strip()

print(f'{(rocks[0][0] & 0b10000000)== 0b10000000},{rocks[0][0]:08b}')
print(f'{(rocks[0][0]<<1 & 0b10000000)== 0b10000000},{rocks[0][0]<<1:08b}')
print(f'{(rocks[0][0]<<2 & 0b10000000)== 0b10000000},{rocks[0][0]<<2:08b}')
print(f'{(rocks[0][0]<<3 & 0b10000000)== 0b10000000},{rocks[0][0]<<3:08b}')
