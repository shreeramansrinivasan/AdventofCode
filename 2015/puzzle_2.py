def wrapping_paper_area(prism_dimensions_string):
    l,w,h = map(int, prism_dimensions_string.split('x'))
    area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l*w, w*h, h*l)
    return area + slack
filepath  = r'example_puzzle_2.txt'
with open(filepath, 'r') as f:
    total_area = sum(wrapping_paper_area(line) for line in f)
print('total wrapping paper area needed',total_area)