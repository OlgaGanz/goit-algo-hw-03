import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, one_line=True, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    if one_line:
        koch_curve(t, order, size)
    else:
        for angle in [120, 120, 120]:
            koch_curve(t, order, size)
            t.right(angle)

    window.mainloop()


def draw_koch_snowflake(order):
    draw_koch_curve(order, False)


def main():
    try:
        recursion_level = 1
        recursion_level = int(
            input("\nInput recursion level (only numbers from 1):--> ")
        )

        if recursion_level <= 0:
            raise ValueError
        elif recursion_level > 3:
            while True:
                answer = input(
                    "\nRecursion level is too high, it will take some time, are you shure? (y/n):--> "
                )
                if answer == "y" or answer == "Y":
                    draw_koch_snowflake(recursion_level)
                    break
                elif answer == "n" or answer == "N":
                    break
        else:
            draw_koch_snowflake(recursion_level)

    except ValueError:
        print("\nYou need to enter only numbers from 1, pls restart\n")


if __name__ == "__main__":
    main()
