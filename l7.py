import customtkinter
import sqlite3
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title('Ice Cream Parlor Cafe')
app.config(bg='#C0FBFF')
app.geometry('800x450')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')

conn = sqlite3.connect('ice_cream_parlor.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor TEXT NOT NULL,
    description TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS customer_suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_suggestion TEXT NOT NULL,
    customer_name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS allergens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    allergen TEXT NOT NULL
)
''')

conn.commit()

def add_seasonal_flavor():
    for widget in app.winfo_children():
        widget.destroy()

    frame3 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame3.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)

    flavor_label = customtkinter.CTkLabel(frame3, text="Flavor", font=font2, text_color='#000000')
    flavor_label.place(relx=0.1, rely=0.2)
    flavor_entry = customtkinter.CTkEntry(frame3, font=font2, text_color='#fff', fg_color='#001a2e',
                                          border_color='#004780', border_width=3, width=200, height=50)
    flavor_entry.place(relx=0.5, rely=0.2)

    description_label = customtkinter.CTkLabel(frame3, text="Description", font=font2, text_color='#000000')
    description_label.place(relx=0.1, rely=0.5)
    description_entry = customtkinter.CTkEntry(frame3, font=font2, text_color='#fff', fg_color='#001a2e',
                                               border_color='#004780', border_width=3, width=200, height=50)
    description_entry.place(relx=0.5, rely=0.5)

    def submit_flavor():
        flavor = flavor_entry.get()
        description = description_entry.get()
        if flavor and description:
            cursor.execute('INSERT INTO seasonal_flavors (flavor, description) VALUES (?, ?)', (flavor, description))
            conn.commit()
            messagebox.showinfo('Success', 'Seasonal flavor added successfully')
            main_menu()
        else:
            messagebox.showerror('Error', 'Enter all the data')

    submit_button = customtkinter.CTkButton(frame3, text="Submit", font=font2, command=submit_flavor)
    submit_button.place(relx=0.4, rely=0.8)


def add_ingredients():
    for widget in app.winfo_children():
        widget.destroy()

    frame3 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame3.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)

    ingredients_label = customtkinter.CTkLabel(frame3, text="Ingredients", font=font2, text_color='#000000')
    ingredients_label.place(relx=0.1, rely=0.2)
    ingredients_entry = customtkinter.CTkEntry(frame3, font=font2, text_color='#fff', fg_color='#001a2e',
                                               border_color='#004780', border_width=3, width=200, height=50)
    ingredients_entry.place(relx=0.5, rely=0.2)

    quantity_label = customtkinter.CTkLabel(frame3, text="Quantity", font=font2, text_color='#000000')
    quantity_label.place(relx=0.1, rely=0.5)
    quantity_entry = customtkinter.CTkEntry(frame3, font=font2, text_color='#fff', fg_color='#001a2e',
                                            border_color='#004780', border_width=3, width=200, height=50)
    quantity_entry.place(relx=0.5, rely=0.5)

    def submit_ingredient():
        ingredients = ingredients_entry.get()
        quantity = quantity_entry.get()
        if ingredients and quantity:
            cursor.execute('INSERT INTO ingredients (ingredient, quantity) VALUES (?, ?)', (ingredients, quantity))
            conn.commit()
            messagebox.showinfo('Success', 'Ingredients added successfully')
            main_menu()
        else:
            messagebox.showerror('Error', 'Enter all the data')

    submit_button = customtkinter.CTkButton(frame3, text="Submit", font=font2, command=submit_ingredient)
    submit_button.place(relx=0.4, rely=0.8)


def add_flavor_suggestion():
    for widget in app.winfo_children():
        widget.destroy()

    frame3 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame3.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)

    add_flavor_suggestion_label = customtkinter.CTkLabel(frame3, text="Add Flavor Suggestion", font=font2,
                                                         text_color='#000000')
    add_flavor_suggestion_label.place(relx=0.1, rely=0.2)
    flavor_suggestion_entry = customtkinter.CTkEntry(frame3, font=font2, text_color='#fff', fg_color='#001a2e',
                                                     border_color='#004780', border_width=3, width=200, height=50)
    flavor_suggestion_entry.place(relx=0.5, rely=0.2)

    customer_name_label = customtkinter.CTkLabel(frame3, text="Customer Name", font=font2, text_color='#000000')
    customer_name_label.place(relx=0.1, rely=0.5)
    customer_name_entry = customtkinter.CTkEntry(frame3, font=font2, text_color='#fff', fg_color='#001a2e',
                                                 border_color='#004780', border_width=3, width=200, height=50)
    customer_name_entry.place(relx=0.5, rely=0.5)

    def submit_flavor_suggestion():
        flavor_suggestion = flavor_suggestion_entry.get()
        customer_name = customer_name_entry.get()
        if flavor_suggestion and customer_name:
            cursor.execute('INSERT INTO customer_suggestions (flavor_suggestion, customer_name) VALUES (?, ?)',
                           (flavor_suggestion, customer_name))
            conn.commit()
            messagebox.showinfo('Success', 'Flavor Suggestion added successfully')
            main_menu()
        else:
            messagebox.showerror('Error', 'Enter all the data')

    submit_button = customtkinter.CTkButton(frame3, text="Submit", font=font2, command=submit_flavor_suggestion)
    submit_button.place(relx=0.4, rely=0.8)


def add_allergen_suggestion():
    for widget in app.winfo_children():
        widget.destroy()

    frame3 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame3.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)

    allergen_suggestion_label = customtkinter.CTkLabel(frame3, text="Add Allergen Suggestion", font=font2,
                                                       text_color='#000000')
    allergen_suggestion_label.place(relx=0.1, rely=0.2)
    allergen_suggestion_entry = customtkinter.CTkEntry(frame3, font=font2, text_color='#fff', fg_color='#001a2e',
                                                       border_color='#004780', border_width=3, width=200, height=50)
    allergen_suggestion_entry.place(relx=0.5, rely=0.2)

    def submit_allergen_suggestion():
        allergen_suggestion = allergen_suggestion_entry.get()
        if allergen_suggestion:
            cursor.execute('INSERT INTO allergens (allergen) VALUES (?)', (allergen_suggestion,))
            conn.commit()
            messagebox.showinfo('Success', 'Allergen Suggestion added successfully')
            main_menu()
        else:
            messagebox.showerror('Error', 'Enter the allergen')

    submit_button = customtkinter.CTkButton(frame3, text="Submit", font=font2, command=submit_allergen_suggestion)
    submit_button.place(relx=0.4, rely=0.8)

def add_offering_items():
    for widget in app.winfo_children():
        widget.destroy()

    frame2 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)  

    title_label = customtkinter.CTkLabel(frame2, font=font1, text='Welcome to Ice Cream Parlor Cafe', text_color='#fff',
                                         bg_color='#001220')
    title_label.place(x=300,y=40)

    add_seasonal_flavor_items = customtkinter.CTkButton(frame2, text='Add Seasonal Flavors', fg_color='black', width=20,
                                                        height=2, font=font2, command=add_seasonal_flavor)
    add_seasonal_flavor_items.place(x=300, y=100)

    add_ingredients_items = customtkinter.CTkButton(frame2, text='Add Ingredients', fg_color='black', width=20,
                                                    height=2, font=font2, command=add_ingredients)
    add_ingredients_items.place(x=300, y=160)

    add_flavour_suggestion_items = customtkinter.CTkButton(frame2, text='Add Flavor Suggestions', fg_color='black',
                                                            width=20,
                                                            height=2, font=font2, command=add_flavor_suggestion)
    add_flavour_suggestion_items.place(x=300, y=220)

    add_allergen_suggestion_items = customtkinter.CTkButton(frame2, text='Add Allergen Suggestions', fg_color='black',
                                                           width=20,
                                                           height=2, font=font2, command=add_allergen_suggestion)
    add_allergen_suggestion_items.place(x=300, y=280)

def search_offering_items():
    for widget in app.winfo_children():
        widget.destroy()

    frame2 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)

    title_label = customtkinter.CTkLabel(frame2, font=font1, text='Welcome to Ice Cream Parlor Cafe', text_color='#fff',
                                         bg_color='#001220')
    title_label.place(x=300, y=40)

    search_sflavor_items = customtkinter.CTkButton(app, text='Search seasonal flavor items', bg_color='#C0FBFF', fg_color='black', width=20,
                                           height=2,
                                           font=font2, command=search_flavor_items)
    search_sflavor_items.place(x=600, y=160)

    search_allergen_items = customtkinter.CTkButton(app, text='Search allergen items', bg_color='#C0FBFF',
                                                   fg_color='black', width=20,
                                                   height=2,
                                                   font=font2, command=search_allergens_items)
    search_allergen_items.place(x=600, y=200)
def search_flavor_items():
    for widget in app.winfo_children():
        widget.destroy()

    frame2 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)
    search_flavors_label = customtkinter.CTkLabel(frame2, text="Search seasonal flavor", font=font2,
                                                  text_color='#000000')
    search_flavors_label.place(relx=0.1, rely=0.2)

    search_flavors_entry = customtkinter.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e',
                                                  border_color='#004780', border_width=3, width=200, height=50)
    search_flavors_entry.place(relx=0.5, rely=0.2)

    def submit_search_flavors():
        flavor_to_search = search_flavors_entry.get()
        if flavor_to_search:
            cursor.execute('SELECT * FROM seasonal_flavors WHERE flavor LIKE ?', ('%' + flavor_to_search + '%',))
            results = cursor.fetchall()
            if results:
                result_frame = customtkinter.CTkFrame(frame2, bg_color='#C0FBFF', fg_color='#C0FBFF')
                result_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

                header_label = customtkinter.CTkLabel(result_frame, text="Search Results", font=font2, text_color='#000000')
                header_label.pack()

                for idx, result in enumerate(results):
                    flavor_label = customtkinter.CTkLabel(result_frame, text=f"{idx + 1}. {result[1]} - {result[2]}", font=font2, text_color='#000000')
                    flavor_label.pack()

            else:
                messagebox.showinfo('Information', 'No matching flavors found')

        else:
            messagebox.showerror('Error', 'Enter the seasonal flavor')

    submit_button = customtkinter.CTkButton(frame2, text="Submit", font=font2, command=submit_search_flavors)
    submit_button.place(relx=0.4, rely=0.4)

def search_allergens_items():
    for widget in app.winfo_children():
        widget.destroy()

    frame2 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)
    search_allergens_label = customtkinter.CTkLabel(frame2, text="Search allergen", font=font2,
                                                 text_color='#000000')
    search_allergens_label.place(relx=0.1, rely=0.2)

    search_allergens_entry = customtkinter.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e',
                                                  border_color='#004780', border_width=3, width=200, height=50)
    search_allergens_entry.place(relx=0.5, rely=0.2)

    def submit_search_allergen():
        allergen_to_search = search_allergens_entry.get()
        if allergen_to_search:
            cursor.execute('SELECT * FROM allergens')
            result= cursor.fetchall()
            if results:
                result_frame = customtkinter.CTkFrame(frame2, bg_color='#C0FBFF', fg_color='#C0FBFF')
                result_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

                header_label = customtkinter.CTkLabel(result_frame, text="Search Results", font=font2,
                                                      text_color='#000000')
                header_label.pack()

                for idx, result in enumerate(results):
                    flavor_label = customtkinter.CTkLabel(result_frame, text=f"{idx + 1}. {result[1]}",
                                                          font=font2, text_color='#000000')
                    flavor_label.pack()

            else:
                messagebox.showinfo('Information', 'No matching Allergens found')

        else:
            messagebox.showerror('Error', 'Enter the allergen')

    submit_button = customtkinter.CTkButton(frame2, text="Submit", font=font2, command=submit_search_allergen)
    submit_button.place(relx=0.4, rely=0.4)

def main_menu():
    for widget in app.winfo_children():
        widget.destroy()

    frame1 = customtkinter.CTkFrame(app, bg_color='#C0FBFF', fg_color='#C0FBFF')
    frame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)

    title_label = customtkinter.CTkLabel(frame1, font=font1, text='Welcome to Ice Cream Parlor Cafe', text_color='#fff',
                                         bg_color='#001220')
    title_label.place(x=300, y=40)

    add_items = customtkinter.CTkButton(app, text='Add items', bg_color='#C0FBFF', fg_color='black', width=20, height=2,
                                        font=font2, command=add_offering_items)
    add_items.place(x=600,y=160)

    search_items = customtkinter.CTkButton(app, text='Search items', bg_color='#C0FBFF', fg_color='black', width=20, height=2,
                                        font=font2, command=search_offering_items)
    search_items.place(x=600, y=200)

if __name__ == "__main__":
    main_menu()
    app.mainloop()

conn.close()
