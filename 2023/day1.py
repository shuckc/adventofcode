import re
import string

def ai(inp, exp):
    print(inp)
    assert inp == exp

def p1(inp):
    t = 0
    for l in inp.split('\n'):
        ln = ""
        #print(l)
        for c in l:
            if c in string.digits:
                ln += c
        s = ln[0] + ln[-1]
        # print(f"{l:30} {ln} -> {s}")
        t += int(s)
    return t

ai(p1("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"), 142)
print(p1(open("day1.txt").read().strip()))

# wrong approach - see tests
def multireplace(string, replacements):
    substrs = sorted(replacements, key=len, reverse=True)
    regexp = re.compile('|'.join(map(re.escape, substrs)))
    return regexp.sub(lambda match: replacements[match.group(0)], string)

def p2(inp):
    swap = dict([(v, str(1+i)) for i,v in enumerate('one,two,three,four,five,six,seven,eight,nine'.split(','))])
    print(swap)
    inp = multireplace(inp, swap)
    return p1(inp)

ai(p2("two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"), 281)
ai(p2("eightwone"), 81)
ai(p2("xxoneightonexx"), 11)
# ai(p2("onetwone"), 11) => FAILS, returns 12 not 11

# scan without replacement for part 2
def p3(inp):
    swap = dict(
        [(v, str(1+i)) for i,v in enumerate('one,two,three,four,five,six,seven,eight,nine'.split(','))] +
        [(str(i),str(i)) for i in range(1,10)]
    )
    print(swap)
    t = 0
    for l in inp.split('\n'):
        ln = []
        for ci in range(len(l)):
            for k,v in swap.items():
                if l[ci:ci+len(k)] == k:
                    ln.append(v)

        s = ln[0] + ln[-1]
        print(f"{l:60} {ln} -> {s}")
        t += int(s)
    return t

ai(p3("eightwone"), 81)
ai(p3("xxoneightonexx"), 11)
ai(p3("onetwone"), 11)
print(p3(open("day1.txt").read().strip()))
