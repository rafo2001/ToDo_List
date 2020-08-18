word = input()
result = None
for letter in range(len(word) // 2):
    if word[letter] != word[-1 * (letter + 1)]:
        result = "Not palindrome"
        break
if result is None:
    result = "Palindrome"
print(result)