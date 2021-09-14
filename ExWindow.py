from tkinter import ttk

import tkinter as tk

import BaseCreateWindow as BaseWin
import NaturalMerge as NatMerge
import SimpleMerge as SimMerge
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# класс, позволяющий работать с файлом(читать все числа из него и записывать в файл)
class ReadWriteFile:
    def _write_file(self, file, temp_array) -> None:
        for j in range(len(temp_array)):
            file.write(str(temp_array[j]) + ' ')
        file.truncate(file.tell() - 1)

    def _read_file(self, file_name: str):
        with open(file_name) as f:
            array = f.read().split()
            array = list(map(int, array))
        return array


# окно эксперемента
class ExWindow(BaseWin.BaseCreateWindow, ReadWriteFile):
    def __init__(self, files_name: str):  # filename - строка со всеми выбранными файлами для эксперемента
        super().__init__()
        self.withdraw()
        self.iconbitmap(r'./icon.ico')
        times_ss = []
        times_ns = []
        SM = SimMerge.SimpleMerge()
        NM = NatMerge.NaturalMerge()
        self.title("Диаграммы работы сортировок")
        self.geometry('1000x600')

        self.tab_control = ttk.Notebook(self)

        self.time = ttk.Frame(self.tab_control)
        self.comparisons = ttk.Frame(self.tab_control)
        self.permutations = ttk.Frame(self.tab_control)

        self.tab_control.add(self.time, text='Время')
        self.tab_control.add(self.permutations, text='Перестановки')
        self.tab_control.add(self.comparisons, text='Сравнения')
        self.tab_control.pack(expand=1, fill='both')

        # print(files_name)
        # сортируем каждый из файлов двумя сортировками и записываем в соответсвующие вектора
        comparision_ss = []
        comparision_ns = []

        permutations_ns = []
        permutations_ss = []
        for i in range(len(files_name)):
            # сортировка с помощью simple sort всех выбранных файлов
            start = time.time()
            array_file = self._read_file(files_name[i])
            temp_array = SM.merge_sort(array_file)

            # запись в файл
            file = open(files_name[i][:22] + 'experiment_files' + '/' + files_name[i][39:] + "_simple_merge.txt", "w")
            self._write_file(file, temp_array)

            end = time.time()
            t = round(float(format((end - start) - ((end - start) // 60) * 60)), 3)
            times_ss.append(t)  # время в секундах
            comparision_ss.append(SM.comparison)
            permutations_ss.append(SM.permutation)
            SM.comparison = 0
            SM.permutation = 0
            # print('comparison:')
            # print(comparision_ss)
            # print(times_ss)

            # сортировка с помощью natural sort всех выбранных файлов
            start = time.time()
            temp_array = NM.natural_sort(array_file)

            # запись в файл
            file = open(files_name[i][:22] + 'experiment_files' + '/' + files_name[i][39:] + "_natural_merge.txt", "w")
            self._write_file(file, temp_array)

            end = time.time()
            t = round(float(format((end - start) - ((end - start) // 60) * 60)), 3)
            times_ns.append(t)  # время в секундах
            comparision_ns.append(NM.comparison)
            permutations_ns.append(NM.permutation)
            NM.comparison = 0
            NM.permutation = 0

        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

        # запоминаем короткие имена файлов
        short_files_name = []
        for i in range(len(files_name)):
            if len(files_name[i]) - 39 <= 10:
                short_files_name.append(files_name[i][39:])
            elif len(files_name[i]) - 39 <= 20:
                short_files_name.append(files_name[i][39:49] + '\n' + files_name[i][49:])
            elif len(files_name[i]) - 39 <= 30:
                short_files_name.append(files_name[i][39:49] + '\n' +
                                        files_name[i][49:59] + '\n' + files_name[i][59:])
            elif len(files_name[i]) - 39 > 30:
                short_files_name.append(files_name[i][39:49] + '\n' +
                                         files_name[i][49:59] + '\n' + files_name[i][59:69] + '\n' + files_name[i][69:])
        # задаём диаграмму time
        self.set_diagrams_with_x(axes, short_files_name, times_ns, times_ss)
        self.create_diagram(axes, fig, "время в секундах", self.time, "Время работы сортировок:")

        # задаём диаграмму сравнений
        fig1, axes1 = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
        self.set_diagrams_with_x(axes1, short_files_name, comparision_ns, comparision_ss)
        self.create_diagram(axes1, fig1, "количество сранений", self.comparisons, "Число сравнений в сортировках:")

        # задаём диаграмму перестановок
        fig2, axes2 = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
        self.set_diagrams_with_x(axes2, short_files_name, permutations_ns, permutations_ss)
        self.create_diagram(axes2, fig2, "количество перестановок", self.permutations, "Число перестановок "
                                                                                       "в сортировках:")

        print(str(short_files_name) + str(times_ns) + str(times_ss) + '/сравнения: ' + str(comparision_ns)
              + str(comparision_ss) + '/перестановки: ' + str(permutations_ns) + str(permutations_ss))

        self.deiconify()
        # сохраняем результирующую диаграмму (нужно будет убрать и удалить папку result_sort)
        # files = os.listdir('./result_sort/')
        # this = 'result.png'
        # count = 1
        # while this in files:
        #     count += 1
        #     this = 'result' + '(' + str(count - 1) + ')' + '.png'
        # if count == 1:
        #     fig.savefig('./result_sort/result' + '.png')
        # else:
        #     fig.savefig('./result_sort/result' + '(' + str(count - 1) + ')' + '.png')

    def set_diagrams_with_x(self, axes, short_files_name, times_ns, times_ss):
        axes[0].set_title('Простое слияние', fontsize=12)
        axes[0].barh(short_files_name, times_ss, color='green', label='простое слияние', alpha=0.8)
        axes[1].set_title('Естественное слияние', fontsize=12)
        axes[1].barh(short_files_name, times_ns, color='blue', label='естественное слияние', alpha=0.8)
        axes[0].tick_params(labelleft='off', left=False)
        axes[1].tick_params(labelleft='off', left=False)

    def create_diagram(self, axes, fig, x_name: str, master, text_head: str):
        canvas = FigureCanvasTkAgg(fig, master=master)
        plot_widget = canvas.get_tk_widget()
        lbl = tk.Label(master, text=text_head, font=("Arial Bold", 14))
        lbl.grid(column=0, row=0, padx=4, pady=2, sticky="w")
        # self._create_label("Время работы сортировок:", 0, 0, 4, 2, "w", "Arial Bold", 14)
        axes[0].set_xlabel(x_name)
        axes[0].set_ylabel("наименование файла")
        axes[1].set_xlabel(x_name)
        axes[1].set_ylabel("наименование файла")
        plt.subplots_adjust(wspace=0.5, hspace=0)
        # рисуем диаграммы
        plot_widget.grid(row=1, column=0, padx=16, pady=2, sticky="wn")
