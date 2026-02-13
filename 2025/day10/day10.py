import pathlib
import re
import collections

def parse_data(instruction_list) -> tuple[list[str], list[list[int]], list[list[int]]]:
    """
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    """

    leds, wires, powers = [], [], []

    for _, instruction in enumerate(instruction_list):

        leds.append(re.compile(r"\[([\.#]+)\]").findall(instruction)[0])

        wires_tmp = []
        for exp_str in re.compile(r"\(([0-9,]+)\)").findall(instruction):
            wires_tmp.append([int(nb_str) for nb_str in exp_str.split(",")])
        wires.append(wires_tmp)

        powers.append([int(nb_str) for nb_str in re.compile(r"\{([0-9,]+)\}").findall(instruction)[0].split(",")])

    return  leds, wires, powers

def wires_to_masks(wire_schema_list: list[list[int]], len_led: int) -> list[list[bool]]:
    mask_list = []
    for wire_schema in wire_schema_list:
        mask = []
        for i in range(len_led):
            if i in wire_schema:
                mask.append(True)
            else:
                mask.append(False)

        mask_list.append(mask)
        
    return mask_list

def leds_to_masks(leds: list[str])-> list[bool]:
    led_masks = []
    for led_str in leds:
        led_masks.append([True if char == "#" else False for char in led_str])
    return led_masks

def part1(instruction_list) -> int:
    leds, wires, _ = parse_data(instruction_list)
    wire_wasks = []

    for led, wire_schema_list in zip(leds, wires):
        wire_wasks.append(wires_to_masks(wire_schema_list, len(led)))
    
    led_masks = leds_to_masks(leds)

    # Find the minimum number of XOR operation (led / wires)
    

    return 0




def part2(instruction_list) -> int:
    leds, wires, powers = parse_data(instruction_list)
    return 0


if __name__ == "__main__":
    PUZZLE_DIR = pathlib.Path(__file__).parent

    with open(PUZZLE_DIR / "test_input.txt", encoding="utf-8") as f:
        instruction_list: list[str] = f.readlines()
    print(f"Part 1: {part1(instruction_list)}")
    print(f"Part 2: {part2(instruction_list)}")
