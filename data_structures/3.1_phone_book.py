# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class Contact:
    def __init__(self, number, name):
        self.number = number
        self.name = name
            
def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = [None]*(10**7-1)
    for cur_query in queries:
        if cur_query.type == 'add':
            if contacts[cur_query.number]:
                contacts[cur_query.number].name = cur_query.name
            else:
                contacts[cur_query.number] = Contact(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
        elif cur_query.type == 'find':
            if contacts[cur_query.number]:
                result.append(contacts[cur_query.number].name)
            else:
                result.append("not found")
            
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

