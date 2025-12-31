#odd numbrer square

result = [i*i for i in range(11) if i % 2 != 0]

______________________________________________________________
word="hackerrank"
vowels=[c for c in word if c in "aeiou"]
print(vowels)
______________________________________________________________

Create pairs from [1,2,3] where i != j

pairs = [(i, j) for i in [1,2,3] for j in [1,2,3] if i != j]

_______________________________________________________________

Convert [-1, 2, -3, 4] → [0, 2, 0, 4]

result = [0 if i < 0 else i for i in [-1, 2, -3, 4]]
_______________________________________________________________

Outer loop first, inner loop next is the key here

Convert this 2D list:

matrix = [[1, 2], [3, 4], [5, 6]]

Into this 1D list:

[1, 2, 3, 4, 5, 6]


flat = []

for row in matrix:          # row = [1, 2] then [3, 4] then [5, 6]
    for num in row:         # num = 1, 2, 3, 4, 5, 6
        flat.append(num)

print(flat)

List comprehension : 

flat = [num for row in matrix for num in row]

_________________________________________________________________

