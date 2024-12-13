file = open("input_test.txt","r")
inputs = file.readlines()
file.close()

tokens = 0
for i in range(0,len(inputs),4):
    (ax, ay) = map(int,inputs[i][12:].replace("\n","").split(", Y+"))
    (bx, by) = map(int, inputs[i+1][12:].replace("\n","").split(", Y+"))
    (px, py) = map(int,inputs[i+2][9:].replace("\n","").split(", Y="))
    px += 10000000000000
    py += 10000000000000
    apresses = ((px * by) - (py * bx)) / ((ax * by) - (ay * bx))
    bpresses = (px - (apresses * ax)) / bx
    if round(apresses) == apresses and round(bpresses) == bpresses:
        tokens += int((3*apresses) + bpresses)

print(tokens) 