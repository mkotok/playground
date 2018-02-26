import random


colors = "RGBCMYKW"
keylen = 4

print "Welcome to Mastermind!"
print "Available colors = %s" % colors
print "Length of key = %d" % keylen
print "-" * 50

key = "".join([random.choice(colors) for _ in xrange(keylen)])
guess = ""
count = 0

while guess != key:

    guess = raw_input("Enter a guess: ").upper()

    if len(guess) != keylen:
        print "Guess must be %d colors. Please try again" % keylen
        continue

    elif not set(guess) <= set(colors):
        print "Invalid colors used. Please try again"
        continue

    count += 1
    diffs = [i for i in xrange(keylen) if key[i] != guess[i]]
    remaining = [key[i] for i in diffs]

    blacks = keylen - len(diffs)
    whites = 0
    for i in diffs:
        try:
            idx = remaining.index(guess[i])
        except ValueError:
            continue
        else:
            del remaining[idx]
            whites += 1

    print "%dW %dB" % (whites, blacks)

print "You guessed the key in %d guess(es)" % count
