from math import log

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)
ign = []
def infer_spaces(s):
    global ign
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

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
        if(i-i+k)==1:
            # print(s[i-k:i])
            f=s[i-k:i]+f
        else:
            if(f!=""):
                ign.append(f)
                # out.append(f)
            f=""
            out.append(s[i-k:i])
        i -= k
        # print(i,k)
    if(f!=""):
        ign.append(f)
        # out.append(f)
    return ((out))
s = 'G00gleisfood'
ans = []
while s!="":
    try:
        out = (infer_spaces(s))
        ans.extend(out)
        # print(out)
        s = ign[0]
        # print(s)
        s=s[1:]
        ign = []
    except:
        break
print(ans)