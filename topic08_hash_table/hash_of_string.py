from hashlib import md5, sha1, sha256

name = "James"

total = 0
for ch in name:
    total += ord(ch)


print(f"Hash of {name} is {total % 10}")

print(md5(name.encode()).hexdigest())

print(sha1(name.encode()).hexdigest())

print(sha256(name.encode()).hexdigest())