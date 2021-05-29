# -- coding utf-8 --
__author__ = 'Alexander Mateyko'

from tkinter import *
from tkinter import messagebox


class Hover_Button(Button):
    """ The Class that controls the highlighting of buttons on hover  """

    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


class Main_Menu(Frame):
    """ The Class that defines the appearance of the Main menu and properties of the Main menu buttons """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Utilities calculator')
        self.master.wm_attributes('-topmost', True)
        self.configure(background="#292929")
        self.pack(fill=BOTH, expand=True)

        global button_settings
        global entry_gas_main
        global entry_water_main
        global entry_electricity_main
        global label_gas_calculated
        global label_water_calculated
        global label_electricity_calculated

        frame = Frame(self)
        frame.pack(fill=BOTH, expand=True)

        frame_1 = Frame(frame, relief=RAISED, borderwidth=10)
        frame_1['bg'] = "#434343"
        frame_1.pack(side='left', fill=BOTH, expand=True)

        frame_2 = Frame(frame, relief=RAISED, borderwidth=10)
        frame_2['bg'] = "#434343"
        frame_2.pack(side='right', fill=BOTH, expand=True)

        label_1 = Label(frame_1, text='Вкажіть ваші нарахування:', bg=frame_1['bg'], fg='white', font='Arial 17')
        label_1.place(x='55', y='30')

        label_gas_1 = Label(frame_1, width=20, height=2, text='Лічильник газу \n(м\u00b3)',
                            bg=frame_1['bg'], fg='white', font='Arial 17')
        label_gas_1.place(x='70', y='100')
        entry_gas_main = Entry(frame_1, width=13, font='Arial 17')
        entry_gas_main.place(x='115', y='165')

        label_water_1 = Label(frame_1, width=20, height=2, text='Лічильник води \n(м\u00b3)',
                              bg=frame_1['bg'], fg='white', font='Arial 17')
        label_water_1.place(x='70', y='230')
        entry_water_main = Entry(frame_1, width=13, font='Arial 17')
        entry_water_main.place(x='115', y='295')

        label_electricity_1 = Label(frame_1, width=20, height=2, text='Лічильник електроенергії \n(кВт•год)',
                                    bg=frame_1['bg'], fg='white', font='Arial 17')
        label_electricity_1.place(x='70', y='360')
        entry_electricity_main = Entry(frame_1, width=13, font='Arial 17')
        entry_electricity_main.place(x='115', y='425')

        label_2 = Label(frame_2, text='Суми до сплати:', bg=frame_2['bg'], fg='white', font='Arial 17')
        label_2.place(x='105', y='30')

        label_gas_2 = Label(frame_2, width=20, height=2, text='Лічильник газу \n(грн)',
                            bg=frame_2['bg'], fg='white', font='Arial 17')
        label_gas_2.place(x='70', y='100')
        label_gas_calculated = Label(frame_2, width=13, bg=frame_2['bg'], fg='white', font='Arial 17')
        label_gas_calculated.place(x='115', y='165')

        label_water_2 = Label(frame_2, width=20, height=2, text='Лічильник води \n(грн)',
                              bg=frame_2['bg'], fg='white', font='Arial 17')
        label_water_2.place(x='70', y='230')
        label_water_calculated = Label(frame_2, width=13, bg=frame_2['bg'], fg='white', font='Arial 17')
        label_water_calculated.place(x='115', y='295')

        label_electricity_2 = Label(frame_2, width=20, height=2, text='Лічильник електроенергії \n(грн)',
                                    bg=frame_2['bg'], fg='white', font='Arial 17')
        label_electricity_2.place(x='70', y='360')
        label_electricity_calculated = Label(frame_2, width=13, bg=frame_2['bg'], fg='white', font='Arial 17')
        label_electricity_calculated.place(x='115', y='425')

        button_settings = Hover_Button(self, width=16, text="Налаштування", bg='gray22', fg='white', font='Arial 17',
                                       activebackground='#A5A5A5')
        button_settings.configure(command=settings, state=NORMAL)
        button_settings.pack(side='left', padx=15, pady=10)

        button_exit = Hover_Button(self, width=16, text="Завершити роботу", bg='gray22', fg='white', font='Arial 17',
                                   activebackground='#A5A5A5')
        button_exit.configure(command=program_exit)
        button_exit.pack(side='right', padx=15, pady=10)

        button_calculate = Hover_Button(self, width=16, text="Розрахувати", bg='gray22', fg='white', font='Arial 17',
                                        activebackground='#A5A5A5')
        button_calculate.configure(command=calculate)
        button_calculate.pack(side='top', padx=15, pady=10)


