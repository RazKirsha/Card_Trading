from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .api_connect import create_card
from trading.models import Card
from django.views.generic import ListView
from .filters import CardFilter


class Homepage(ListView):
    template_name = 'homepage.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CardFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Card.objects.filter(status='list').exclude(owner=self.request.user.profile).order_by('-power')


def signup(request):
    form = CustomCreationForm()
    profile_form = CharacterForm()
    if request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            new_user = Profile.objects.create(user=user)
            new_user.rank = 0
            for _ in range(7):
                card = create_card()
                type_color = {'regular': '#ffffff', 'silver': '#9F9F9F', 'gold': '#FDBE00', 'premium': '#5E839B'}
                new_card = Card.objects.create(name=card[0], power=card[1], details=card[2], type=card[3],
                                               color=type_color[card[3]],
                                               owner=new_user)
                if "/comics/" not in card[2]:
                    new_card.get_picture()
                new_user.rank += int(card[1])
            new_user.coins = 7500
            new_user.save()
            profile_form = CharacterForm(request.POST, instance=new_user)
            if profile_form.is_valid():
                profile_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'registration/signup.html', {'form': form, 'profile_form': profile_form})


@login_required
def user_profile(request):
    cards = Card.objects.filter(owner=request.user.profile).order_by('-power')
    cards_num = Card.objects.filter(owner=request.user.profile).count()
    filter = CardFilter(request.GET, queryset=cards)
    return render(request, 'user_profile.html', {'cards': cards, 'filter': filter, 'count': cards_num})


@login_required
def change_status(request, pk):
    if request.method == 'GET':
        return render(request, 'change_status.html')

    else:
        card = Card.objects.get(id=pk)
        if card.status == 'list':
            card.status = 'keep'
            card.save()
        else:
            card.status = 'list'
            card.save()
        messages.success(request, 'status was changed')

    return redirect('profile')
