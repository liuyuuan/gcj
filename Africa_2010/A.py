# Problem A. Store Credit
import sys
import pdb
def main():
    case = int(sys.stdin.readline().strip())
    count = case
    while case >0:
        case -= 1
        credit = int(sys.stdin.readline().strip('\n'))
        num = int(sys.stdin.readline().strip('\n'))
        prices = sys.stdin.readline().strip('\n').split()
        prices = [ int(n) for n in prices ]
        p = prices[:]
        prices.sort()
        # find credit//2
        # { i points to the number equal to or bigger than
        #   credit//2 }
        i = -1
        for n in prices:
            i += 1
            if i == num:
                return -1          # !no-result exit
            if 2*n>=credit:
                break;
        if 2*prices[i] == credit and 2*prices[i+1] == credit:
            pos = p.index(prices[i])
            pos1 = p.index(prices[i+1],pos+1)
            print "Case #%d:" % (count-case),
            print pos+1, pos1+1   # !normal exit 1
        #####################
        else:
            j = i-1
            if 2*prices[i]==credit:
                i += 1
            # { must not be in range (j,i) }
            while i<num and j>=0 and prices[i] < credit:
                addup = prices[j] + prices[i]
                if addup < credit:
                    i += 1
                else:
                    if  addup > credit:
                        j -= 1
                    else:
                        break
            if prices[i] + prices[j] == credit:
                print "Case #%d:" % (count-case),
                pj = p.index(prices[j])+1
                pi = p.index(prices[i])+1
                if pj < pi:
                    print pj, pi #! normal exit 2
                else:
                    print pi, pj
            else:
                return -1        # !no-result exit
if __name__ == '__main__':
    main()
