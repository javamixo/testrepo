from django.shortcuts import render, redirect
from .forms import OrderCakeForm
from .models import Cake, Ingredient, CakeIngredient

def order_cake(request):
    if request.method == 'POST':
        form = OrderCakeForm(request.POST)
        if form.is_valid():
            cake_name = form.cleaned_data['cake_name']
            amount_kg = form.cleaned_data['amount_kg']

            # You can now process the order here.
            # For example, you might create an Order object and
            # update the database with the ordered cake and amount.
            # For now, we'll just print the data.
            print(f"Ordered Cake: {cake_name}, Amount: {amount_kg} kg")
            return redirect('cake_list')  # Redirect to cake list or another page
    else:
        form = OrderCakeForm()

    return render(request, 'cakes/order_cake.html', {'form': form})