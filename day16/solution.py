from functools import reduce

from read_input import read_input


def hex_to_bin(filename):
    hex_bin = {"0": "0000",
               "1": "0001",
               "2": "0010",
               "3": "0011",
               "4": "0100",
               "5": "0101",
               "6": "0110",
               "7": "0111",
               "8": "1000",
               '9': "1001",
               "A": "1010",
               "B": "1011",
               "C": "1100",
               "D": "1101",
               "E": "1110",
               "F": "1111",
               }
    return "".join(list(map(lambda x: hex_bin[x], read_input(filename)[0])))


def process_result(type_id, result):
    if type_id == 0:
        return sum(result)
    if type_id == 1:
        return reduce(lambda a, b: a * b, result)
    if type_id == 2:
        return min(result)
    if type_id == 3:
        return max(result)
    if type_id == 5:
        return 1 if result[0] > result[1] else 0
    if type_id == 6:
        return 1 if result[0] < result[1] else 0

    return 1 if result[0] == result[1] else 0


def get_packet_value(packet):
    this_typeid = int(packet[3:6], 2)
    packet = packet[6:]
    if this_typeid == 4:
        return handle_literal(packet)

    if packet[0] == "1":
        result, packet = handle_by_number(packet)
        return process_result(this_typeid, result), packet

    result, packet = handle_by_length(packet)
    return process_result(this_typeid, result), packet


def handle_by_length(packet):
    result = []
    sub_packets_length = int(packet[1:16], 2)
    packet = packet[16:]
    stop_at_len = len(packet) - sub_packets_length
    while len(packet) > stop_at_len:
        value, packet = get_packet_value(packet)
        result.append(value)
    return result, packet


def handle_by_number(packet):
    result = []
    sub_packets = int(packet[1:12], 2)
    packet = packet[12:]
    for sub_packet in range(sub_packets):
        value, packet = get_packet_value(packet)
        result.append(value)
    return result, packet


def handle_literal(packet):
    keep_reading = True
    value = []
    while keep_reading:
        value.append(packet[:5][1:5])
        keep_reading = packet[0] == "1"
        packet = packet[5:]
    return int("".join(value), 2), packet


def process(filename):
    packet = hex_to_bin(filename)
    return get_packet_value(packet)


if __name__ == '__main__':
    print(process("input.txt")[0])
