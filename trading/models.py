from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from bs4 import BeautifulSoup
from urllib.request import urlopen


# Create your models here.


class Card(models.Model):
    options = [('L', 'list'),
               ('K', 'keep')]

    name = models.CharField(max_length=500)
    power = models.IntegerField()
    details = models.URLField()
    owner = models.ForeignKey(Profile, on_delete=models.PROTECT)
    status = models.CharField(choices=options, default='list', max_length=900)
    picture = models.URLField(default='https://bit.ly/3uY7NAX')
    type = models.CharField(default='regular', max_length=200)
    color = models.CharField(default='#ffffff', max_length=200)

    def __str__(self):
        return self.name

    def get_picture(self):
        url_to_scrape = self.details

        r = urlopen(url_to_scrape)
        page_html = r.read()
        r.close()

        html_soup = BeautifulSoup(page_html, 'html.parser')

        wrap = html_soup.find('figure', class_="img__wrapper masthead__background")
        a_div = wrap.find('div')
        pic_url = a_div.attrs['style'].split("'")[1]
        self.picture = pic_url
        self.save()


class Transaction(models.Model):
    options = [('A', 'accepted'),
               ('D', 'declined'),
               ('P', 'pending')]

    offered_price = models.IntegerField()
    bid_status = models.CharField(choices=options, default='pending', max_length=900)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, max_length=900, related_name='buyer')
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, max_length=900, related_name='seller')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    buyer_update = models.CharField(default='n', max_length=100)

    def accept(self):
        self.bid_status = 'accepted'
        self.buyer.coins -= self.offered_price
        self.seller.coins += self.offered_price
        self.buyer.rank += self.card.power
        self.seller.rank -= self.card.power
        self.card.owner = self.buyer
        self.buyer.save()
        self.seller.save()
        self.card.save()
        self.save()

    def decline(self):
        self.bid_status = 'declined'
        self.save()