class Settings_Menu(Frame):
    """ The Class that defines the appearance of the Settings menu and properties of the Settings menu buttons  """

    def __init__(self):
        super().__init__()
        self.initUI()

    @staticmethod
    def initUI():
        set_win.attributes('-topmost', True)
        set_win.configure(background="#292929")
        button_settings.configure(state=DISABLED)

        global entry_gas
        global entry_water
        global entry_electricity

        frame = Frame(set_win, relief=RAISED, borderwidth=5)
        frame['bg'] = "#434343"
        frame.columnconfigure([0, 1], minsize=250)
        frame.rowconfigure([0, 1, 2], minsize=100)
        frame.pack(fill=BOTH, expand=True)

        label_gas = Label(frame, width=16, height=2, text='Ціна газу \n1 м\u00b3/грн',
                          bg=frame['bg'], fg='white', font='Arial 17')
        label_gas.grid(row=0, column=0)
        entry_gas = Entry(frame, width=13, font='Arial 17')
        entry_gas.grid(row=0, column=1, sticky='w')

        label_water = Label(frame, width=16, height=2, text='Ціна води \n1 м\u00b3/грн',
                            bg=frame['bg'], fg='white', font='Arial 17')
        label_water.grid(row=1, column=0)
        entry_water = Entry(frame, width=13, font='Arial 17')
        entry_water.grid(row=1, column=1, sticky='w')

        label_electricity = Label(frame, width=16, height=2, text='Ціна електроенергії \n1 кВт•год/грн',
                                  bg=frame['bg'], fg='white', font='Arial 17')
        label_electricity.grid(row=2, column=0)
        entry_electricity = Entry(frame, width=13, font='Arial 17')
        entry_electricity.grid(row=2, column=1, sticky='w')

        button_save = Hover_Button(set_win, text="Закінчити редагування", bg='gray22', fg='white',
                                   font='Arial 17', activebackground='#A5A5A5')
        button_save.configure(command=settings_save)
        button_save.pack(side='top', padx=15, pady=10)


def main():
    """ The function that launches the graphical interface of the Main menu """
    window = Tk()
    window.geometry('850x600+530+170')
    app_1 = Main_Menu()
    window.protocol('WM_DELETE_WINDOW', program_exit)
    window.mainloop()


def calculate():
    """ The Function that is responsible for calculating utility bills """

    rate_dict = {'gas': 0, 'water': 0, 'electricity': 0}
    gas_calc = 0
    water_calc = 0
    electricity_calc = 0
    try:
        with open('rate_dictionary.txt') as file:
            for i in file.readlines():
                key, val = i.strip().split(':')
                rate_dict[key] = val
    except FileNotFoundError:
        messagebox.showerror('Помилка', 'Увага! Файл з тарифами не знайдено. Перейдіть до налаштувань та вкажіть діючі '
                                        'тарифи на комунальній послуги.')
    except IOError:
        messagebox.showerror('Помилка', 'Увага! Файл з тарифами не знайдено. Перейдіть до налаштувань та вкажіть діючі '
                                        'тарифи на комунальній послуги.')
    except ValueError:
        messagebox.showerror('Помилка', 'Увага! Файл з тарифами було пошкоджено. Перейдіть до налаштувань та вкажіть '
                                        'діючі тарифи на комунальній послуги.')
    try:
        gas_calc = (float(rate_dict['gas']) * float(entry_gas_main.get()))
        water_calc = (float(rate_dict['water']) * float(entry_water_main.get()))
        electricity_calc = (float(rate_dict['electricity']) * float(entry_electricity_main.get()))
    except ValueError:
        messagebox.showerror('Помилка', 'Вказані дані не відповідають числовому формату. '
                                        '\nБудь ласка, перевірте вказану інформацію')
    try:
        label_gas_calculated.configure(text='{:8.3f}'.format(gas_calc))
        label_water_calculated.configure(text='{:8.3f}'.format(water_calc))
        label_electricity_calculated.configure(text='{:8.3f}'.format(electricity_calc))
    except ValueError:
        messagebox.showerror('Помилка', 'Вказані дані не відповідають числовому формату. '
                                        '\nБудь ласка, перевірте вказану інформацію')
    except TypeError:
        messagebox.showerror('Помилка', 'Вказані дані не відповідають числовому формату. '
                                        '\nБудь ласка, перевірте вказану інформацію')


