# Import the HttpResponse module to send data from view to template
from django.http import HttpResponse
# Import view module
from django.views import View
# Import random module
import random

# Define class for class-based views
class MyView(View):

    def get(self, request):
        # Declare the list variable
        listdata = []
        # Add the first element of the list
        listdata.append('<center><h2>The list of 10 random numbers are:</h2>')
        # Iterate the loop for 10 times
        for n in range(10):
            # Generate a random number within 1 to 50
            random_number = random.randint(1, 50)
            # Add the random number in the list
            listdata.append(random_number)
            # Add a break element in the list
            listdata.append('<br/>')
        # Add the last element of the list
        listdata.append('</center>')
        # Send the list values to the browser
        return HttpResponse(listdata)