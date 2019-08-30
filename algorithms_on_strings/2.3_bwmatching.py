# python3
import sys


def PreprocessBWT(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
        * starts - for each character C in bwt, starts[C] is the first position 
            of this character in the sorted array of 
            all characters of the text.
        * occ_count_before - for each character C in bwt and each position P in bwt,
            occ_count_before[C][P] is the number of occurrences of character C in bwt
            from position 0 to position P inclusive.
    """
    # create count array
    starts = dict()
    counter = dict()
    occ_count_before = [dict() for _ in range(len(bwt)+1)]

    for i, c in enumerate(bwt):
        for k, v in counter.items():
            occ_count_before[i][k] = v
        if not c in counter:
            counter[c] = 0
        counter[c] += 1
    
    # add last row to count array
    for k, v in counter.items():
        occ_count_before[len(bwt)][k] = v

    # create dictionary with starting indices
    templist = sorted([(k,v) for k,v in counter.items()], key=lambda x: x[0])
    summing = 0
    for item in templist:
        starts[item[0]] = summing
        summing += item[1]
        
    return starts, occ_count_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and occ_counts_before.
    """
    top = 0
    bottom = len(bwt) - 1
    idx = 1

    while top <= bottom:
        if idx <= len(pattern):
            symbol = pattern[-idx]

            count_top = 0
            count_bottom = 0
            if symbol in occ_counts_before[top]:
                count_top = occ_counts_before[top][symbol]
            if symbol in occ_counts_before[bottom+1]:
                count_bottom = occ_counts_before[bottom+1][symbol]

            if count_bottom - count_top > 0:
                top = starts[symbol] + count_top
                bottom = starts[symbol] + occ_counts_before[bottom+1][symbol] - 1
            else:
                return 0
        else:
            break
        idx += 1

    return bottom - top + 1
     

if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
