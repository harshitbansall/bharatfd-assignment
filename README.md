
# BharatFD Backend Assignment

This repository contains the backend solution for the BharatFD assignment. The code is built as per the provided instructions and is available in the `main` branch.

# Table of Contents

1. [🚀 Deployment](#deployment)
2. [🔑 Admin Site](#admin-site)
3. [🌟 Features Implemented](#features-implemented)
4. [⚙️ Quick Setup without Docker](#quick-setup-without-docker)
5. [🐳 Quick Setup with Docker](#quick-setup-with-docker)
6. [📡 API Usage](#api-usage)
7. [💬 Contribution Guidelines](#contribution-guidelines)

## 🚀 Deployment

The project is deployed on a DigitalOcean droplet. You can access the application via the following link:

[http://bharatfd-assignment.devharshit.in](http://bharatfd-assignment.devharshit.in)

## 🔑 Admin Site

You can access the Django admin site for the project at:

[http://bharatfd-assignment.devharshit.in/admin](http://bharatfd-assignment.devharshit.in/admin)

Use the following credentials to log in:

- **Username**: `test`
- **Password**: `123456789`

## 🌟 Features Implemented:

- ✅ Automatic Translations while object creation
- ✅ Multi-language translation using Google Translate
- ✅ REST API with language selection
- ✅ Individual FAQ translation and caching
- ✅ Redis caching for improved performance
- ✅ Unit tests for models and API

## ⚙️ Quick Setup (Without Docker 🐳)

To set up the project, install dependencies, and run the application, execute the following commands:

```bash
git clone https://github.com/harshitbansall/bharatfd-assignment.git
cd bharatfd-assignment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

To run tests, use:

```bash
source venv/bin/activate
pytest
```

## ⚙️ Quick Setup (With Docker 🐳)

To set up the project with Docker, you can use the following command:

```bash
git clone https://github.com/harshitbansall/bharatfd-assignment.git
cd bharatfd-assignment
docker compose up --build
```

This will build the Docker image and run the application in the container, exposing the app on `http://localhost:80`. 


## 📡 API Usage
- For Localhost
```bash
# Fetch FAQs in English (default)
curl http://localhost:8000/api/faqs/

# Fetch FAQs in Hindi
curl http://localhost:8000/api/faqs/?lang=hi

# Fetch FAQs in Bengali
curl http://localhost:8000/api/faqs/?lang=bn
```

- For Deployment
```bash
# Fetch FAQs in English (default)
curl http://bharatfd-assignment.devharshit.in/api/faqs/

# Fetch FAQs in Hindi
curl http://bharatfd-assignment.devharshit.in/api/faqs/?lang=hi

# Fetch FAQs in Bengali
curl http://bharatfd-assignment.devharshit.in/api/faqs/?lang=bn
```

# Schema
![Screenshot 2025-02-01 at 9 08 29 PM](https://github.com/user-attachments/assets/5fc58041-0d22-40a8-a445-5c1d88b8954f)


# 📝 Contribution Guidelines

Thank you for considering contributing to the BharatFD Backend Assignment! We welcome contributions to make the project better. Please follow the steps below to get started:

## 🛠️ How to Contribute

1. **Fork the repository**  
   Click the "Fork" button at the top-right of the repository to create a copy of the repository under your GitHub account.

2. **Clone your forked repository**  
   Clone the forked repository to your local machine.

   ```bash
   git clone https://github.com/YOUR-USERNAME/bharatfd-assignment.git
   ```
2. **Create a new branch**  
   Before making changes, create a new branch to work on your feature or fix.

   ```bash
   git checkout -b feature-or-fix-name
   ```
3. **Make your changes**
   Make your changes to the project. Ensure your code follows the PEP 8 style guide for Python code and includes proper documentation.

4. **Test your changes**
   Ensure that your changes are covered by tests, and run all tests to verify everything works correctly.
   ```bash
   source venv/bin/activate
   pytest
   ```
5. **Commit and Push**
   Commit and push your changes to your forked repo.

6. **Create a Pull Request (PR)**
    Go to the original repository and create a pull request to merge your changes. Provide a detailed description of the changes and why they are needed.
   
## Contact

If you have any questions or need further information, feel free to reach out at [harshitbansal587@gmail.com](mailto:harshitbansal587@gmail.com).
