
total_lenth= 100
block_lenth= 5
tiles = total_lenth/block_lenth

black_blocks= tiles/2
white_blocks= black_blocks-1
print (black_blocks,white_blocks)
gaps = (total_lenth - (black_blocks + white_blocks )*5)/2

print (gaps)