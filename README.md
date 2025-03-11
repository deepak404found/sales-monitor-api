# Sales Monitor API

This is a simple API that allows you to monitor sales of a product. It is built using Django Rest Framework.

## Overview

The Sales Monitor API is a Django-based application that allows users to monitor sales of various products. It leverages the Django Rest Framework (DRF) for building the API and includes JWT-based authentication for secure access.

## Features

- **User Management**: Register and login users with JWT authentication.
- **Product Management**: List, filter, and categorize products.
- **Sales Monitoring**: Track sales data and generate charts for sales and items sold.

## Installation

1. Clone the repository.
2. Install dependencies using Poetry:

    ```sh
    poetry install
    ```

3. Apply migrations:

    ```sh
    python manage.py migrate
    ```

4. Add sample data:

    ```sh
    python manage.py runscript addSampleProducts
    ```

5. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

- **User Registration**: `POST /api/users/register`
- **User Login**: `POST /api/users/login`
- **Product List**: `GET /api/products/list`
- **Sales Chart**: `GET /api/products/sales_chart`
- **Items Chart**: `GET /api/products/items_chart`

## License

This project is licensed under the MIT License.
