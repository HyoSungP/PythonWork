import sys
grid = '100006020000100475000304800079005000000000503305809000014060002960000000000080000'
#grid = '000000010400000000020000000000050604008000300001090000300400200050100000000807000'
#grid = '000000012000035000000600070700000300000400800100000000000120000080000040050000600'
#grid = '000000012003600000000007000410020000000500300700000600280000040000300500000000000'
#grid = '000000012008030000000000040120500000000004700060000000507000300000620000000100000'
#grid = '000000012040050000000009000070600400000100000000000050000087500601000300200000000'
#grid = '000000012050400000000000030700600400001000000000080000920000800000510700000003000'
#grid = '000000012300000060000040000900000500000001070020000000000350400001400800060000000'
#grid = '000000012400090000000000050000200000600000400000108000018000000000030700502000000'
#grid = '100006020000100475000304800079005000000000503305809000014060002960000000000080700'
#grid = '072408935400900000051020000030000001000501000100000070000090870000002000298607310'

def cross(A, B):
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
            for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
            for s in squares)

def parse_grid(grid):
        values= dict((s, digits) for s in squares)
        for s,d in grid_values(grid).items():
                if d in digits and not assign(values, s, d):
                        return False 
        return values


def grid_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    if d not in values[s]:
        return values 
    values[s] = values[s].replace(d,'')
    
    if len(values[s]) == 0:
        return False 
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
    if len(dplaces) == 0:
        return False 
    elif len(dplaces) == 1:
        if not assign(values, dplaces[0], d):
            return False
    return values

def solve(grid): return search(parse_grid(grid))

def search(values):
    if values is False:
        return False 
    if all(len(values[s]) == 1 for s in squares):
        return values
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
        for d in values[s])

def some(seq):
    for e in seq:
        if e: return e
    return False


anwerlist = solve(grid).values()
anwerlist = list(anwerlist)
intrealdata = [int(i) for i in anwerlist]
print(intrealdata)