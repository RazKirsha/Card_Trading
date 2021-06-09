from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.api_connect import create_card


# Create your views here.
@login_required
def bid(request, pk):
    form = MakeBidModelForm()
    if request.method == 'GET':
        return render(request, 'bidding_page.html', {'form': form})

    else:
        click = request.POST
        form = MakeBidModelForm(click)
        card_details = Card.objects.get(id=pk)
        if form.is_valid():
            if int(click['offered_price']) < int(request.user.profile.coins):
                bid = form.save(commit=False)
                bid.bid_status = 'Pending'
                bid.buyer = request.user.profile
                bid.seller = card_details.owner
                bid.card = card_details
                bid.save()
                messages.success(request, 'Bid was made')
                return redirect('profile')

            else:
                messages.error(request, 'Not enuoght coins for this bid!')
                form = MakeBidModelForm()
                return render(request, 'bidding_page.html', {'form': form})
        else:
            messages.error(request, 'Bad form input')
            return redirect('profile')


@login_required
def my_sellings(request):
    data = Transaction.objects.filter(seller=request.user.profile).filter(bid_status='Pending')

    if request.method == 'GET':
        return render(request, 'my_sellings.html', {'data': data})


@login_required
def accept_bid(request, pk):
    spec_bid = Transaction.objects.get(id=pk)
    if request.user.profile != spec_bid.seller:
        messages.warning(request, "Don't be a cheeky bastard!")
        return redirect('profile')

    if request.method == 'GET':
        return render(request, 'accept_bid.html')

    else:
        spec_bid.accept()
        messages.success(request, 'Transaction was made successfully!')

    return redirect('profile')


@login_required
def decline_bid(request, pk):
    if request.method == 'GET':
        return render(request, 'reject_bid.html')

    else:
        spec_bid = Transaction.objects.get(id=pk)
        spec_bid.decline()
    return redirect('profile')


@login_required
def buy_pack(request, pk):
    if request.method == 'GET':
        return render(request, 'buy_pack.html')

    else:
        player = Profile.objects.get(id=pk)
        if player.coins >= 3000:
            for _ in range(5):
                card = create_card()
                type_color = {'regular': '#ffffff', 'silver': '#a4a4a4', 'gold': '#FDBE00', 'premium': '#5E839B'}
                new_card = Card.objects.create(name=card[0], power=card[1], details=card[2], type=card[3],
                                               color=type_color[card[3]],
                                               owner=player)
                if "/comics/" not in card[2]:
                    new_card.get_picture()
                player.rank += int(card[1])

            player.coins -= 3000
            player.save()
            messages.success(request, 'pack has been bought!')
        else:
            messages.error(request, 'Not enough coins')
        return redirect('profile')


@login_required
def my_bids(request):
    data = Transaction.objects.filter(buyer=request.user.profile).filter(buyer_update='n')

    if request.method == 'GET':
        return render(request, 'my_bids.html', {'data': data})

    else:
        offer_id = request.POST['id']
        offer = Transaction.objects.get(id=offer_id)
        print('\n')
        print('---------------')
        print(offer.card.name)
        print(offer.buyer_update)
        print('---------------')
        print('\n')
        offer.buyer_update = 'r'
        print('\n')
        print('---------------')
        print(offer.buyer_update)
        print('---------------')
        print('\n')
        offer.save()
        return redirect('profile')
