with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("\n", " ")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)