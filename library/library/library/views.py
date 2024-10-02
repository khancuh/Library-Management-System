from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import connect_to_newdb  # Import the database connection function
# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'library/login.html')

# Home view
@login_required
def home_view(request):
    return render(request, 'library/home.html')

# Issue book view
@login_required
def issue_book_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        issue_date = request.POST.get('issue_date')

        # Connect to the MySQL database
        db = connect_to_newdb()
        cursor = db.cursor()

        try:
            # SQL query to insert the book issue data into the database
            query = """
                INSERT INTO td (first_name, last_name, book_name, author, issue_date)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (first_name, last_name, book_name, author, issue_date))

            # Commit the transaction
            db.commit()

            messages.success(request, "Book issued successfully!")

        except Exception as e:
            db.rollback()  # Rollback in case of error
            messages.error(request, f"Error issuing the book: {e}")

        finally:
            # Close the connection
            cursor.close()
            db.close()

    return render(request, 'library/issue_book.html')


# Return book view
@login_required
def return_book_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        return_date = request.POST.get('return_date')

        # Connect to the MySQL database
        db = connect_to_newdb()
        cursor = db.cursor()

        try:
            # SQL query to insert the book return data into the td1 table
            query = """
                INSERT INTO td1 (first_name, last_name, book_name, author, return_date)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (first_name, last_name, book_name, author, return_date))

            # Commit the transaction
            db.commit()

            # Success message to the user
            messages.success(request, "Your book is successfully returned!")

        except Exception as e:
            # Rollback the transaction in case of error
            db.rollback()
            messages.error(request, f"Error returning the book: {e}")

        finally:
            # Close the database connection
            cursor.close()
            db.close()

    return render(request, 'library/return_book.html')
