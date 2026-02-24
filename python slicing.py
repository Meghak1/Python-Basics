

---

# Python Slicing — Quick Notes

##  General Syntax

```python
arr[start : stop : step]
```

* `start` → inclusive
* `stop` → exclusive
* `step` → default = 1
* Omitted start = 0
* Omitted stop = end

---

# Basic Rules

```python
nums = [10,20,30,40,50]
```

* `nums[:2]` → `[10,20]`
* `nums[2:]` → `[30,40,50]`
* `nums[1:4]` → `[20,30,40]`
* `nums[:]` → copy of list
* `nums[-1]` → `50` (indexing, not slice)

---

```python
s = "python"
```

* `s[:3]` → `"pyt"`
* `s[3:]` → `"hon"`
* `s[1:5]` → `"ytho"`
* `s[-2:]` → `"on"`
* `s[:-1]` → `"pytho"`

---

# Negative Indexing

```python
nums = [1,2,3,4,5,6,7]
```

* `nums[-3:]` → `[5,6,7]`
* `nums[:-3]` → `[1,2,3,4]`
* `nums[-5:-2]` → `[3,4,5]`
* `nums[1:-1]` → `[2,3,4,5,6]`
* `nums[-1:-4]` → `[]` (start > stop)

---

# Step Slicing

```python
nums = [0,1,2,3,4,5,6,7,8,9]
```

* `nums[::2]` → `[0,2,4,6,8]`
* `nums[1::2]` → `[1,3,5,7,9]`
* `nums[::-1]` → reverse
* `nums[::-2]` → reverse step 2
* `nums[8:2:-1]` → `[8,7,6,5,4,3]`

---

```python
s = "abcdefg"
```

* `s[::3]` → `"adg"`
* `s[::-1]` → `"gfedcba"`
* `s[5:1:-1]` → `"fedc"`

---

# Important Edge Cases

* `arr[3:3]` → `[]`
* `arr[4:1]` → `[]`
* Start > stop with positive step → empty
* `arr[:]` → new copy
* `arr` → same reference

---

# Common Interview Patterns

### Remove first & last

```python
arr[1:-1]
```

### Reverse

```python
arr[::-1]
```

### Rotate right by k

```python
arr[-k:] + arr[:-k]
```

### Split list

```python
mid = len(arr)//2
arr[:mid], arr[mid:]
```

### Swap halves

```python
arr[mid:] + arr[:mid]
```

### Palindrome

```python
s == s[::-1]
```

---

# Golden Rules to Remember

1. Stop index is NOT included
2. Default step = +1
3. Negative step reverses direction
4. start > stop (with + step) → empty
5. `[:]` makes a copy

---

