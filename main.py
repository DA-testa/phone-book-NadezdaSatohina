# python3

bucket_size = 256
buckets = [[] for i in range(bucket_size)]

def _hash_func(self, i):
    return i % bucket_size


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
            
def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(self, queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        hashed = _hash_func(cur_query.number)
        bucket = self.buckets[hashed]
        
        if cur_query.type == 'add':    
            for contact in bucket:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:
                self.buckets[hashed].append(cur_query)
                
        elif cur_query.type == 'del':
            for j in range(len(bucket)):
                if bucket[j].number == cur_query.number:
                    bucket.pop(j)
                    break
                    
        else:
            response = 'not found'
            for contact in bucket:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(queries, read_queries()))


