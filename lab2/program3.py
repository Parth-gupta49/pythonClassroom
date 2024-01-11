import re


# Regex functions
print("**Regex Functions**")


text = "My number is 12345. My name is John"


print("\n- re.search(pattern, string):")
match = re.search(r"\s", text)  # Find the first white space occurrence
print("The first white-space character is located in position:", match.start())


print("\n- re.findall(pattern, string):")
matches = re.findall("[A-M]", text)  # Find words between[A-M]
print("Matches:", matches)


print("\n- re.split(pattern, string):")
split_text = re.split(r"\s", text)  # Split by whitespace
print("Split text:", split_text)


print("\n- re.sub(pattern, repl, string):")
new_text = re.sub(r"\s", "$", text)  # Replace digits with "number"
print("New text:", new_text)


# Metacharacters
print("\n**Metacharacters**")


print("\n- [.]: Matches any single character except newline")
print(re.findall(r"..", "ab12cd"))


print("\n- [^]: Matches the beginning of the string")
x = re.findall("^My", text)
if x:
  print("Yes, the string starts with 'My'")
else:
  print("No match")


print("\n- [$]: Matches the end of the string")
x = re.findall("John$", text)
if x:
  print("Yes, the string ends with 'John'")
else:
  print("No match")


print("\n- []: Matches a character class")
print(re.findall(r"[aeiou]", "hello world"))


print("\n- |: Matches either expression")
print(re.findall(r"hello|earth", "hello world"))


print("\n- (): Groups expressions")
print(re.findall(r"(\w+) (\w+)", "hello world"))


print("\n- \: Signals a special sequence")
x = re.findall("\d", text)
print(x)


txt = "hello planet"


print("\n- [*]: Zero or more occurrences")
# Search for a sequence that starts with "he", followed by 0 or more (any) characters, and an "o":
print(re.findall(r"he.*o", txt))


print("\n- [+]: One or more occurrences")
# Search for a sequence that starts with "he", followed by 1 or more (any) characters, and an "o":
print(re.findall(r"he.+o", txt))


print("\n- [?]: Zero or one occurrences")
# Search for a sequence that starts with "he", followed by zero or one (any) characters, and an "o":
print(re.findall(r"he.?o", txt))


print("\n- {}: Exactly the specified number of occurrences")
# Search for a sequence that starts with "he", followed exactly by 2 (any) characters, and an "o":
print(re.findall(r"he.{2}o", txt))
