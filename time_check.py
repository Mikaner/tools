import time
length = int(1e6)
output = ""
time.time()

start = time.time()
for i in range(length):
    if i % 2:
        output = "odd"
    else:
        output = "even"
end = time.time()
print(end-start)

start = time.time()
for i in range(length):
    output = "odd"*(i%2) or "even"
end = time.time()
print(end-start)