# Ecommerce Website

A Django-based ecommerce site with user authentication, a product catalog, and a shopping cart.

## Features
* **Pages** — home, product listing, about us, contact
* **Authentication** — signup and login
* **Shopping cart** — per-user cart storing product name, description, price, image, and quantity

## Tech Stack
Django · SQLite

## Setup

```
cd Ecommerce_Website
pip install django pillow
python manage.py migrate
python manage.py runserver
```

## Known issue
`add_to_cart` in `views.py` currently references a `products` relation on `User_Cart` that isn't defined on the model — this needs to be reconciled (either add a many-to-many `products` field, or rewrite the view to populate `User_Cart`'s existing fields directly) before cart-adding will work end-to-end.
