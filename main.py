homerseklet = [0, 12, 13, 9, 2, 7]

i = 0
while i < len(homerseklet):
    if i > 0:
        if homerseklet[i - 1] >= homerseklet[i] + 3:
            print(f"Ezen a napon {i + 1}: {homerseklet[i-1]} C° -> {homerseklet[i]} C°")
    i += 1
