eg = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

def parse(eg):
    for line in filter(None, eg.split('\n')):
        all_digits, data = line.split('|')
        all_digits = all_digits.strip().split(' ')
        data = data.strip().split(' ')
        yield all_digits, data

def part1(iter):
    p = 0
    for all_digits, data in iter:
        ls = [1 for x in data if len(x) in (2,4,3,7)]
        p += sum(ls)
        # digit segs    len unique
        # 1     cf       2   Y
        # 4     bcdf     4   Y
        # 7     acf      3   Y
        # 8     abcdefg  7   Y
    return p

digits = {
        'abcefg': 0,
        'cf': 1,
        'acdeg':2,
        'acdfg': 3,
        'bcdf':4,
        'abdfg':5,
        'abdefg':6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }

def part2(iter):
    # Method:
    # digit segs    len unique
    # 1     cf       2   Y
    # 4     bcdf     4   Y
    # 7     acf      3   Y
    # 8     abcdefg  7   Y
    # 2     acdeg    5   N
    # 3     acdfg    5   N
    # 5     abdfg    5   N
    # 0     abcefg   6   N
    # 6     abdefg   6   N
    # 9     abcdfg   6   N
    # subtract 1 from 7 to find a
    #   7,1   acf-cf => a
    # subtract 7 from all len5s
    #   (2)   acdeg-acf = deg
    #   (3)   acdfg-acf = dg
    #   (5)   abdfg-acf = bdg
    # then subtract 4 from two longer to find g, then e
    #     deg - bcdf = eg
    #     bdg - bcdf = g
    # then shorter dg - g finds d
    # Progress: abcdefg => a--de-g
    #  take the 6s and remove adeg, leaves 1x2, 2x3
    #           (6) abdefg - adeg = bf
    #           (9) abcdfg - adeg = bcf
    #           (0) abcefg - adeg = bcf
    #  subtract pattern for 7 from the shorter to find b
    #      bf - acf = b
    # Progress: abcdefg => ab-de-g
    #      take all len5 patterns, subtract known 'adeg' to find c
    #     (2)  acdeg-adeg = c
    #     (3)  acdfg-adeg = cf
    #     (5)  abdfg-adeg = bf
    #    Minus c on 2x2 to find f
    #        cf-c  = f
    #        bf-c  = bf

    def checkE1(singletonset):
        assert(len(singletonset) == 1)
        return list(singletonset)[0]

    gtotal = 0
    for all_digits, data in iter:
        # all_digits is a set of 10 7segment wires
        # egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg

        # sort by length to pull out the known digits. parenthesis show unknown ordering
        # cg cgb cegd (fecab bfceg egfdb) (egadfb cdbfeg fgcdab) gbdefca
        sets_by_length = [set(x) for x in sorted(all_digits, key=len)]
        assert(len(sets_by_length) == 10)
        # 2 3 4 5 5 5 6 6 6 7
        known = {
            1: sets_by_length[0], # cf
            4: sets_by_length[2], # bcdf
            7: sets_by_length[1], # acf
            8: sets_by_length[9], # abcdefg
        }
        fives = sets_by_length[3:6]
        sixes = sets_by_length[6:9]

        #print(known)
        # subtract 1 from 7 to find a
        a = checkE1(known[7] - known[1])

        # subtract 7 from all len5s
        littles = sorted([x - known[7] for x in fives], key=len)
        # then subtract 4 from two longer to find g, then e
        mids = sorted([x - known[4] for x in littles[1:]], key=len)
        g = checkE1(mids[0])
        e = checkE1(mids[1] - mids[0])
        # then shorter dg - g finds d
        d = checkE1(littles[0] - set(g))

        #  take the 6s and remove adeg, leaves 1x2, 2x3
        sixes_adeg = sorted([x - set([a,d,e,g]) for x in sixes], key=len)
        #  subtract pattern for 7 from the shorter to find b
        b = checkE1(sixes_adeg[0] - known[7])

        #      take all len5 patterns, subtract known 'adeg' to find c
        fives_adeg = sorted([x - set([a,d,e,g]) for x in fives], key=len)
        #     (2)  acdeg-adeg = c
        #     (3)  acdfg-adeg = cf
        #     (5)  abdfg-adeg = bf
        c = checkE1(fives_adeg[0])
        #    Minus c on remainder from longer to find f then b
        #        cf-c  = f
        #        bf-c  = bf - f = b
        fives_adeg2 = sorted([x - set(c) for x in fives_adeg[1:]], key=len)
        f = checkE1(fives_adeg2[0])
        b = checkE1(fives_adeg2[1] - set(f))

        #print("mapping {}{}{}{}{}{}{}".format(a,b,c,d,e,f,g))
        #
        decoder = {a: 'a', b: 'b', c: 'c', d: 'd', e: 'e', f: 'f', g:'g'}
        total = 0
        print(data)
        for d in data:
            segs = ''.join(sorted([decoder[c] for c in d]))
            total = 10*total + digits[segs]
        print(total)
        gtotal += total
    print("grand total {}".format(gtotal))

print(part1(parse(eg)))
print(part1(parse(open('input/day8.txt').read())))

part2(parse(eg))
part2(parse(open('input/day8.txt').read()))
