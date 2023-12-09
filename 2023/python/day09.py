from operator import sub


def seq_sub(seq):
    return list(map(sub, seq[1:], seq))


def main():
    with open("../inputs/09", "r") as f:
        seq = f.read()
        lines = seq.split("\n")

    forward = 0
    backward = 0
    for line in lines:
        seq = list(map(int, line.split(" ")))
        seqs = [seq]
        while not all([x == 0 for x in seq]):
            seq = seq_sub(seq)
            seqs.append(seq)

        forward += sum([seq[-1] for seq in seqs])

        r = 0
        for seq in reversed(seqs[:-1]):
            r = seq[0] - r
        backward += r

    print(forward)
    print(backward)


if __name__ == "__main__":
    main()
