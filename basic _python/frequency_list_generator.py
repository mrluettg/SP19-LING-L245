import sys

vocab = {} # dict to store frequency list

# for each of the lines of input
for line in sys.stdin.readlines(): 
    # the form is the line without spacing
    form = line.strip()
    # if we haven't seen it yet, set the frequency count to 0
    if form not in vocab:
        vocab[form] = 0
    vocab[form] = vocab[form] + 1

# print out the frequency list
for w in vocab:
    print('%d\t%s' % (vocab[w], w))