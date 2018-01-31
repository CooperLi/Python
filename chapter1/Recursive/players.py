def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n-1)

def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        play_alice(n-2)
    else:
        play_alice(n-1)

def is_even(n):
    if n % 2 == 0:
        return True

print("play_alice(20)")
play_alice(20)
print("play_bob(6)")
play_bob(6)

#for n in range(1,200):
#    play_alice(n)
