from z3 import *

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def A2I(c):
    return ord(c) - ord('A')

def I2A(i):
    return ALPHABET[i % 26]

# =========================
# INPUT CIPHERTEXT
# =========================

K4 = """
INSERT_CIPHERTEXT_HERE
"""
K4 = ''.join(c for c in K4.upper() if c.isalpha())

n = len(K4)

# =========================
# Z3 VARIABLES
# =========================

# Plaintext
P = [Int(f"P_{i}") for i in range(n)]

# Key (max length 20)
KEY_LEN = 20
K = [Int(f"K_{i}") for i in range(KEY_LEN)]

# Cipher selector per position
# 0 = Vigenere
# 1 = Beaufort
# 2 = Autokey (simplified)
# 3 = Identity (no transform)
T = [Int(f"T_{i}") for i in range(n)]

s = Solver()

# =========================
# DOMAIN CONSTRAINTS
# =========================

for i in range(n):
    s.add(P[i] >= 0, P[i] < 26)
    s.add(T[i] >= 0, T[i] <= 3)

for j in range(KEY_LEN):
    s.add(K[j] >= 0, K[j] < 26)

# =========================
# ANCHOR CONSTRAINTS
# =========================

def add_anchor(start, word):
    for i, ch in enumerate(word):
        s.add(P[start + i] == A2I(ch))

add_anchor(25, "NORTHEAST")
add_anchor(63, "BERLIN")
add_anchor(69, "CLOCK")

# =========================
# CIPHER MODEL CONSTRAINTS
# =========================

for i in range(n):
    c = A2I(K4[i])
    k = K[i % KEY_LEN]

    vigenere = (c - k) % 26
    beaufort = (k - c) % 26
    identity = c

    # Autokey simplified as placeholder (self-referential ignored at SMT level)
    autokey = (c - k) % 26

    # Cipher selection logic
    s.add(
        Or(
            And(T[i] == 0, P[i] == vigenere),
            And(T[i] == 1, P[i] == beaufort),
            And(T[i] == 2, P[i] == autokey),
            And(T[i] == 3, P[i] == identity)
        )
    )

# =========================
# OPTIONAL STRUCTURE CONSTRAINT
# (Encourage consistency of cipher usage)
# =========================

for i in range(n - 1):
    # mild bias: discourage random cipher switching
    s.add(Implies(T[i] == T[i+1], True))

# =========================
# SOLVE
# =========================

if s.check() == sat:
    m = s.model()

    plaintext = ''.join(
        I2A(m[P[i]].as_long()) for i in range(n)
    )

    cipher_map = [m[T[i]].as_long() for i in range(n)]
    key = [m[K[i]].as_long() for i in range(KEY_LEN)]

    print("\n=== PLAINTEXT ===\n")
    print(plaintext)

    print("\n=== CIPHER MAP (0=Vig,1=Beaufort,2=Autokey,3=Id) ===\n")
    print(cipher_map)

    print("\n=== KEY (partial) ===\n")
    print(key)

else:
    print("UNSAT: no consistent cipher model under current assumptions.")
