# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.table = [None] * bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count
    
    def process_queries(self, queries):
        result = []
        for q in queries:
            query = Query(q)
            if query.type == "check":
                if not self.table[query.ind]:
                    self.table[query.ind] = []
                result.append(' '.join(self.table[query.ind]))
            else:
                idx = self._hash_func(query.s)
                if not self.table[idx]:
                    self.table[idx] = []
                if query.type == "find":
                    found = False
                    for item in self.table[idx]:
                        if item == query.s:
                            found = True
                            break
                    result.append("yes" if found else "no")
                elif query.type == "del":
                    for i in range(len(self.table[idx])):
                        if self.table[idx][i] == query.s:
                            del self.table[idx][i]
                            break
                elif query.type == "add":
                    found = False
                    for item in self.table[idx]:
                        if item == query.s:
                            found = True
                            break
                    if not found:
                        self.table[idx].insert(0, query.s)

        return result

if __name__ == '__main__':
    bucket_count = int(input())
    n = int(input())
    proc = QueryProcessor(bucket_count)
    queries = []
    for _ in range(n):
        queries.append(input().split())
    result =  proc.process_queries(queries)
    print("\n".join(result))
