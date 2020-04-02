#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
from quadratic_equation import quadratic_equation

def main():
    # create a main window
    window  = tkinter.Tk()
    window.title("Quadratic equation")
    window.geometry('350x200')

    tkinter.Label(window, text='In ax^2 + bx + c = 0 please specify a, b and c:').grid(row = 0, column = 0, columnspan = 2)
    tkinter.Label(window, text='a: ').grid(row=1, column=0)
    tkinter.Label(window, text='b: ').grid(row=2, column=0)
    tkinter.Label(window, text='c: ').grid(row=3, column=0)

    a = tkinter.Entry(window, width=15)
    a.grid(column=1, row=1)
    a.focus() # Set focus to entry widget

    b = tkinter.Entry(window, width=15)
    b.grid(column=1, row=2)

    c = tkinter.Entry(window, width=15)
    c.grid(column=1, row=3)

    output = tkinter.Label(window)
    output.grid(row=4, column=1)

    def clicked():
        if not a.get().isdigit():
            output.configure(text = "Invalid input")
            return

        elif not b.get().isdigit():
            output.configure(text = "Invalid input")
            return

        elif not c.get().isdigit():
            output.configure(text = "Invalid input")
            return

        answer = quadratic_equation(int(a.get()), int(b.get()), int(c.get()))

        if not answer:
            output.configure(text = "No solution, sorry")

        elif isinstance(answer, dict):
            output.configure(text = "x1 = " + str(answer["x1"]) + ", " + "x2 = " + str(answer["x2"]))

        else:
            output.configure(text = "x = " + str(answer))

    tkinter.Button(window, text="Calulate", command=clicked).grid(column=0, row=4)

    window.mainloop()

if __name__ == '__main__':
    main()