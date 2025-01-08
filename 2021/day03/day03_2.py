import pathlib


def get_count_zeros(instruction_list: list[str], idx: int) -> int:
    count_zeros = 0

    for bit_text in instruction_list:
        if bit_text[idx] == "0":
            count_zeros += 1

    return count_zeros


def part2(instruction_list):
    nb_bits = len(instruction_list)

    oxigen_instruction_list = instruction_list
    for i in range(nb_bits):
        if (
            get_count_zeros(oxigen_instruction_list, i)
            > len(oxigen_instruction_list) / 2
        ):
            bit = "0"
        else:
            bit = "1"

        oxigen_instruction_list = [
            bit_text for bit_text in oxigen_instruction_list if bit_text[i] == str(bit)
        ]
        if len(oxigen_instruction_list) == 1:
            break

    co2_instruction_list = instruction_list
    for j in range(nb_bits):
        if get_count_zeros(co2_instruction_list, j) > len(co2_instruction_list) / 2:
            bit = "1"
        else:
            bit = "0"

        co2_instruction_list = [
            bit_text for bit_text in co2_instruction_list if bit_text[j] == str(bit)
        ]
        if len(co2_instruction_list) == 1:
            break

    oxigen_generator_rating_int = int(oxigen_instruction_list[0], 2)
    co2_scrubber_rating_int = int(co2_instruction_list[0], 2)

    print(
        f"Oxigene generator rating: {oxigen_generator_rating_int} (in bits: {oxigen_instruction_list[0]})"
    )
    print(
        f"CO2 scrubber rating: {co2_scrubber_rating_int} (in bits: {co2_instruction_list[0]})"
    )
    return oxigen_generator_rating_int * co2_scrubber_rating_int
    # 1313900 Too high


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.read().splitlines()

    print(f"Part 2: {part2(instruction_list)}")
