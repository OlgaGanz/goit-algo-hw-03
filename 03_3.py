import time
import os


discs_amount = 3
steps = 0
a = []
b = []
c = []


# init fill
def towers_start_fill(n: int):
    for i in range(0, n):
        a.append(i + 1)
        b.append(0)
        c.append(0)


# visualize towers
def towers_visualization(n: int, src: dict, hlp: dict, dst: dict, colored: int = -1):
    txt = "{:^" + str(n + n * 2) + "}"
    print(txt.format("<-A->"), txt.format("<-B->"), txt.format("<-C->"), "\n")
    for i in range(0, n):

        if src[i] == 0:
            a = "|"
        else:
            a = f"╒{"═"*(2*src[i]-1)}╕"

        if hlp[i] == 0:
            b = "|"
        else:
            b = f"╒{"═"*(2*hlp[i]-1)}╕"

        if dst[i] == 0:
            c = "|"
        else:
            c = f"╒{"═"*(2*dst[i]-1)}╕"

        if colored != -1:
            if colored == src[i]:
                txt_a = "\033[93m{:^" + str(n + n * 2) + "}\x1b[0m"
            else:
                txt_a = "{:^" + str(n + n * 2) + "}"
            if colored == hlp[i]:
                txt_b = "\033[93m{:^" + str(n + n * 2) + "}\x1b[0m"
            else:
                txt_b = "{:^" + str(n + n * 2) + "}"
            if colored == dst[i]:
                txt_c = "\033[93m{:^" + str(n + n * 2) + "}\x1b[0m"
            else:
                txt_c = "{:^" + str(n + n * 2) + "}"

            print(txt_a.format(a), txt_b.format(b), txt_c.format(c))
        else:
            print(txt.format(a), txt.format(b), txt.format(c))

    line = "-" * (n + n * 2) * 3 + "--"
    print(txt.format(line), "\n")
    time.sleep(0.5)


# move values from one list to another
def disc_mover(n, src, dst):
    if src == "A":
        src = a
    elif src == "B":
        src = b
    else:
        src = c

    if dst == "A":
        dst = a
    elif dst == "B":
        dst = b
    else:
        dst = c

    i = 1
    while i <= discs_amount:
        if dst[-i] == 0:
            dst[-i] = src[src.index(n)]
            src[src.index(n)] = 0
            break
        else:
            i += 1


# main hanoi algorithm
def hanoi_towers(n: int, source, destination, helper):
    global steps
    if n > 0:
        steps += 1
        if n == 1:
            print(
                f"\nMove disk \033[93m1\x1b[0m from \033[96m{source}\x1b[0m to \033[96m{destination}\x1b[0m"
            )
            disc_mover(n, source, destination)
            towers_visualization(discs_amount, a, b, c, n)
            return

        hanoi_towers(n - 1, source, helper, destination)

        print(
            f"\nMove disk \033[93m{n}\x1b[0m from \033[96m{source}\x1b[0m to \033[96m{destination}\x1b[0m"
        )
        disc_mover(n, source, destination)
        towers_visualization(discs_amount, a, b, c, n)

        hanoi_towers(n - 1, helper, destination, source)


# input and errors checking
def main():
    os.system("cls" if os.name == "nt" else "clear")
    global discs_amount
    try:
        discs_amount = int(input("\nEnter ammount of disks:-> "))
        if discs_amount <= 0:
            raise ValueError
        elif discs_amount > 5:
            while True:
                answer = input(
                    "\nDiscs amount is pretty high, it will take some time, are you shure? (y/n):--> "
                )
                if answer == "y" or answer == "Y":
                    towers_start_fill(discs_amount)
                    towers_visualization(discs_amount, a, b, c)
                    hanoi_towers(discs_amount, "A", "C", "B")
                    print(
                        f"Task is done, it's took \033[93m{steps}\x1b[0m step{"s" if steps > 1 else ""}\n"
                    )
                    break
                elif answer == "n" or answer == "N":
                    break
        else:
            towers_start_fill(discs_amount)
            towers_visualization(discs_amount, a, b, c)
            hanoi_towers(discs_amount, "A", "C", "B")
            print(
                f"Task is done, it's took \033[93m{steps}\x1b[0m step{"s" if steps > 1 else ""}\n"
            )
    except:
        print("Enter numbers >= 1 only\n")


if __name__ == "__main__":
    main()
