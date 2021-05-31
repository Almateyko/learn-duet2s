from tkinter import messagebox

rate_dict = dict(gas=0.0, water=0.0, electricity=0.0)
stable_rate_dict = {}


def dict_remembering(filename, t_dict):
    try:
        with open(filename, 'r') as file:
            for i in file.readlines():
                key, val = i.strip().split(':')
                t_dict[key] = float(val)
    except FileNotFoundError:
        messagebox.showerror('Помилка', 'Файл з тарифами не знайдено. Перейдіть до налаштувань та вкажіть діючі '
                                        'тарифи на комунальній послуги.')
        return 'Not Found'
    except IOError:
        messagebox.showerror('Помилка', 'Файл з тарифами не знайдено. Перейдіть до налаштувань та вкажіть діючі '
                                        'тарифи на комунальній послуги.')
        return 'Not Found'
    except ValueError:
        messagebox.showerror('Помилка', 'Файл з тарифами було пошкоджено. Перейдіть до налаштувань та вкажіть '
                                        'діючі тарифи на комунальній послуги.')
        return 'ValueError'
    except TypeError:
        messagebox.showerror('Помилка', 'Файл з тарифами було пошкоджено. Перейдіть до налаштувань та вкажіть '
                                        'діючі тарифи на комунальній послуги.')
        return 'TypeError'


def dict_write_chek(resource, val):
    try:
        if val == '':
            dict_search_n_set(resource)
            return 'Verification was unsuccessful'
        elif not 0 <= float(val) <= 999:
            dict_search_n_set(resource)
            raise ValueError
        else:
            rate_dict[resource] = float(val)
            return 'Verification was successful'
    except ValueError:
        messagebox.showwarning('Увага!', "Частина внесених даних не збережена через невідповідність формату: "
                                         "це має бути невід'ємне число не більше за 999.")
        return 'ValueError'
    except TypeError:
        messagebox.showwarning('Увага!', "Частина внесених даних не збережена через невідповідність формату: "
                                         "це має бути невід'ємне число не більше за 999.")
        return 'TypeError'


def dict_search_n_set(required_key):
    try:
        rate_dict[required_key] = stable_rate_dict[required_key]
    except KeyError:
        stable_rate_dict[required_key] = 0


def dict_write(key, val):
    stable_rate_dict[key] = val
    dict_memorization('rate_dictionary.txt', stable_rate_dict)


def dict_memorization(filename, t_dict):
    try:
        with open(filename, 'w') as file:
            for key, val in t_dict.items():
                file.write('{}:{}\n'.format(key, val))
    except FileNotFoundError:
        messagebox.showwarning('Увага!', 'Попередній файл не знайдено. Створено новий файл з тарифами.')
        with open(filename, 'w') as file:
            for key, val in rate_dict.items():
                file.write('{}:{}\n'.format(key, val))
        return 'Not Found'
    except IOError:
        messagebox.showwarning('Увага!', 'Попередній файл не знайдено. Створено новий файл з тарифами.')
        with open(filename, 'w') as file:
            for key, val in rate_dict.items():
                file.write('{}:{}\n'.format(key, val))
        return 'Not Found'
    except ValueError:
        messagebox.showwarning('Увага!', "Частина внесених даних не збережена через невідповідність формату: "
                                         "це має бути невід'ємне число не більше за 999.")
        return 'ValueError'
    except TypeError:
        messagebox.showwarning('Увага!', "Частина внесених даних не збережена через невідповідність формату: "
                                         "це має бути невід'ємне число не більше за 999.")
        return 'TypeError'
