from math import log

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)
def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)
    def best_str(f):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        
        return min((c + wordcost.get(f, 9e999), k+1) for k,c in candidates)
    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    f = ""
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        if c==9e999:
            c,k = best_str(f)
            
            if c == cost[i]:
                print("Asserted!")
            
                print(f)
            else:
                print("othjer")
                out.append(f)
                print(f)
                f=""
            # print(s[i-k:i])
            # f=s[i-k:i]+f
        else:
            print()
            if(f!=""):
                out.append(f)
            f=""
            out.append(s[i-k:i])
        i -= k
        # print(i,k)
    if(f!=""):
        out.append(f)
    return " ".join(reversed(out))

s = 'goodMIcrosOftisbagoogleorbad'
print(infer_spaces(s))
