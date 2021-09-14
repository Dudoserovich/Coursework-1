import tkinter as tk


# класс с созданием базовых объектов
from tkinter import LEFT


class BaseCreateWindow(tk.Tk):
    def __init__(self):
        super().__init__()

    def _create_label(self, text, column, row, padx, pady, sticky, font_style, font_size,  master, state=tk.NORMAL) -> None:
        lbl = tk.Label(master=master, text=text, font=(font_style, font_size), justify=LEFT, state=state)
        lbl.grid(column=column, row=row, padx=padx, pady=pady, sticky=sticky)

    def _create_check_button(self, chk_state, text, column, row, padx, pady, sticky) -> None:
        chk_state.set(False)
        chk = tk.Checkbutton(self, text=text, var=chk_state, justify=LEFT, command=self.__switchButtonState)
        chk.grid(column=column, row=row, padx=padx, pady=pady, sticky=sticky)

    def _create_button(self, master, text, bg, fg, command, column, row, padx, pady, sticky, height=2, width=17, columnspan=2) -> None:
        btn = tk.Button(master=master, text=text, bg=bg, fg=fg, command=command, height=height, width=width)
        btn.grid(column=column, row=row, padx=padx, pady=pady, sticky=sticky, columnspan=columnspan)

    # меняем состояние 5го типа
    def __switchButtonState(self):
        check = False
        for i in range(len(self.chk_arr) - 1):
            if self.chk_arr[i].get():
                check = True
        if check:
            if self.chk['state'] == tk.DISABLED:
                self.chk['state'] = tk.NORMAL
                self.spin1['state'] = tk.NORMAL
                self.spin2['state'] = tk.NORMAL
        else:
            self.chk['state'] = tk.DISABLED
            self.spin1['state'] = tk.DISABLED
            self.spin2['state'] = tk.DISABLED
        # self.but.invoke()
        # print(self.chk['state'])