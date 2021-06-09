from django.urls import path
from . import views

urlpatterns = [
    path('bid/<int:pk>', views.bid, name='bid'),
    path('my_sellings/', views.my_sellings, name='my_sellings'),
    path('accept_bid/<int:pk>', views.accept_bid, name='accept_bid'),
    path('decline_bid/<int:pk>', views.decline_bid, name='decline_bid'),
    path('buy_pack/<int:pk>', views.buy_pack, name='buy_pack'),
    path('my_bids/', views.my_bids, name='my_bids'),
]
