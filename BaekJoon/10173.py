import sys
while True:
    sentence = sys.stdin.readline().strip()
    if len(sentence) > 80 or sentence == "EOI":
        break

    if "nemo" in sentence.lower():
        print("Found")
    else:
        print("Missing")