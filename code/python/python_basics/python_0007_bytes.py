s = "This is a string"

b = b"This is a set of bytes"

print(s)

print(b)

encode_string_into_bytes = s.encode("utf-8")
print(encode_string_into_bytes)

decoded_string = encode_string_into_bytes.decode("utf-8")
print (decoded_string)

print(decoded_string == s) 