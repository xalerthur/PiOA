import numpy as np

# Считаем количество операций умножения (исключая умножение на 0, на 1 и 10 (степени 10))
count = 0
lastCount = 0

def isNorm(a):
	if abs(a) == 1 or abs(a) % 10 == 0:
		return False
	return True

def amountOfOp(matA_, matB_):
	global count
	global lastCount
	lastCount = 0
	if isNorm(matA_[0, 0]) and isNorm(matB_[0, 0]):
		lastCount += 1
	if isNorm(matA_[0, 1]) and isNorm(matB_[1, 0]):
		lastCount += 1
	if isNorm(matA_[0, 0]) and isNorm(matB_[0, 1]):
		lastCount += 1
	if isNorm(matA_[0, 1]) and isNorm(matB_[1, 1]):
		lastCount += 1
	if isNorm(matA_[1, 0]) and isNorm(matB_[0, 0]):
		lastCount += 1
	if isNorm(matA_[1, 1]) and isNorm(matB_[1, 0]):
		lastCount += 1
	if isNorm(matA_[1, 0]) and isNorm(matB_[0, 1]):
		lastCount += 1
	if isNorm(matA_[1, 1]) and isNorm(matB_[1, 1]):
		lastCount += 1
	count += lastCount
matA = np.matrix( [
	[0, 1, 2, -1],
	[3, 2, 0, 1],
	[1, -1, 2, 0],
	[1, 2, 3, 1]
] )
matB = np.matrix( [
	[0, -1, 1, 1],
	[3, 2, 0, 2],
	[2, 1, -2, 3],
	[1, 3, 2, 0]
] )

matA11 = np.array( [[matA[0, 0], matA[0, 1]], [matA[1, 0], matA[1, 1]]] )
matA12 = np.array( [[matA[0, 0 + 2], matA[0, 1 + 2]], [matA[1, 0 + 2], matA[1, 1 + 2]]] )
matA21 = np.array( [[matA[0 + 2, 0], matA[0 + 2, 1]], [matA[1 + 2, 0], matA[1 + 2, 1]]] )
matA22 = np.array( [[matA[0 + 2, 0 + 2], matA[0 + 2, 1 + 2]], [matA[1 + 2, 0 + 2], matA[1 + 2, 1 + 2]]] )

matB11 = np.array( [[matB[0, 0], matB[0, 1]], [matB[1, 0], matB[1, 1]]] )
matB12 = np.array( [[matB[0, 0 + 2], matB[0, 1 + 2]], [matB[1, 0 + 2], matB[1, 1 + 2]]] )
matB21 = np.array( [[matB[0 + 2, 0], matB[0 + 2, 1]], [matB[1 + 2, 0], matB[1 + 2, 1]]] )
matB22 = np.array( [[matB[0 + 2, 0 + 2], matB[0 + 2, 1 + 2]], [matB[1 + 2, 0 + 2], matB[1 + 2, 1 + 2]]] )

print("A: " + str(matA.flatten()))
print("A_11: " + str(matA11.flatten()))
print("A_12: " + str(matA12.flatten()))
print("A_21: " + str(matA21.flatten()))
print("A_22: " + str(matA22.flatten()))
print("B: " + str(matB.flatten()))
print("B_11: " + str(matB11.flatten()))
print("B_12: " + str(matB12.flatten()))
print("B_21: " + str(matB21.flatten()))
print("B_22: " + str(matB22.flatten()))

print("=====================\n")
print("D_0 = ( A_11 + A_22 ) * ( B_11 + B_22 )")
print("D_0 = ( " + str(matA11.flatten()) + " + " + str(matA22.flatten()) + " ) * ( " + str(matB11.flatten()) + " + " + str(matB22.flatten()) + " )")
print("D_0 = ( " + str((matA11 + matA22).flatten()) + " ) * ( " + str((matB11 + matB22).flatten()) + " )")
D_0 = np.dot((matA11 + matA22), (matB11 + matB22))
print("D_0 = " + str(D_0.flatten()))
amountOfOp((matA11 + matA22),  (matB11 + matB22))
print("Amount of muls (without 0, 1 and 10) = " + str(lastCount))

