# huesli

<h1> Simple Flask Furniture Inventory Application </h1>

<h2> Description </h2>

    Web-Based Interface: Access your furniture inventory through a sleek and intuitive web interface, designed for ease of use.
    Database Integration: At the heart of our application lies a database that stores all your entries to furniture inventory details.
    Display in Table Format: View your entire furniture collection in table format, making it easy to browse and understand your inventory at a glance.
    CRUD Operations: The application supports Create, Read, Update, and Delete (CRUD) operations, allowing you to:
        Add New Entries: Seamlessly add new furniture items to your inventory.
        Remove Entries: Delete items from your inventory when they are no longer available or needed.
        Update Existing Entries: Modify the details of existing furniture items as needed.
    Search and Filter: Implement search and filtering capabilities to quickly find specific items or categories within your inventory.
    Template-Driven: Utilizes Flask's templating features to render HTML dynamically, offering a consistent and responsive user interface.

<h2> Technologies Used: </h2>

    Flask: A lightweight WSGI web application framework in Python, providing tools, libraries, and technologies for building web applications.
    HTML/CSS: For structuring and styling the web interface.
    Database Management System: A backend database to store and manage the furniture data efficiently.
    

<h2> Installation and Setup </h2>

git clone [repository URL]
cd [local repository]
pip install pipenv



<h2> Running Application Locally </h2>

<h3>with Docker</h3>
# modify Dockerfile, by replacing last command with
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]

docker build -t huesli .
docker run -p 5000:5000 huesli

<h3>without Docker</h3>
pipenv shell
pipenv install 
flask run

