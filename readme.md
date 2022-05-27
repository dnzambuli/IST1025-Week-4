### Bytes and Booleans in Python

#### Bytes 
Computers read data in the form of binary code which can be expressed as 1 and 0
There are many ways to encode computer data. one is hex code data 

an example of hex code 
```hex
00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0E 0F
23 57 6F 72 69 6E 67 20 77 69 74 68 20 62 69
6E 61 72 79 20 66 69 6C 65 73 0A +
```
which translates to text 
```text
Working with binary data +
```

Bytes are just 8 bits of 1 and 0 that are used to encode text used in modern browsers. 

##### Python and Bytes 
Python provides a built in functions and special characters to deal with hex encoded variables this are based on [UTF8 encoding](https://en.wikipedia.org/wiki/UTF-8).
These are:
- The built in function **bytes()** to handle cases of bytes to be used in our code.
  ```python
  '''
  create a variable x 
  call bytes which takes:
    * the length of the bytes (hex values expresed as x\(0-9/ A-F)
    * the type of encoding (optional)
    * the error to raise in the event of unexpected input
  *** variable x is immutable ***
  '''
  x = bytes(4, 'utf-8', ValueError('invalid input'))
  print(x)
  ```
  outputs on terminal
  ```bash
  C:\Users\user> b'\x00\x00\x00\x00'
  ```

- The special character **b'*sample string*'** for inline formating of strings that may contain byte data like [emoticons](https://unicode.org/emoji/charts/full-emoji-list.html) and non-english language characters [utf-8](https://www.utf8-chartable.de/).

```python
'''
make a variable x 
it holds a string with an emoji in it 
emoji code U+1F603
* b encodes the data so that the code U+1F603 is converted to utf8
* str converts byte data to strings
* bytes converts hex encoded data to computer readable immutable bytes
'''
x = b'this is a smiley face:\n U+1F603'
print(str(bytes(x))
```
output
```
C:\Users\user> b'this is a smiley face:\n U+1F603'
```
**Notice** the new line character is also output

### Booleans
The only logical data types of python that come built in 
```Python 
'''
* True - incicates that a statement will pass
* False - indicates a statement will fail 
note they start with capital letters 
'''
a = 5 
b = 6 
a == b # False 
a == 5 # True 
a != b # True 
a < b  # True 
a > b # False 
```