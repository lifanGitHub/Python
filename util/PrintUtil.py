def print_string(string="", div=20):
    sb = list()
    count = 0
    for c in string:
        sb.append(c)
        if c == "\n":
            count = 0
        else:
            count += 1
        if count == div:
            sb.append('\n')
            count = 0
    print("".join(sb))


def save_string(src="", name=""):
    f = open(name, "w")
    f.write(src)
    f.close()


# for index in range(len(sb)):
#     if sb[index] == "\n":
#         count = 0
#     else:
#         count += 1
#     if count == div


def main():
    print_string(
        "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")


if __name__ == '__main__':
    main()
