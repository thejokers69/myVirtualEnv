import os

# Define the directory structure
structure = {
    'covoiturage_universitaire': [
        '__init__.py',
        'settings.py',
        'urls.py',
        'wsgi.py',
        'asgi.py',
    ],
    'app': [
        '__init__.py',
        'admin.py',
        'apps.py',
        'models.py',
        'tests.py',
        'views.py',
        'urls.py',
        'templates/base.html',
        'templates/admin_dashboard.html',
        'templates/user_list.html',
        'templates/trip_list.html',
        'templates/reservation_list.html',
        'templates/report.html',
        'static/css/',
        'static/js/'
    ]
}

# Create the files and directories
for folder, files in structure.items():
    for file in files:
        filepath = os.path.join(folder, file)
        if file.endswith('/'):
            os.makedirs(filepath, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as f:
                pass  # Just create an empty file

print("Project structure created successfully.")
