# String: Is the sequence of unicode characters
# Bytes: Is the sequence of raw eight bit values

b = bytes([0x41, 0x42, 0x43, 0x44])
print(b)

s = "abcd"
print(s)

# It will not work as we need to first decode te byte
# print(b+s)

s2 = b.decode("utf-8")
print(s+s2)
# abcdABCD


# Now lets learn how to encode a string into bytes
s3 = "This is a test"
b2 = s3.encode("utf-8")
print(b2)
# b'This is a test'

b3 = s.encode("utf-32")
print(b3)
# b'\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00d\x00\x00\x00'
