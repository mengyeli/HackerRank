X = input()
print(any(ch.isalnum() for ch in X))
print(any(ch.isalpha() for ch in X))
print(any(ch.isdigit() for ch in X))
print(any(ch.islower() for ch in X))
print(any(ch.isupper() for ch in X))