with open("./day03/input.txt") as f:
    instruction_list = f.read().splitlines()

bit_len = len(instruction_list[0])
nb_bits = len(instruction_list)
count_zeros = [0] * bit_len

for bit_text in instruction_list:
    for i, bit in enumerate(bit_text):
        if bit == "0":
            count_zeros[i] += 1

final_bit = [0 if nb_zeros > nb_bits / 2 else 1 for nb_zeros in count_zeros]
final_bit_inverse = [1 if nb_zeros > nb_bits / 2 else 0 for nb_zeros in count_zeros]
gamma_rate = int("".join([str(i) for i in final_bit]), 2)
epsilon_rate = int("".join([str(i) for i in final_bit_inverse]), 2)

print(f"Gamma rate: {gamma_rate} (in bits: {''.join([str(i) for i in final_bit])})")
print(
    f"Epsilon rate: {epsilon_rate} (in bits: {''.join([str(i) for i in final_bit_inverse])})"
)
print(f"Result: {gamma_rate * epsilon_rate}")
