import sqlite3
import streamlit as st

# Database setup
def create_tables():
    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER NOT NULL,
                    ingredient TEXT NOT NULL,
                    FOREIGN KEY (recipe_id) REFERENCES recipes (id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS steps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER NOT NULL,
                    step_order INTEGER NOT NULL,
                    description TEXT NOT NULL,
                    FOREIGN KEY (recipe_id) REFERENCES recipes (id))''')
    conn.commit()
    conn.close()

# Add a recipe to the database
def add_recipe(title, ingredients, steps):
    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()

    # Insert the recipe
    c.execute("INSERT INTO recipes (title) VALUES (?)", (title,))
    recipe_id = c.lastrowid

    # Insert ingredients
    for ingredient in ingredients:
        c.execute("INSERT INTO ingredients (recipe_id, ingredient) VALUES (?, ?)", (recipe_id, ingredient))

    # Insert steps
    for order, step in enumerate(steps, start=1):
        c.execute("INSERT INTO steps (recipe_id, step_order, description) VALUES (?, ?, ?)", (recipe_id, order, step))

    conn.commit()
    conn.close()

# Delete a recipe from the database
def delete_recipe(recipe_id):
    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()

    # Delete ingredients and steps associated with the recipe
    c.execute("DELETE FROM ingredients WHERE recipe_id = ?", (recipe_id,))
    c.execute("DELETE FROM steps WHERE recipe_id = ?", (recipe_id,))

    # Delete the recipe
    c.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))

    conn.commit()
    conn.close()

# Streamlit app
create_tables()
st.title("Recipe Manager")

# Input form
st.header("Add a New Recipe")
with st.form("recipe_form"):
    title = st.text_input("Recipe Title")
    ingredients = st.text_area("Ingredients (one per line)").split("\n")
    steps = st.text_area("Steps (one per line)").split("\n")
    submitted = st.form_submit_button("Add Recipe")

if submitted:
    if title and ingredients and steps:
        add_recipe(title, [i.strip() for i in ingredients if i.strip()], [s.strip() for s in steps if s.strip()])
        st.success("Recipe added successfully!")
    else:
        st.error("Please fill in all fields.")

# Display recipes
st.header("All Recipes")
conn = sqlite3.connect("recipes.db")
c = conn.cursor()
c.execute("SELECT id, title FROM recipes")
recipes = c.fetchall()

for recipe_id, recipe_title in recipes:
    with st.expander(recipe_title):
        # Show ingredients
        c.execute("SELECT ingredient FROM ingredients WHERE recipe_id = ?", (recipe_id,))
        ingredients = c.fetchall()
        st.write("**Ingredients:**")
        for ingredient, in ingredients:
            st.write(f"- {ingredient}")

        # Show steps
        c.execute("SELECT step_order, description FROM steps WHERE recipe_id = ? ORDER BY step_order", (recipe_id,))
        steps = c.fetchall()
        st.write("**Steps:**")
        for order, description in steps:
            st.write(f"{order}. {description}")

        # Delete recipe button
        if st.button(f"Delete {recipe_title}", key=f"delete_{recipe_id}"):
            delete_recipe(recipe_id)
            st.success(f"Recipe '{recipe_title}' deleted successfully!")
            st.experimental_rerun()

conn.close()
