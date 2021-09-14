import BaseCreateWindow as BaseWin
import tkinter.messagebox as mb
import tkinter as tk
import os
import random
from tkinter import filedialog, DISABLED, NORMAL, LEFT, BOTH
import ExWindow as ExWin


class WorkFile:
    def _fill_up(self, file, count_num: int, min: int, max: int) -> None:
        new_max = int(max / count_num)
        rand = random.randint(min, new_max)
        file.write(str(rand) + ' ')
        for i in range(count_num - 1):
            new_max += int(count_num)
            rand = random.randint((new_max - int(count_num)), new_max)
            if i != count_num - 2:
                file.write(str(rand) + ' ')
            else:
                file.write(str(rand))

    def _fill_down(self, file, count_num: int, max: int) -> None:
        new_max = max - int(count_num)
        new_min = new_max - int(count_num)
        rand = random.randint(new_min, new_max)
        file.write(str(rand) + ' ')
        for i in range(count_num - 1):
            new_max -= int(count_num) // 100000
            new_min -= int(count_num) // 100000
            rand = random.randint(new_min, new_max)
            if i != count_num - 2:
                file.write(str(rand) + ' ')
            else:
                file.write(str(rand))

    def _fill_file(self, file_extension: str, file) -> None:
        min = 1
        max = 50000000
        check = False
        if file_extension == ".up":
            self._fill_up(file, int(self.spin.get()), min, max)
        elif file_extension == ".down":
            self._fill_down(file, int(self.spin.get()), max)
        elif file_extension == ".rand":  # случайная последовательность
            for i in range(int(self.spin.get())):
                file.write(str(random.randint(min, max)) + ' ')
            file.truncate(file.tell() - 1)
        elif file_extension == ".sim":  # одно и то же число
            num = random.randint(min, max)
            for i in range(int(self.spin.get()) - 1):
                file.write(str(num) + ' ')
            file.write(str(num))
        elif file_extension == ".up_down":  # убывающие и возрастающие подпоследовательности
            # print("up_down")
            num_up = int(self.spin1.get())
            num_down = int(self.spin2.get())
            countUpDown = num_up + num_down
            count = int(int(self.spin.get()) / countUpDown)  # общее количество эл-ов в одной подпоследовательности
            if int(self.spin.get()) % countUpDown != 0:
                check = True
                if num_up != 0:
                    self._fill_up(file, count + int(self.spin.get()) % countUpDown, min, max)
                    num_up -= 1
                    if num_up != 0 & num_down != 0:
                        file.write(' ')
                elif num_down != 0:
                    self._fill_down(file, count + int(self.spin.get()) % countUpDown, min)
                    num_down -= 1
                    if num_up != 0 & num_down != 0:
                        file.write(' ')
            while num_up != 0 & num_down != 0:
                num_up -= 1
                file.write(' ')
                self._fill_down(file, count, max)
                num_down -= 1
                file.write(' ')
            while num_up != 0:
                if check:
                    file.write(' ')
                check = True
                self._fill_up(file, count, min, max)
                num_up -= 1
            while num_down != 0:
                if int(self.spin.get()) % countUpDown != 0 or (not check):
                    file.write(' ')
                self._fill_down(file, count, max)
                num_down -= 1
                file.write(' ')

    def _create_file(self, name: str, file_extension: str) -> None:
        directory = r'C:/MyPrograms/Kursach/generation_files'
        files = os.listdir(directory)
        this = name + file_extension
        count = 1
        while this in files:
            count += 1
            this = name + file_extension + '(' + str(count - 1) + ')'
        if count == 1:
            file = open("./generation_files/" + name + file_extension, "w")
        else:
            file = open("./generation_files/" + name + file_extension + '(' + str(count - 1) + ')', "w")

        # сама генерация в файле
        self._fill_file(file_extension, file)

        file.close()