print("=====================\n")
print("D_1 = ( A_12 - A_22 ) * ( B_21 + B_22 )")
print("D_1 = ( " + str(matA12.flatten()) + " - " + str(matA22.flatten()) + " ) * ( " + str(matB21.flatten()) + " + " + str(matB22.flatten()) + " )")
print("D_1 = ( " + str((matA12 - matA22).flatten()) + " ) * ( " + str((matB21 + matB22).flatten()) + " )")
D_1 = np.dot((matA12 - matA22), (matB21 + matB22))
print("D_1 = " + str(D_1.flatten()))
amountOfOp((matA12 - matA22),  (matB21 + matB22))
print("Amount of muls (without 0, 1 and 10) = " + str(lastCount))

print("=====================\n")
print("D_2 = ( A_21 - A_11 ) * ( B_11 + B_12 )")
print("D_2 = ( " + str(matA21.flatten()) + " - " + str(matA11.flatten()) + " ) * ( " + str(matB11.flatten()) + " + " + str(matB12.flatten()) + " )")
print("D_2 = ( " + str((matA21 - matA11).flatten()) + " ) * ( " + str((matB11 + matB12).flatten()) + " )")
D_2 = np.dot((matA21 - matA11), (matB11 + matB12))
print("D_2 = " + str(D_2.flatten()))
amountOfOp((matA21 - matA11),  (matB11 + matB12))
print("Amount of muls (without 0, 1 and 10) = " + str(lastCount))

print("=====================\n")
print("D_3 = ( A_11 + A_12 ) * B_22")
print("D_3 = ( " + str(matA11.flatten()) + " + " + str(matA12.flatten()) + " ) * ( " + str(matB22.flatten()) + " )")
print("D_3 = ( " + str((matA11 + matA12).flatten()) + " ) * ( " + str((matB22).flatten()) + " )")
D_3 = np.dot((matA11 + matA12), matB22)
print("D_3 = " + str(D_3.flatten()))
amountOfOp((matA11 + matA12),  matB22)
print("Amount of muls (without 0, 1 and 10) = " + str(lastCount))

print("=====================\n")
print("D_4 = A_11 * ( B_12 - B_22 )")
print("D_4 = ( " + str(matA11.flatten()) + " + ) * ( " + str(matB12.flatten()) + " - " + str(matB22.flatten()) + " )")
print("D_4 = ( " + str((matA11).flatten()) + " ) * ( " + str((matB12 - matB22).flatten()) + " )")
D_4 = np.dot(matA11, (matB12 - matB22))
print("D_4 = " + str(D_4.flatten()))
amountOfOp(matA11, (matB12 - matB22))
print("Amount of muls (without 0, 1 and 10) = " + str(lastCount))

print("=====================\n")
print("D_5 = A_22 * ( B_21 - B_11 )")
print("D_5 = ( " + str(matA22.flatten()) + " + ) * ( " + str(matB21.flatten()) + " - " + str(matB11.flatten()) + " )")
print("D_5 = ( " + str((matA22).flatten()) + " ) * ( " + str((matB21 - matB11).flatten()) + " )")
D_5 = np.dot(matA22, (matB21 - matB11))
print("D_5 = " + str(D_5.flatten()))
amountOfOp(matA22, (matB21 - matB11))
print("Amount of muls (without 0, 1 and 10) = " + str(lastCount))

print("=====================\n")
print("D_6 = ( A_21 + A_22 ) * B_11")
print("D_6 = ( " + str(matA21.flatten()) + " + " + str(matA22.flatten()) + " ) * ( " + str(matB11.flatten()) + " )")
print("D_6 = ( " + str((matA21 + matA22).flatten()) + " ) * ( " + str((matB11).flatten()) + " )")
D_6 = np.dot((matA21 + matA22), matB11)
print("D_6 = " + str(D_6.flatten()))
amountOfOp((matA21 + matA22),  matB11)
print("Amount of muls (without 0, 1 and 10) = " + str(lastCount))

S11 = D_0 + D_1 - D_3 + D_5
S12 = D_3 + D_4
S21 = D_5 + D_6
S22 = D_0 + D_2 + D_4 - D_6

result = np.array( [[S11[0, 0], S11[0, 1], S12[0, 0], S12[0, 1]],
					[S11[1, 0], S11[1, 1], S12[1, 0], S12[1, 1]],
					[S21[0, 0], S21[0, 1], S22[0, 0], S22[0, 1]],
					[S21[1, 0], S21[1, 1], S22[1, 0], S22[1, 1]]])

print('Answer: \n' + str(result) + "\n")
print('Amount of steps: ' + str(count))