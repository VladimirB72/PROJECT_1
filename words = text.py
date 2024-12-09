text = "Toto je příklad textu pro analýzu délky slov."
words = text.split()
word_lengths = {}

for word in words:
    length = len(word)
word_lengths[length] = word_lengths.get(length, 0) + 1
word_lengths

# Příklad použití:
result = analyze_text(text)

print(result)