# Welcome to Our Project Repository!

## About the Projects
This repository contains two versions of our project: `thejokers_dev` and `thejokers2_dev`. Each version is tailored for a specific operating system:

- **thejokers_dev**: This version is optimized for macOS.
- **thejokers2_dev**: This version is optimized for Windows.

## Getting Started
To get started with the project, follow these steps based on your operating system:

### For macOS Users (thejokers_dev)
1. Clone the repository: git clone https://github.com/thejokers69/myVirtualEnv

2. Checkout the appropriate branch based on your operating system:
- For macOS:
  ```
  git checkout thejokers_dev
  ```
- For Windows:
  ```
  git checkout thejokers2_dev
  ```

3. Follow the instructions provided in the respective branch's README.md file for setup and usage.

## Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---


# Using Models and Admin Site in Django

Welcome to our Django project repository! This README will guide you through working with models and the admin site.

## 1. Defining Models

We have defined models for `Program`, `Subject`, and `Student` in their respective apps. Here's a brief overview:

### Program Model (program/models.py)

- `Program`: Represents a program with fields such as name, description, and registration fees.
- `RegistersFor`: Represents the relationship between programs and students.

### Student Model (student/models.py)

- `Student`: Represents a student with fields like first name, last name, birth date, email, and program ID.

### Subject Model (subject/models.py)

- `Subject`: Represents a subject with fields like name, description, and class hours.

## 2. Using Admin Site

To manage our models easily, we utilize the Django admin site. Here's how to get started:

### Register Models in Admin Site

In each app's `admin.py` file, models need to be registered to access them in the admin site.

#### Registering Models

- In the `program` app, register `Program` and `RegistersFor` models.
- In the `student` app, register the `Student` model.

### Create a Superuser

To access the admin site, you need a superuser account. Run the following command and follow the prompts:

```bash
python manage.py createsuperuser


## Log in to Admin Site

Start the Django development server: python manage.py runserver

Then, navigate to http://127.0.0.1:8000/admin in your browser. Log in using the superuser credentials created earlier.

##Explore Admin Site
Once logged in, you can:

View, add, edit, and delete instances of registered models.
Search for specific instances.
Filter instances based on certain criteria.
Conclusion
You're now equipped to work with models and the admin site in our Django project. Feel free to explore and manage data efficiently using the admin interface!

Feel free to modify this README according to your project's specific details and requirements!



