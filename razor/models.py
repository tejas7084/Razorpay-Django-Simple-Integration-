from django.db import models
# Create your models here.


class Razorpay(models.Model):

    SERVICES_CHOICES = (
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
    )

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    services = models.CharField(
        max_length=100, choices=SERVICES_CHOICES, default="small")
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        if self.paid == True:
            return self.name + " paid"
        else:
            return self.name + " not paid"
