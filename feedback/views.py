from django.shortcuts import render, get_object_or_404
from .models import FeedbackItem

def home(request):
    return render(request, 'feedback/home.html')

def item_list(request):
    items = FeedbackItem.objects.all()
    return render(request, 'feedback/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(FeedbackItem, pk=pk)
    return render(request, 'feedback/item_detail.html', {'item': item})
