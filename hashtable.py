

class HashTable:

    def __init__(self, initial_size=15):

        self.size = initial_size
        self.table = [[] for _ in range(self.size)] # Create a list of lists

    def __str__(self):
        return str(self.table)

    def __len__(self):
        return sum([len(bucket) for bucket in self.table])

    def _hash(self, key):
        # Create a hash method that returns the index of the key
        return key % self.size

    def insert(self, package_id, package):
        """Insert package into hash table or update if it already exists"""
        index = self._hash(package_id)
        bucket = self.table[index]

        # Check if package_id is already in the hash table, then update
        for i, (pid, _) in enumerate(bucket):
            if pid == package_id:
                bucket[i] = (package_id, package) # Change this line to add a package object to the bucket
                return

        # If package_id is not in the hash table, append to end of table
        bucket.append((package_id, package))

    def lookup(self, package_id):
        """Return the package associated with the package_id"""
        index = self._hash(package_id)
        bucket = self.table[index]

        for pid, package in bucket:
            if pid == package_id:
                return package
            return None

    def update(self, key, value):
        pass

    def delete(self, key):
        pass