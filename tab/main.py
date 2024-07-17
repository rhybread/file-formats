def main():
    txt = open("txts/like_real_people_do.txt", "r")

    read_lines(txt)

    txt.close()
    return


if __name__ == 'main':
    main()


def read_lines(txt):
    # each string has a list which details what fret to be played at what index
    # each list's elements are tuples in the format (index, fret)
    E, A, D, G, B, e = list()
    index = 0

    for line in txt:
        curr_string = list()

        for char in line:
            match char:     # todo: replace with the defined tunings
                case "|":
                    break
                case 'E':
                    curr_string = E
                    break
                case 'A':
                    curr_string = A
                    break
                case 'D':
                    curr_string = D
                    break
                case 'G':
                    curr_string = G
                    break
                case 'B':
                    curr_string = B
                    break
                case 'e':
                    curr_string = E
                    break
            curr_string.append((index, char))
            index += 1
        index = 0

    return
