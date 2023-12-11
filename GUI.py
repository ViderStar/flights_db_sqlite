import tkinter as tk
from tkinter import ttk


class GUI:
    def __init__(self, database):
        self.db = database

        root = tk.Tk()
        root.geometry("1000x720")
        root.title("Flights HandBook")
        # root.iconbitmap(r"img.ico")
        root.tk.call("source", "Azure-ttk-theme/azure.tcl")
        root.tk.call("set_theme", "light")

        name_label = ttk.Label(text="Artsem Lebiadzevich\n3 course, 12 group")
        name_label.pack(anchor=tk.N, pady=(20, 20))

        year_label = ttk.Label(text="2023")
        year_label.pack(anchor=tk.N)
        # root.resizable(False, False)

        # Создание выпадающего списка для выбора справочника
        self.directory_var = tk.StringVar()
        directory_label = ttk.Label(root, text="Выберите справочник:")
        directory_label.pack(anchor=tk.W, padx=10, pady=(30, 10))
        directory_combobox = ttk.Combobox(root, textvariable=self.directory_var, state="readonly")
        directory_combobox["values"] = ["airports", "airlines", "flights"]
        directory_combobox.pack(anchor=tk.W, padx=10)

        # Создание кнопок для действий с записями
        add_button = ttk.Button(root, text="Добавить", command=self.add_entry)
        add_button.pack(anchor=tk.W, padx=10, pady=(20, 5))

        edit_button = ttk.Button(root, text="Редактировать", command=self.edit_entry)
        edit_button.pack(anchor=tk.W, padx=10, pady=5)

        delete_button = ttk.Button(root, text="Удалить", command=self.delete_entry)
        delete_button.pack(anchor=tk.W, padx=10, pady=5)

        view_button = ttk.Button(root, text="Просмотреть", command=self.view_entry)
        view_button.pack(anchor=tk.W, padx=10, pady=5)

        # Создание таблицы для отображения данных
        self.table = ttk.Treeview(root, columns=("id", "code", "name", "city", "country"))
        self.table.heading("#0", text="ID")
        self.table.column("#0", width=50)
        self.table.heading("id", text="ID")
        self.table.column("id", width=50)
        self.table.heading("code", text="Код")
        self.table.column("code", width=100)
        self.table.heading("name", text="Название")
        self.table.column("name", width=200)
        self.table.heading("city", text="Город")
        self.table.column("city", width=200)
        self.table.heading("country", text="Страна")
        self.table.column("country", width=200)
        self.table.pack(anchor=tk.W, padx=10, pady=(30, 10))

        # Обновление таблицы при выборе справочника
        self.directory_var.trace("w", self.update_table)

        root.mainloop()

    def update_table(self, *args):
        """
        Обновляет таблицу при выборе справочника.
        """
        directory = self.directory_var.get()

        if directory == "airports":
            data = self.db.get_all_airports()
        elif directory == "airlines":
            data = self.db.get_all_airlines()
        elif directory == "flights":
            data = self.db.get_all_flights()
        else:
            data = []

        self.table.delete(*self.table.get_children())

        for row in data:
            self.table.insert("", "end", values=row)

    def add_entry(self):
        """
        Открывает окно для добавления новой записи.
        """
        directory = self.directory_var.get()

        if directory == "airports":
            AddAirportWindow(self.db, self.update_table)
        elif directory == "airlines":
            AddAirlineWindow(self.db, self.update_table)
        elif directory == "flights":
            AddFlightWindow(self.db, self.update_table)

    def edit_entry(self):
        """
        Открывает окно для редактирования выбранной записи.
        """
        selected_item = self.table.selection()

        if selected_item:
            item_id = self.table.item(selected_item)["values"][0]
            directory = self.directory_var.get()

            if directory == "airports":
                EditAirportWindow(self.db, self.update_table, item_id)
            elif directory == "airlines":
                EditAirlineWindow(self.db, self.update_table, item_id)
            elif directory == "flights":
                EditFlightWindow(self.db, self.update_table, item_id)

    def delete_entry(self):
        """
        Удаляет выбранную запись из базы данных.
        """
        selected_item = self.table.selection()

        if selected_item:
            item_id = self.table.item(selected_item)["values"][0]
            directory = self.directory_var.get()

            if directory == "airports":
                self.db.delete_airport(item_id)
            elif directory == "airlines":
                self.db.delete_airline(item_id)
            elif directory == "flights":
                self.db.delete_flight(item_id)

            self.update_table()

    def view_entry(self):
        """
        Открывает окно для просмотра выбранной записи.
        """
        selected_item = self.table.selection()

        if selected_item:
            item_id = self.table.item(selected_item)["values"][0]
            directory = self.directory_var.get()

            if directory == "airports":
                ViewAirportWindow(self.db, item_id)
            elif directory == "airlines":
                ViewAirlineWindow(self.db, item_id)
            elif directory == "flights":
                ViewFlightWindow(self.db, item_id)


