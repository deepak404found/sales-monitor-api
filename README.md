# 🚀 Sales Monitor API  

The **Sales Monitor API** is a powerful backend solution built using **Django Rest Framework (DRF)**. It allows users to monitor product sales, track sales performance, and analyze data through dynamic charts.  

This API provides a structured and secure way to handle product and sales data using **JWT-based authentication** for access control. The API includes endpoints for user registration, product listing, and sales insights, making it easy to integrate with a frontend for a complete monitoring solution.

## ✅ **Features**  

- **User Management**: Register and login users with JWT authentication.
- **Product Management**: List, filter, and categorize products.
- **Sales Monitoring**: Track sales data and generate charts for sales and items sold.

## 🛠️ **Installation**  

1. Clone the repository.
2. Install Poetry and dependencies:

    Install Poetry using `curl`:

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    Add Poetry to your PATH:

    ```sh
    export PATH="$HOME/.local/bin:$PATH"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

    Install dependencies:

    ```sh
    poetry install
    ```

3. Activate the Poetry Environment:

    ```sh
    poetry shell
    ```

4. Make Migrations and Migrate:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Add sample data:

    ```sh
    python manage.py runscript addSampleProducts
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

## 🌐 Usage

- **User Registration**: `POST /api/users/register`
- **User Login**: `POST /api/users/login`
- **Product List**: `GET /api/products/list?category=category_name&search=search_query&ordering=ordering_field&limit=limit&offset=offset`
- **Sales Chart**: `GET /api/products/sales_chart`
- **Items Chart**: `GET /api/products/items_chart`

## 📚 **Postman Documentation**

The API documentation is available in the Postman collection below:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/17055995/2sAYkAPh7S)