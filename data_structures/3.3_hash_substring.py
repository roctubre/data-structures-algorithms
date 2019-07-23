# python3

_multiplier = 263
_prime = 1000000007

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))
    
def polyHash(s):
    hash = 0
    for i in range(len(s)-1, -1, -1):
        hash = (hash * _multiplier + ord(s[i])) % _prime
    return hash
    
def get_occurrences(pattern, text):
    result = []
    len_p = len(pattern)
    len_t = len(text)
    
    # hash of pattern
    pattern_hash = polyHash(pattern)
    
    # hash last len(P) characters in text
    c_hash = polyHash(text[len_t-(len_p):])
    
    # compare pattern with last len(p) characters in text
    if c_hash == pattern_hash and pattern == text[len_t-(len_p):]:
        result.append(len_t-(len_p))
    
    # calculate _multiplier ** len(P) mod _prime
    y = 1
    for i in range(1, len_p+1):
        y = (y * _multiplier) % _prime
    
    # calculate hashes and compare to pattern
    for i in range(len_t-(len_p+1), -1, -1):
        c_hash = (c_hash * _multiplier - ord(text[i+len_p])*y + ord(text[i])) % _prime
        if c_hash == pattern_hash and pattern == text[i:i+len_p]:
            result.append(i)
            
    return list(reversed(result))

    
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

