import numpy as np
import matplotlib.pyplot as plt

def file_process(s):
    f = open(s, "r")
    lines = f.readlines()
    f.close()
    convert = []
    result = []

    for line in lines:
        for element in line.split():
            convert.append(float(element))
        result.append(convert)
        convert = []

    result = np.array(result)
    return result

result1 = file_process("result1.txt")
result2 = file_process("result2.txt")
result3 = file_process("result3.txt")

time = result1[:,0]
x = result1[:,2]
v = result1[:,3]
plt.plot(x, v, label = "(1,0)")

time = result2[:,0]
x = result2[:,2]
v = result2[:,3]
plt.plot(x, v, label = "(2,0)")

time = result3[:,0]
x = result3[:,2]
v = result3[:,3]
plt.plot(x, v, label = "(0,3)")

plt.legend()
plt.show()

