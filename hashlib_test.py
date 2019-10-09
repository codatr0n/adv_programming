import hashlib

# ['sha256', 'sha3_384', 'sha1', 'sha384', 'blake2s', 'shake_128', 'sha3_512', 'shake_256', 'blake2b', 'sha3_256', 'md5', 'sha512', 'sha224', 'sha3_224']

line = "010100010010100010010111110101001010"
hash_object = hashlib.md5(line.encode("utf-8"))

print("line: {}\noutput: {}".format(line, hash_object.hexdigest()))
