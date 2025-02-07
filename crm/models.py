from django.db import models


class Product(models.Model):

    name=models.CharField(max_length=100)

    price=models.PositiveIntegerField()

    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):

    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    reviewer_name=models.CharField(max_length=100)

    rating=models.IntegerField()

    comment=models.CharField(max_length=100)

    review_date=models.DateField()