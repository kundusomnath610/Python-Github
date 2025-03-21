s1 = "This is a test. This test is simple. ".replace(".", " ").split()
di = {}

for i in s1:
    if i in di:
        di[i] = di[i] + 1
    else:
        di[i] = 1

for key in di.keys():
    print(f"{key}: {di[key]}")