class AddAirportWindow:
    def __init__(self, db, update_table):
        self.db = db
        self.update_table = update_table

        self.window = tk.Toplevel()
        self.window.title("Добавить аэропорт")

        code_label = ttk.Label(self.window, text="Код:")
        code_label.pack(anchor=tk.W, padx=10, pady=(20, 5))
        self.code_entry = ttk.Entry(self.window)
        self.code_entry.pack(anchor=tk.W, padx=10)

        name_label = ttk.Label(self.window, text="Название:")
        name_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.pack(anchor=tk.W, padx=10)

        city_label = ttk.Label(self.window, text="Город:")
        city_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.city_entry = ttk.Entry(self.window)
        self.city_entry.pack(anchor=tk.W, padx=10)

        country_label = ttk.Label(self.window, text="Страна:")
        country_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.country_entry = ttk.Entry(self.window)
        self.country_entry.pack(anchor=tk.W, padx=10)

        save_button = ttk.Button(self.window, text="Сохранить", command=self.save_entry)
        save_button.pack(anchor=tk.W, padx=10, pady=(20, 10))

    def save_entry(self):
        code = self.code_entry.get()
        name = self.name_entry.get()
        city = self.city_entry.get()
        country = self.country_entry.get()

        self.db.add_airport(code, name, city, country)
        self.update_table()
        self.window.destroy()


class AddAirlineWindow:
    def __init__(self, db, update_table):
        self.db = db
        self.update_table = update_table

        self.window = tk.Toplevel()
        self.window.title("Добавить авиакомпанию")

        code_label = ttk.Label(self.window, text="Код:")
        code_label.pack(anchor=tk.W, padx=10, pady=(20, 5))
        self.code_entry = ttk.Entry(self.window)
        self.code_entry.pack(anchor=tk.W, padx=10)

        name_label = ttk.Label(self.window, text="Название:")
        name_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.pack(anchor=tk.W, padx=10)

        country_label = ttk.Label(self.window, text="Страна:")
        country_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.country_entry = ttk.Entry(self.window)
        self.country_entry.pack(anchor=tk.W, padx=10)

        save_button = ttk.Button(self.window, text="Сохранить", command=self.save_entry)
        save_button.pack(anchor=tk.W, padx=10, pady=(20, 10))

    def save_entry(self):
        code = self.code_entry.get()
        name = self.name_entry.get()
        country = self.country_entry.get()

        self.db.add_airline(code, name, country)
        self.update_table()
        self.window.destroy()


class AddFlightWindow:
    def __init__(self, db, update_table):
        self.db = db
        self.update_table = update_table

        self.window = tk.Toplevel()
        self.window.title("Добавить рейс")

        airline_label = ttk.Label(self.window, text="Авиакомпания:")
        airline_label.pack(anchor=tk.W, padx=10, pady=(20, 5))
        self.airline_entry = ttk.Entry(self.window)
        self.airline_entry.pack(anchor=tk.W, padx=10)

        origin_label = ttk.Label(self.window, text="Откуда:")
        origin_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.origin_entry = ttk.Entry(self.window)
        self.origin_entry.pack(anchor=tk.W, padx=10)

        destination_label = ttk.Label(self.window, text="Куда:")
        destination_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.destination_entry = ttk.Entry(self.window)
        self.destination_entry.pack(anchor=tk.W, padx=10)

        save_button = ttk.Button(self.window, text="Сохранить", command=self.save_entry)
        save_button.pack(anchor=tk.W, padx=10, pady=(20, 10))

    def save_entry(self):
        airline = self.airline_entry.get()
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()

        self.db.add_flight(airline, origin, destination)
        self.update_table()
        self.window.destroy()


