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



# for index in range(len(sb)):
#     if sb[index] == "\n":
#         count = 0
#     else:
#         count += 1
#     if count == div


def main():
    print_string("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")


if __name__ == '__main__':
    main()
