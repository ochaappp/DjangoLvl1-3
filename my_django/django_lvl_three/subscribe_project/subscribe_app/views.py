from django.shortcuts import render
from subscribe_app.models import Customer

# Create your views here.
def index(request):
    return render(request, 'subscribe_app/index.html')

def customers(request):
    Customer_list = Customer.objects.order_by('first_name')
    Customer_dict = {'customers':Customer_list}
    return render(request, 'subscribe_app/customers.html', context=customer_dict)