class EditAirportWindow:
    def __init__(self, db, airport_id, update_table):
        self.db = db
        self.airport_id = airport_id
        self.update_table = update_table

        self.window = tk.Toplevel()
        self.window.title("Редактировать аэропорт")

        airport = self.db.get_airport(airport_id)

        code_label = ttk.Label(self.window, text="Код:")
        code_label.pack(anchor=tk.W, padx=10, pady=(20, 5))
        self.code_entry = ttk.Entry(self.window)
        self.code_entry.insert(0, airport['code'])
        self.code_entry.pack(anchor=tk.W, padx=10)

        name_label = ttk.Label(self.window, text="Название:")
        name_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.insert(0, airport['name'])
        self.name_entry.pack(anchor=tk.W, padx=10)

        city_label = ttk.Label(self.window, text="Город:")
        city_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.city_entry = ttk.Entry(self.window)
        self.city_entry.insert(0, airport['city'])
        self.city_entry.pack(anchor=tk.W, padx=10)

        country_label = ttk.Label(self.window, text="Страна:")
        country_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.country_entry = ttk.Entry(self.window)
        self.country_entry.insert(0, airport['country'])
        self.country_entry.pack(anchor=tk.W, padx=10)

        save_button = ttk.Button(self.window, text="Сохранить", command=self.save_entry)
        save_button.pack(anchor=tk.W, padx=10, pady=(20, 10))

    def save_entry(self):
        code = self.code_entry.get()
        name = self.name_entry.get()
        city = self.city_entry.get()
        country = self.country_entry.get()

        self.db.update_airport(self.airport_id, code, name, city, country)
        self.update_table()
        self.window.destroy()


class EditAirlineWindow:
    def __init__(self, db, airline_id, update_table):
        self.db = db
        self.airline_id = airline_id
        self.update_table = update_table

        self.window = tk.Toplevel()
        self.window.title("Редактировать авиакомпанию")

        airline = self.db.get_airline(airline_id)

        code_label = ttk.Label(self.window, text="Код:")
        code_label.pack(anchor=tk.W, padx=10, pady=(20, 5))
        self.code_entry = ttk.Entry(self.window)
        self.code_entry.insert(0, airline['code'])
        self.code_entry.pack(anchor=tk.W, padx=10)

        name_label = ttk.Label(self.window, text="Название:")
        name_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.insert(0, airline['name'])
        self.name_entry.pack(anchor=tk.W, padx=10)

        country_label = ttk.Label(self.window, text="Страна:")
        country_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.country_entry = ttk.Entry(self.window)
        self.country_entry.insert(0, airline['country'])
        self.country_entry.pack(anchor=tk.W, padx=10)

        save_button = ttk.Button(self.window, text="Сохранить", command=self.save_entry)
        save_button.pack(anchor=tk.W, padx=10, pady=(20, 10))

    def save_entry(self):
        code = self.code_entry.get()
        name = self.name_entry.get()
        country = self.country_entry.get()

        self.db.update_airline(self.airline_id, code, name, country)
        self.update_table()
        self.window.destroy()


