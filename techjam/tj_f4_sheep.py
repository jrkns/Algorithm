def print_area(area):
    for i in range(len(area)):
        row = ''
        for j in range(len(area[0])):
            if area[i][j] == 0:
                row += '.'
            else:
                row += '*'
        print(row)
    return

def main():
    # Require Testcase File
    infile = open('testdata4.txt', 'r')
    n = infile.readline()
    impossible = [(3,3,2),(3,2,1)]
    for i in range(int(n)):
        a, b, c = infile.readline().split()
        a = int(a)
        b = int(b)
        c = int(c)
        print('#' + str(i + 1))
        area = [[0 for x in range(a)] for y in range(b)]
        aa = 0
        bb = 0
        fix_a = a
        fix_b = b
        while a > 0 and b > 0:
            if a > b:
                if c-b < 0:
                    break
                for k in range(fix_b):
                    area[k][aa] = 1
                aa +=1
                a -= 1
                c-=b
            else:
                if c-a < 0:
                    break
                for k in range(fix_a):
                    area[bb][k] = 1
                bb+=1
                b -= 1
                c-=a
        im = False
        for A,B,C in impossible:
            if a==A and b==B and c==C:
                im = True
            if a==B and b==A and c==C:
                im = True
        if im:
            print('impossible')
        elif min(a,b) == 2 and c >= 1 and c%2!=0:
            print('impossible')
        elif a == 1 and b == 1:
            print('impossible')
        elif a==4 and b==4 and c==3:
            area[bb][aa] = 1
            area[bb+1][aa] = 1
            area[bb][aa+1] = 1
            print_area(area)
        elif a == 1 or b == 1:
            if fix_a == 1 or fix_b == 1:
                if max(fix_a,fix_b) - c - 1 > 0:
                    print_area(area)
                else:
                    print('impossible')
            else:
                print('impossible')
        elif c == 0:
            print_area(area)
        elif max(a,b)-c >= 2:
            if a > b:
                for ii in range(aa,aa+c):
                    area[bb][ii] = 1
            else:
                for ii in range(bb,bb+c):
                    area[ii][aa] = 1
            print_area(area)
        elif min(a,b) >= 3 and c > 2:
            if a > b:
                for ii in range(bb,bb+3):
                    area[ii][aa] = 1
                for ii in range(aa,aa+c-2):
                    area[bb][ii] = 1
            else:
                for ii in range(aa,aa+3):
                    area[bb][ii] = 1
                for ii in range(bb,bb+c-2):
                    area[ii][aa] = 1
            print_area(area)
        else:
            print('impossible')

if __name__ == '__main__':
    main()