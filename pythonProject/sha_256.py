import hashlib

str_input = input()

result = hashlib.sha256(str_input.encode())
print(result.hexdigest())