# класс начального окна
class FirstWindow(BaseWin.BaseCreateWindow, WorkFile):

    def __init__(self):
        super().__init__()

        self.iconbitmap(r'./icon.ico')
        # количество созданных файлов
        self.count = 0

        self.check_gen = False

        self.title("Экспериментальное исследование сортировок Merge sort")
        self.geometry('500x400')

        # создание заголовка
        self._create_label("Параметры генерации", 0, 0, 4, 2, "w", "Arial Bold", 14, self)

        self._create_label("Кол-во элементов последовательности:", 0, 1, 12, 2, "w", "Arial Bold", 10, self)
        self.spin = tk.Spinbox(self, from_=2, to=10000000, width=10)
        self.spin.grid(column=0, row=2, padx=16, pady=5, sticky="w")

        self._create_label("Укажите тип последовательности:", 0, 3, 12, 2, "w", "Arial Bold", 10, self)

        chk_state1 = tk.BooleanVar()
        self._create_check_button(chk_state1, 'Отсортированная по возрастанию', 0, 5, 12, 2, "w")

        chk_state2 = tk.BooleanVar()
        self._create_check_button(chk_state2, 'Отсортированная по убыванию', 0, 5, 12, 2, "e")

        chk_state3 = tk.BooleanVar()
        self._create_check_button(chk_state3, 'Случайная', 0, 6, 12, 2, "w")

        chk_state4 = tk.BooleanVar()
        self._create_check_button(chk_state4, 'С многократноповторяющимся \nодним элементом', 0, 6, 7, 2, "e")

        # canvas = tk.Canvas(self)
        # canvas.create_line(16, 25, 400, 25)
        # canvas.grid(column=0, row=7, padx=0, pady=0, columnspan=3, rowspan=5, sticky="n")

        chk_state5 = tk.BooleanVar()
        chk_state5.set(False)
        frame3 = tk.Frame(master=self,
            relief=tk.SUNKEN,
            borderwidth=1)
        frame3.grid(column=0, row=8, padx=5, pady=5)
        self.chk = tk.Checkbutton(master=frame3, text='Состоящая из k возрастающих \n'
                                             'и j убывающих подпоследовательностей', var=chk_state5, state=DISABLED, justify=LEFT)
        self.chk.grid(column=0, row=8, padx=12, pady=2, sticky="w")

        self._create_label("Количество возрастающих \nподпоследовательностей:", 0, 9, 12, 2, "w", "Arial Regular", 10, frame3)
        self.spin1 = tk.Spinbox(master=frame3, from_=0, to=5000000, width=10)
        self.spin1['state'] = tk.DISABLED
        self.spin1.grid(column=0, row=10, padx=16, pady=5, sticky="wn")
        self._create_label("Количество убывающих \nподпоследовательностей:", 1, 9, 12, 2, "w", "Arial Regular", 10, frame3)
        self.spin2 = tk.Spinbox(master=frame3, from_=0, to=5000000, width=10)
        self.spin2['state'] = tk.DISABLED
        self.spin2.grid(column=1, row=10, padx=16, pady=5, sticky="wn")

        # массив с состояниеми чекбоксов
        self.chk_arr = [chk_state1, chk_state2, chk_state3, chk_state4, chk_state5]

        frame4 = tk.Frame(master=self,
            relief=tk.FLAT,
            borderwidth=1)
        frame4.grid(column=0, row=11, padx=5, pady=5)
        self._create_button(frame4, "Сгенерировать \nпоследовательность", "blue",
                            "white", self.__click_generation, 0, 11, 0, 5, "ne", 2, 0, 1)

        self._create_button(frame4, "Эксперимент", "green", "white", self.__click_ex, 1, 11, 10, 5, "nw")

    def __generation(self, num: int) -> None:
        if num == 0:
            self._create_file(self.spin.get(), ".up")
        elif num == 1:
            self._create_file(self.spin.get(), ".down")
        elif num == 2:
            self._create_file(self.spin.get(), ".rand")
        elif num == 3:
            self._create_file(self.spin.get(), ".sim")
        elif num == 4:
            self._create_file(self.spin.get() + '_' + self.spin1.get() + '_' + self.spin2.get(), ".up_down")

    def __click_generation(self) -> None:
        check = False
        check1 = False
        if 1 < int(self.spin.get()) <= 1000000:
            # проверяем количество подпоследовательностей последнего чекбокса
            for i in range(5):
                if self.chk_arr[i].get():
                    if i != 4:
                        check = True
                        self.__generation(i)  # создание файла генерации без подпоследовательностей
                    elif (self.chk_arr[4].get() == True) & (int(self.spin1.get()) +
                                                            int(self.spin2.get()) <= int(self.spin.get()) / 2) \
                            & (int(self.spin1.get()) + int(self.spin2.get()) != 0):
                        self.__generation(i)  # создание файла генерации с подпоследовательностями
                        check = True
                    elif self.chk_arr[4].get():
                        check1 = True

            if check1:
                mb.showerror("Ошибка", "Неправильное количество подпоследовательностей у последнего чек-бокса!")
            elif not check:
                mb.showerror("Ошибка", "Не было выбрано ни одного чек-бокса!")
            else:
                mb.showinfo("Информация", "Последовательность успешно сгенерирована")
                self.check_gen = True
        else:
            mb.showerror("Ошибка", "Неправильное количество элементов последовательности!")

    def __click_ex(self) -> None:
        # Выбор файлов для эксперемента
        tk.Tk().withdraw()

        # отображает только файлы генерации
        files_name = filedialog.askopenfilenames(initialdir="C:\MyPrograms\Kursach\generation_files",
                                                 title="Выбор файлов для эксперемента",
                                                 filetypes=(("Files", "*.up *.up*) *.down *.down*) "
                                                                      "*.rand *.rand*) "
                                                                      "*.sim *.sim*) *.up_down *.up_down*)"),))
        # переходим к новому окну с эксперементом
        if files_name != "":
            # self.withdraw() # скрывает окно
            self.destroy()  # закрытие окна
            ex_window = ExWin.ExWindow(files_name)
            ex_window.resizable(False, False)
            ex_window.mainloop()
        else:
            mb.showwarning("Предупреждение", "Файлы не были выбраны")
