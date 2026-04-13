from ArraySet import ArraySet

setA = ArraySet()
setB = ArraySet()

setA.insert('거울')
setA.insert('휴대폰')
setA.insert('물병')

setB.insert('거울')
setB.insert('휴대폰')
setB.insert('손수건')
setB.insert('볼펜')

print("SetA:" ,setA)
print("SetB:", setB)

setB.delete('거울')
print("SetB:", setB)

print("A U B:", setA.union(setB))
print("A ^ B:", setA.intersect(setB))
print("A - B:", setA.difference(setB))
print("A = B:", setA.equals(setB))


