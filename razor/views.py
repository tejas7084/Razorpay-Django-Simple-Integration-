from django.shortcuts import render, redirect
from .models import Razorpay
from .forms import RazorpayForm
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def payment_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        services = request.POST.get('services')
        client = razorpay.Client(
            auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

        razorpay_payment = client.order.create(
            dict(amount=amount, currency='INR'))

        order_id = razorpay_payment['id']
        order_status = razorpay_payment['status']

        if order_status == 'created':
            razorpay_save = Razorpay(
                name=name,
                amount=amount,
                services=services,
                order_id=order_id
            )
            razorpay_save.save()
            razorpay_payment['name'] = name
            razorpay_payment['amount'] = amount
            razorpay_payment['order_id'] = order_id

            form = RazorpayForm(request.POST or None)
            return render(request, 'payment.html', {'form': form, 'razorpay_payment': razorpay_payment})
    form = RazorpayForm()
    return render(request, 'payment.html', {'form': form})


@csrf_exempt
def success(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature'],
    }

    client = razorpay.Client(
        auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        razorpay_save = Razorpay.objects.get(
            order_id=response['razorpay_order_id'])
        razorpay_save.razorpay_payment_id = response['razorpay_payment_id']
        razorpay_save.paid = True
        razorpay_save.save()
        return render(request, 'success.html', {'status': True})
    except:
        return render(request, "success.html", {'status': False})
