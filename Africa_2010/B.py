#Problem B. Reverse Words
import sys
inputs = sys.stdin
case = int(inputs.readline().strip())
count = case
while case > 0:
    case -= 1
    words = inputs.readline().strip()
    words = words.split()
    words.reverse()
    print "Case #%d:" % (count-case),
    for word in words:
        print word,
    print '\n',
