text = input().split()
text.sort(key=len)
print(" ".join(text))