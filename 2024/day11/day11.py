from collections import Counter

def blink(nb_counter: Counter) -> Counter:
    tmp_counter = Counter()
    for nb, count in nb_counter.items():
        if count == 0:
            continue

        if nb == "0":
            tmp_counter["1"] += nb_counter[nb]
        elif len(nb) % 2 == 0: 
            tmp_counter[str(int(nb[: len(nb) // 2]))] += nb_counter[nb]
            tmp_counter[str(int(nb[len(nb) // 2 :]))] += nb_counter[nb]
        else:
            tmp_counter[str(int(nb) * 2024)] += nb_counter[nb]

    return tmp_counter

with open("./2024/day11/input.txt", encoding="utf-8") as f:
    instruction_list: list[str] = f.readlines()

nb_counter = Counter(instruction_list[0].strip().split(" "))

len_nb_list = []

for j in range(75):
    nb_counter = blink(nb_counter)
    len_nb_list.append(len(nb_counter.keys()))

print(sum(nb_counter.values()))
