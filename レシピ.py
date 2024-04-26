import tkinter as tk
from tkinter import messagebox

class Recipe:
    def init(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeManagerApp:
    def init(self, master):
        self.master = master
        self.master.title("Recipe Manager")

        self.recipes = []

        self.recipelistbox = tk.Listbox(master, width=50, height=20)
        self.recipelistbox.pack(pady=10)

        self.addbutton = tk.Button(master, text="Add Recipe", command=self.addrecipe)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(master, text="Remove Recipe", command=self.remove_recipe)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.display_button = tk.Button(master, text="Display Recipes", command=self.display_recipes)
        self.display_button.pack(side=tk.LEFT, padx=10)

    def add_recipe(self):
        # Function to add recipe
        pass

    def remove_recipe(self):
        # Function to remove recipe
        pass

    def display_recipes(self):
        # Function to display recipes
        pass

def main():
    root = tk.Tk()
    app = RecipeManagerApp(root)
    root.mainloop()

if __name__ == "__main":
    main()