""" This is a program that calculates the amounts charged for the use of utility rates. """

# -- coding utf-8 --
__author__ = 'Alexander Mateyko'

from tkinter import *
from tkinter import messagebox

try:
    from src.dict_functions import *
except FileNotFoundError:
    messagebox.showwarning('Увага!', 'Втрачено файли, які потрібні для роботи програми. Потрібне перевстановлення.')
    exit()


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

        label_gas_2 = Label(frame_2, width=20, height=2, text='Газопостачання \n(грн)',
                            bg=frame_2['bg'], fg='white', font='Arial 17')
        label_gas_2.place(x='70', y='100')
        label_gas_calculated = Label(frame_2, width=13, bg=frame_2['bg'], fg='white', font='Arial 17')
        label_gas_calculated.place(x='115', y='165')

        label_water_2 = Label(frame_2, width=20, height=2, text='Водопостачання та\nводовідведення (грн)',
                              bg=frame_2['bg'], fg='white', font='Arial 17')
        label_water_2.place(x='70', y='230')
        label_water_calculated = Label(frame_2, width=13, bg=frame_2['bg'], fg='white', font='Arial 17')
        label_water_calculated.place(x='115', y='295')

        label_electricity_2 = Label(frame_2, width=20, height=2, text='Електропостачання \n(грн)',
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
    app = Main_Menu()
    window.protocol('WM_DELETE_WINDOW', program_exit)
    window.resizable(False, False)
    window.mainloop()
    dict_remembering('rate_dictionary.txt', stable_rate_dict)


def settings():
    """ The function that launches the graphical interface of the Settings menu """

    global set_win

    set_win = Tk()
    set_win.title('Utilities calculator settings')
    set_win.geometry("455x400+60+370")
    app = Settings_Menu()
    set_win.protocol('WM_DELETE_WINDOW', settings_save)
    set_win.resizable(False, False)
    set_win.mainloop()


def calculate():
    calculating(entry_gas_main.get(), entry_water_main.get(), entry_electricity_main.get())


def calculating(gas_in, water_in, electricity_in):
    """ The Function that is responsible for calculating utility bills """

    dict_remembering('rate_dictionary.txt', stable_rate_dict)

    calculate_chek('gas', gas_in)
    calculate_chek('water', water_in)
    calculate_chek('electricity', electricity_in)

    gas_calculated = (float(stable_rate_dict['gas']) * float(resources_for_count['gas']))
    water_calculated = (float(stable_rate_dict['water']) * float(resources_for_count['water']))
    electricity_calculated = (float(stable_rate_dict['electricity']) * float(resources_for_count['electricity']))

    label_gas_calculated.configure(text='{:8.3f}'.format(gas_calculated))
    label_water_calculated.configure(text='{:8.3f}'.format(water_calculated))
    label_electricity_calculated.configure(text='{:8.3f}'.format(electricity_calculated))


def calculate_chek(resource, enter_data):
    global resources_for_count
    resources_for_count = {'gas': 0.0, 'water': 0.0, 'electricity': 0.0}

    try:
        if enter_data == '':
            resources_for_count[resource] = 0
            return 'Verification was unsuccessful'
        elif not 0 <= float(enter_data) <= 999:
            resources_for_count[resource] = 0
            raise ValueError
        else:
            resources_for_count[resource] = float(enter_data)
            return 'Verification was successful'
    except ValueError:
        messagebox.showwarning('Увага!', "Деякі обчислення не виконані через невідповідність формату: "
                                         "це має бути невід'ємне число не більше за 999.")
        return 'ValueError'
    except TypeError:
        messagebox.showwarning('Увага!', "Деякі обчислення не виконані через невідповідність формату: "
                                         "це має бути невід'ємне число не більше за 999.")
        return 'TypeError'
    except NameError:
        messagebox.showwarning('Увага!', "Втрачено шляха до таблиці тарифів. Для подальшої роботи потрібне "
                                             "перевстанолвення програми.")
        return 'NameError'


def settings_save():
    """ The Function that is responsible for exiting the settings menu """

    answer = messagebox.askyesno(title='Закінчити редагування',
                                 message='Зберегти зміни?')
    if answer:
        tariffs_changing(entry_gas.get(), entry_water.get(), entry_electricity.get())
        set_win.destroy()
        button_settings.configure(state=NORMAL)

    elif not answer:
        set_win.destroy()
        button_settings.configure(state=NORMAL)


def tariffs_changing(gas, water, electricity):
    """ The Function that is responsible for creating/editing utility tariffs """

    dict_write_chek('gas', gas)
    dict_write('gas', gas)
    dict_write_chek('water', water)
    dict_write('water', water)
    dict_write_chek('electricity', electricity)
    dict_write('electricity', electricity)


def program_exit():
    """ The Function that is responsible for exiting the program """

    if messagebox.askyesno(title='Завершення роботи',
                           message='Ви впевнені що хочете завершити роботу з програмою?'):
        exit()


if __name__ == '__main__':
    main()
