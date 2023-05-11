from django.shortcuts import render

# Create your views here.
# Import the date module to read the current date
from datetime import date
# Import the HttpResponse module to send data from view to template
from django.http import HttpResponse

# Define function to create function-based view
def index(request):
    # Read the current date
    today = date.today()
    # Set static data for the view
    content = "<center><h1 style='color:green'>Welcome to Stupendous Sloths</h1><h2>"
    content += "Today is " + today.strftime("%B") + " " + today.strftime("%d") + ", " + str(today.year) + "</h2></center>"
    # Sent the content to the browser
    return HttpResponse(content)
