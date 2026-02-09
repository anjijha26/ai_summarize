from app.summarizer import summarize

print("Paste the text you want to summarize.")
print("Press ENTER on an empty line to finish.\n")

lines = []

while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

text = "\n".join(lines)

if not text.strip():
    print("No input provided.")
else:
    summary = summarize(text)

    print("\n--- SUMMARY ---")
    print(summary)