def settings():
    """ The function that launches the graphical interface of the Settings menu """

    global set_win

    set_win = Tk()
    set_win.title('Utilities calculator settings')
    set_win.geometry("455x400+60+370")
    app = Settings_Menu()
    set_win.protocol('WM_DELETE_WINDOW', settings_save)
    set_win.mainloop()


def settings_save():
    """ The Function that is responsible for exiting the settings menu """

    answer = messagebox.askyesno(title='Закінчити редагування',
                                 message='Зберегти зміни?')
    if answer:

        rate_changing()
        set_win.destroy()
        button_settings.configure(state=NORMAL)
        """except ValueError:
            messagebox.showerror('Помилка', 'Вказані дані не відповідають числовому формату. '
                                        '\nБудь ласка, перевірте вказану інформацію')"""
    elif not answer:
        set_win.destroy()
        button_settings.configure(state=NORMAL)


def rate_changing():
    """ The Function that is responsible for creating/editing utility tariffs """

    rate_dict = dict(gas=0, water=0, electricity=0)
    try:
        if entry_gas.get() == '':
            with open('rate_dictionary.txt', 'r') as file:
                for i in file.readlines():
                    key, val = i.strip().split(':')
                    if key == 'gas':
                        rate_dict[key] = val
        else:
            rate_dict['gas'] = float(entry_gas.get())

        if entry_water.get() == '':
            with open('rate_dictionary.txt', 'r') as file:
                for i in file.readlines():
                    key, val = i.strip().split(':')
                    if key == 'water':
                        rate_dict[key] = val
        else:
            rate_dict['water'] = float(entry_water.get())

        if entry_electricity.get() == '':
            with open('rate_dictionary.txt', 'r') as file:
                for i in file.readlines():
                    key, val = i.strip().split(':')
                    if key == 'electricity':
                        rate_dict[key] = val
        else:
            rate_dict['electricity'] = float(entry_electricity.get())
    except ValueError:
        messagebox.showerror('Помилка', 'Увага! Файл з тарифами було пошкоджено. Будь ласка, вкажіть '
                                        'діючі тарифи на комунальній послуги.')
    try:
        with open('rate_dictionary.txt', 'w') as file:
            for key, val in rate_dict.items():
                file.write('{}:{}\n'.format(key, val))
    except FileNotFoundError:
        messagebox.showwarning('УВАГА!', 'Попередній файл не знайдено. Створено новий файл з тарифами.')
        with open('rate_dictionary.txt', 'w') as file:
            for key, val in rate_dict.items():
                file.write('{}:{}\n'.format(key, val))
    except IOError:
        messagebox.showwarning('УВАГА!', 'Попередній файл не знайдено. Створено новий файл з тарифами.')
        with open('rate_dictionary.txt', 'w') as file:
            for key, val in rate_dict.items():
                file.write('{}:{}\n'.format(key, val))
    except ValueError:
        messagebox.showerror('Помилка', 'Вказані дані не відповідають числовому формату. '
                                        '\nБудь ласка, перевірте вказану інформацію')


def program_exit():
    """ The Function that is responsible for exiting the program """

    if messagebox.askyesno(title='Завершення роботи',
                           message='Ви впевнені що хочете завершити роботу з програмою?'):
        exit()


if __name__ == '__main__':
    main()
