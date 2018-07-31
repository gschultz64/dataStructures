class HashMap():
    def __init__(self, size=64):
        self.size = size
        self.hashmap = [[None] for i in range(self.size)]

    def put(self, key, value):
        hash_key = hash(key)
        hash_idx = hash_key % self.size
        if (self.hashmap[hash_idx][0] == None):
            self.hashmap[hash_idx][0] = {key: value}
        else:
            # This is where we deal with collisions
            self.hashmap[hash_idx].append({key: value})

    def get(self, key):
        hash_key = hash(key)
        hash_idx = hash_key % self.size
        return self.hashmap[hash_idx]

    def remove(self, key):
        hash_key = hash(key)
        hash_idx = hash_key % self.size
        if (len(self.hashmap[hash_idx]) > 1):
            for i in range(len(self.hashmap[hash_idx])):
                if (list(self.hashmap[hash_idx][i].keys())[0] == key):
                    self.hashmap[hash_idx][i] = ["Removed"]
        else:
            self.hashmap[hash_idx] = ["removed"]

    def print_map(self):
        for item in self.hashmap:
            print(item)


hm = HashMap(16)

hm.put("Kyle Van Bergen", "This is Kyle's string!")
hm.put("Jacob Spade", "This is Jacob's string!")
hm.put("Steve Peters", "This is Steve's string!")
hm.put("Michael Shull", "This is Mike's string!")

# hm.print_map()

hm.remove("Steve Peters")
hm.print_map()
