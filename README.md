# Veterinary Services Backend

This is the backend server for a comprehensive veterinary services management system. It provides API endpoints to interact with the database containing information about users, veterinaries, services, pet items, and pets.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Sample Requests](#sample-requests)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

The Veterinary Services Backend is a Flask-based server designed to handle the data management and operations for a veterinary service platform. It offers a robust set of API endpoints for user management, veterinary services, pet information, and more.

## Features

- User authentication and registration
- Comprehensive veterinary information management
- Service types and offerings
- Pet items and their associated prices
- Pet registration and ownership

---

## Getting Started

### Installation

To get started, clone the repository:

 bash
git clone git@github.com:RotichKipkoech/pets-database.git

## Dependencies

Create and activate a virtual environment:

 * bash

 * python3 -m venv venv
 * source venv/bin/activate

### Install the required dependencies:

* bash

 * pip install -r requirements.txt

## Project Structure

graphql

├── app.py                 # Main application file
├── config.py              # Configuration file for the Flask app
├── models.py              # Database models and schema definitions
├── routes.py              # API endpoints and routes
└── venv/                  # Virtual environment (not included in repository)

## Running the Server

To start the server, run:

bash

* python app.py

The server will start at https://pets-backend-nlog.onrender.com.
API Endpoints

    GET /users: Get all users.
    POST /users: Create a new user.
    GET /veterinary: Get all veterinaries.
    GET /pets: Get all pets.
    GET /petitems: Get all pet items.
    GET /services: Get all services.
    POST /users: Create a new user.
    PUT /users/<int:user_id>: Update user details.
    PATCH /users/<int:user_id>: Partially update user details.


## Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, please feel free to reach out to:

    Kennedy Rotich | Alex Irungu
    Email: kipkoechrottich@gmail.com | Irungualex@gmail.com