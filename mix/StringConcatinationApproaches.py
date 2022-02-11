# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = ""
for n in range(20):
    nums += str(n)   # slow and inefficient
print(nums)

# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = []
print(type(nums))
for n in range(20):
    nums.append(str(n))
print("".join(nums))  # much more efficient


# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums2 = [str(n) for n in range(20)]
print(type(nums2))
print("".join(nums2))
foo = 'foo'
bar = 'bar'

foobar = '{foo}{bar}'.format(foo=foo, bar=bar) # It is best
print(foobar)