class EditFlightWindow:
    def __init__(self, db, flight_id, update_table):
        self.db = db
        self.flight_id = flight_id
        self.update_table = update_table

        self.window = tk.Toplevel()
        self.window.title("Редактировать рейс")

        flight = self.db.get_flight(flight_id)

        airline_label = ttk.Label(self.window, text="Авиакомпания:")
        airline_label.pack(anchor=tk.W, padx=10, pady=(20, 5))
        self.airline_entry = ttk.Entry(self.window)
        self.airline_entry.insert(0, flight['airline'])
        self.airline_entry.pack(anchor=tk.W, padx=10, pady=(20, 5))

        origin_label = ttk.Label(self.window, text="Откуда:")
        origin_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.origin_entry = ttk.Entry(self.window)
        self.origin_entry.insert(0, flight['origin'])
        self.origin_entry.pack(anchor=tk.W, padx=10)

        destination_label = ttk.Label(self.window, text="Куда:")
        destination_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.destination_entry = ttk.Entry(self.window)
        self.destination_entry.insert(0, flight['destination'])
        self.destination_entry.pack(anchor=tk.W, padx=10)

        save_button = ttk.Button(self.window, text="Сохранить", command=self.save_entry)
        save_button.pack(anchor=tk.W, padx=10, pady=(20, 10))

    def save_entry(self):
        airline = self.airline_entry.get()
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()

        self.db.update_flight(self.flight_id, airline, origin, destination)
        self.update_table()
        self.window.destroy()


import tkinter as tk
from tkinter import ttk


class ViewAirportWindow:
    def __init__(self, airport):
        self.window = tk.Toplevel()
        self.window.title("Просмотр аэропорта")

        code_label = ttk.Label(self.window, text="Код:")
        code_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.code_entry = ttk.Entry(self.window)
        self.code_entry.insert(0, airport['code'])
        self.code_entry.configure(state='readonly')
        self.code_entry.pack(anchor=tk.W, padx=10)

        name_label = ttk.Label(self.window, text="Название:")
        name_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.insert(0, airport['name'])
        self.name_entry.configure(state='readonly')
        self.name_entry.pack(anchor=tk.W, padx=10)

        city_label = ttk.Label(self.window, text="Город:")
        city_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.city_entry = ttk.Entry(self.window)
        self.city_entry.insert(0, airport['city'])
        self.city_entry.configure(state='readonly')
        self.city_entry.pack(anchor=tk.W, padx=10)

        country_label = ttk.Label(self.window, text="Страна:")
        country_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.country_entry = ttk.Entry(self.window)
        self.country_entry.insert(0, airport['country'])
        self.country_entry.configure(state='readonly')
        self.country_entry.pack(anchor=tk.W, padx=10)


class ViewAirlineWindow:
    def __init__(self, airline):
        self.window = tk.Toplevel()
        self.window.title("Просмотр авиалинии")

        code_label = ttk.Label(self.window, text="Код:")
        code_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.code_entry = ttk.Entry(self.window)
        self.code_entry.insert(0, airline['code'])
        self.code_entry.configure(state='readonly')
        self.code_entry.pack(anchor=tk.W, padx=10)

        name_label = ttk.Label(self.window, text="Название:")
        name_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.insert(0, airline['name'])
        self.name_entry.configure(state='readonly')
        self.name_entry.pack(anchor=tk.W, padx=10)

        country_label = ttk.Label(self.window, text="Страна:")
        country_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.country_entry = ttk.Entry(self.window)
        self.country_entry.insert(0, airline['country'])
        self.country_entry.configure(state='readonly')
        self.country_entry.pack(anchor=tk.W, padx=10)


class ViewFlightWindow:
    def __init__(self, flight):
        self.window = tk.Toplevel()
        self.window.title("Просмотр рейса")

        airline_label = ttk.Label(self.window, text="Авиалиния:")
        airline_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.airline_entry = ttk.Entry(self.window)
        self.airline_entry.insert(0, flight['airline'])
        self.airline_entry.configure(state='readonly')
        self.airline_entry.pack(anchor=tk.W, padx=10)

        origin_label = ttk.Label(self.window, text="Откуда:")
        origin_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.origin_entry = ttk.Entry(self.window)
        self.origin_entry.insert(0, flight['origin'])
        self.origin_entry.configure(state='readonly')
        self.origin_entry.pack(anchor=tk.W, padx=10)

        destination_label = ttk.Label(self.window, text="Куда:")
        destination_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        self.destination_entry = ttk.Entry(self.window)
        self.destination_entry.insert(0, flight['destination'])
        self.destination_entry.configure(state='readonly')
        self.destination_entry.pack(anchor=tk.W, padx=10)
