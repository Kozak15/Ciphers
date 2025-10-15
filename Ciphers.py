
#Helper function to make the cipher alphabet
def encipher(keyword):
    alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for item in keyword:
        if item in alpha:
            alpha.remove(item)
    l = []
    for item in keyword:
        if item not in l:
            l.append(item)
    return ''.join(l) + ''.join(alpha)
#Main functions
def keyword_cipher(s,keyword):
    st,cipher,beta = '',encipher(keyword),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in s:
        st += cipher[beta.index(item)]
    return st
    
def keyword_decipher(s,keyword):
    st,cipher,beta = '',encipher(keyword),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for item in s:
        st += beta[cipher.index(item)]
    return st
#Example:
#keyword_cipher('APPLE','HOME') returns 'HPPJA'. Cipher alphabet is 'HOMEBDFGIJKLNOPQRSTUVWXZYAC'
#keyword_decipher('HPPJA','HOME') returns 'APPLE'

#Takes in a list of keywords and encodes/decodes the string s using each keyword in turn
def keywords_cipher(s,lst):
    l1,i = [],0
    for item in lst:
        l1.append(encipher(item))
    st = ''
    for item in s:
        if item == ' ':
            st += ' '
        else:
            st += keyword_cipher(item,l1[i])
            i += 1
            i %= len(lst)
    return st

def keywords_decipher(s,lst):
    l1,i = [],0
    for item in lst:
        l1.append(encipher(item))
    st = ''
    for item in s:
        if item == ' ':
            st += ' '
        else:
            st += keyword_decipher(item,l1[i])
            i += 1
            i %= len(lst)
    return st

#Playfair cipher
#Helper functions
def coord(char, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if char == grid[i][j]:
                return [ i , j]
def extract(coord , grid):
    return grid[coord[0]][coord[1]]

#Makes a 5x5 grid from the keyword
def grid(keyword):#I and J are the same
    beta = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    l = list(keyword)
    for i in range(len(l)):
        if l[i] == 'J':
            l[i] = 'I'
    l1 = []
    for item in l:
        if item not in l1:
            l1.append(item)
    for item in beta:
        if item not in l1:
            l1.append(item)
    grid = [l1[i:i+5] for i in range(0,25,5)]
    return grid
#Splits the string into pairs, adding Xs where necessary
def pairs(s):
    s = s.replace('J', 'I')
    lst = list(s)
    i = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i + 1] and i % 2 == 0:
            lst.insert(i + 1, 'X')
        i += 2
    if len(lst) % 2:
        lst.append('X')
    return [lst[i] + lst[i + 1] for i in range(0, len(lst), 2)]
#Main function
def playfair_cipher(s,keyword):
    griddy = grid(keyword)
    pair = pairs(s)
    result = ''
    for a,b in pair:
        r1,c1 = coord(a,griddy)
        r2,c2 = coord(b,griddy)
        if r1 == r2:
            result += (griddy[r1][(c1+1) % 5] + griddy[r2][(c2+1) % 5])
        elif c1 == c2:
            result += (griddy[(r1+1) % 5][c1] + griddy[(r2+1) % 5][c2])
        else:
            result += (griddy[r1][c2] + griddy[r2][c1])
    return result
