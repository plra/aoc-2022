from p1 import cmp

DIV_1, DIV_2 = [[2]], [[6]]


def read_input(filename):
    with open(filename) as f:
        packets = [eval(packet_str) for packet_str in f.read().split()]
        packets.append(DIV_1)
        packets.append(DIV_2)
        return packets


def insert_packet(packets, p):
    for i, q in enumerate(packets):
        if cmp(p, q) == -1:
            packets.insert(i, p)
            return
    packets.append(p)


# Insertion sort
def order_packets(packets):
    ordered_packets = []
    for p in packets:
        insert_packet(ordered_packets, p)
    return ordered_packets


if __name__ == "__main__":
    packets = read_input("input.txt")
    ordered_packets = order_packets(packets)
    decoder_key = (ordered_packets.index(DIV_1) + 1) * (
        ordered_packets.index(DIV_2) + 1
    )
    print(decoder_key)
