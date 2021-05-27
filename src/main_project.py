# -- coding utf-8 --
__author__ = 'Alexander Mateyko'

from tkinter import *
from tkinter import messagebox


class Hover_Button(Button):

    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


def main():
    window = Tk()
    window.geometry("850x600+530+170")
    window.title('Utilities calculator')
    window["bg"] = "#292929"
    window.overrideredirect(1)
    window.wm_attributes('-topmost', 1)
    window.protocol("WM_DELETE_WINDOW", program_exit)

    frame = Frame(window, relief=RAISED, borderwidth=10)
    frame["bg"] = "#434343"
    frame.pack(fill=BOTH, expand=True)

    button_settings = Hover_Button(window, width=16, text="Налаштування", bg='gray22', fg='white', font='Arial 17',
                                   activebackground='#A5A5A5')
    button_settings.configure(command=settings)
    button_settings.pack(side='left', padx=15, pady=10)

    button_exit = Hover_Button(window, width=16, text="Завершити роботу", bg='gray22', fg='white', font='Arial 17',
                               activebackground='#A5A5A5')
    button_exit.configure(command=program_exit)
    button_exit.pack(side='right', padx=15, pady=10)

    button_calculate = Hover_Button(window, width=16, text="Розрахувати", bg='gray22', fg='white', font='Arial 17',
                                    activebackground='#A5A5A5')
    button_calculate.configure(command=calculate)
    button_calculate.pack(side='top', padx=15, pady=10)

    window.mainloop()


def calculate():
    rate_dict = {}
    with open('rate_dictionary.txt') as file:
        for i in file.readlines():
            key, val = i.strip().split(':')
            rate_dict[key] = val
    print(rate_dict)


def settings():
    global set_win
    set_win = Tk()
    set_win.geometry("350x550+130+200")
    set_win.title('Utilities calculator settings')
    set_win["bg"] = "#292929"

    set_win.lift()
    set_win.attributes('-topmost', True)
    set_win.after_idle(set_win.attributes, '-topmost', True)

    frame = Frame(set_win, relief=RAISED, borderwidth=5)
    frame["bg"] = "#434343"
    frame.pack(fill=BOTH, expand=True)

    button_save = Hover_Button(set_win, text="Зберегти налаштування", bg='gray22', fg='white', font='Arial 17',
                               activebackground='#A5A5A5')
    button_save.configure(command=settings_save)
    button_save.pack(side='top', padx=15, pady=10)


def program_exit():
    if messagebox.askyesno(title='Завершення роботи',
                           message='Ви впевнені що хочете завершити роботу з програмою?'):
        exit()


def settings_save():
    if messagebox.askyesno(title='Зберегти налаштування',
                           message='Зберегти внесенні зміни?'):
        rate_changing()
        set_win.destroy()


def rate_changing():
    try:
        rate_dict = dict(gas=0, water=0, electricity=0)
        with open('rate_dictionary.txt', 'w') as file:
            for key, val in rate_dict.items():
                file.write('{}:{}\n'.format(key, val))
    except FileNotFoundError:
        print('Файл не знайдено. Створено новий файл з тарифами')
    except IOError:
        print('Файл не знайдено. Створено новий файл з тарифами')


if __name__ == '__main__':
    main()
