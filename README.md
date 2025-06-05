# 🍲 Recipe Book Backend - Database Schema

This project is a backend database model for a **Recipe Book** system. It includes tables and relationships for storing recipes, ingredients, and their associations, optimized for querying, managing, and extending recipe data.

---

## 🗂️ Entity-Relationship Overview

The system uses three core tables:

### 1. **Recipe**
Stores detailed information about a recipe.

| Field         | Type        | Description                    |
|---------------|-------------|--------------------------------|
| recipeID      | varchar(20) | Primary key                    |
| cuisineName   | varchar(50) | Type of cuisine (e.g., Italian)|
| categoryName  | varchar(20) | Category (e.g., Dessert)       |
| recipeName    | varchar(50) | Name of the recipe             |
| duration      | int         | Preparation time in minutes    |
| serving       | int         | Number of servings             |
| description   | varchar     | Short description              |
| procedure     | varchar     | Cooking instructions           |
| img_url       | Type        | Link or path to image          |
| favorite      | boolean     | Whether it's marked as favorite|
| date          | date        | Date added                     |

---

### 2. **Ingredients**
Stores information about each ingredient.

| Field           | Type         | Description                 |
|------------------|--------------|-----------------------------|
| ingredientID     | varchar(20)  | Primary key                 |
| ingredientName   | varchar(50)  | Name of the ingredient      |
| measure          | float        | Default amount per use      |
| unit             | varchar(10)  | Unit of measure (e.g., g, ml)|

---

### 3. **have** (Join Table)
A many-to-many relationship between Recipes and Ingredients.

| Field         | Type   | Description                          |
|---------------|--------|--------------------------------------|
| recipeID      | int    | Foreign key → Recipe.recipeID        |
| ingredientID  | int    | Foreign key → Ingredients.ingredientID |
| quantity      | int    | Quantity of ingredient in the recipe |

> `recipeID` and `ingredientID` act as a composite primary key.

---

## 🔗 Relationships

- A **Recipe** can have **many Ingredients**.
- An **Ingredient** can appear in **many Recipes**.
- These are connected via the **`have`** join table.

---

## 🛠️ Technologies Used

- **ERD**: Designed using Lucidchart
- **Backend**: Django
- **Fronted**: vuejs
- **Database**: SQLite
