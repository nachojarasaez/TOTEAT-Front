from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
import requests 

from rest_framework.views import APIView
from rest_framework.response import Response



class ProductsView(View):
    def get(self, request, *args, **kwargs):
        print(request)
        if 'month' in request.GET.keys():
            if 'day' in request.GET.keys():
                return render(request, 'productsCharts.html', {"month":request.GET['month'], "day": request.GET['day']})
            else: 
                return render(request, 'productsCharts.html', {"month":request.GET['month'], "day": ''})
        else:
            return render(request, 'productsCharts.html', {"value":"", "day": ''})


def get_products(request, *args, **kwargs):
    url = "https://mysterious-reef-10731.herokuapp.com/app/stadistics/products"
    if 'month' in request.GET.keys() and request.GET['month'] != '4':
        url += '?month='+request.GET['month']
        if 'day' in request.GET.keys() and request.GET['day'] != '0':
            url += '&day='+request.GET['day']
    print(url)
    data = requests.get(url)
    data = data.json()
    labels = {'1':list(data['category'].keys()), '2':list(data['product'].keys())}
    default_items = {'1':[i for i in data['category'].values()], '2':[i['quantity'] for i in data['product'].values()]}
    data = {"labels": labels, "default": default_items}

    return JsonResponse(data) # http response


class GeneralsView(View):
    def get(self, request, *args, **kwargs):
        print(request.GET)
        if 'modalidad' in request.GET.keys():
            print('hola')
            return render(request, 'generalsCharts.html', {"month":request.GET['month'], "modality": request.GET['modalidad']})
        else:
            print("holaaaaa")
            return render(request, 'generalsCharts.html', {"modality":"", "month": ''})


def get_generals(request, *args, **kwargs):
    url = "https://mysterious-reef-10731.herokuapp.com/app/stadistics/generals"
    print(request.GET.keys())

    if 'modality' in request.GET.keys():
        url += '?modality=2&month='+request.GET['month']
    else:
        labels = ["Enero", 'Febrero', "Marzo"]
        labels = {'1':labels,'2':labels}

    data = requests.get(url)
    data = data.json()
    if 'modality' in request.GET.keys():
        labels = {'1':list(data['total'].keys()),'2':list(data['total'].keys())}
    default_items = {'1':[i['atencion'] for i in data['total'].values()], '2':[i['total'] for i in data['total'].values()]}
    data = {"labels": labels, "default": default_items}
    print(data)

    return JsonResponse(data) # http response

class WorkersView(View):
    def get(self, request, *args, **kwargs):
        print(request)
        if 'month' in request.GET.keys():
            if 'day' in request.GET.keys():
                return render(request, 'workersCharts.html', {"month":request.GET['month'], "day": request.GET['day']})
            else: 
                return render(request, 'workersCharts.html', {"month":request.GET['month'], "day": ''})
        else:
            return render(request, 'workersCharts.html', {"month":"", "day": ''})


def get_workers(request, *args, **kwargs):
    url = "https://mysterious-reef-10731.herokuapp.com/app/stadistics/workers"
    if 'month' in request.GET.keys() and request.GET['month'] != '4':
        url += '?month='+request.GET['month']
        if 'day' in request.GET.keys() and request.GET['day'] != '0':
            url += '&day='+request.GET['day']
    data = requests.get(url)
    data = data.json()
    titles = []
    tag = ['de millones de peso', "de mesas atendidas", 'de atenciones']
    if 'month' in request.GET.keys() and request.GET['month'] != '4':
        mes = request.GET['month']
        if mes == '1':
            month = 'Enero'
        elif mes == '2':
            month = 'Febrero'
        else:
            month = 'Marzo'
        if 'day' in request.GET.keys() and request.GET['day'] != '0':
            titles.append('Total de Ventas por Mesero - '+request.GET['day']+'de '+month)
            titles.append('Cantidad de mesas atendidas por Mesero - '+request.GET['day']+'de '+month)
            titles.append('Cantidad de Atenciones por Cajero - '+request.GET['day']+'de '+month)
        else:
            titles.append('Total de Ventas por Mesero - ' + month)
            titles.append('Cantidad de mesas atendidas por Mesero - ' + month)
            titles.append('Cantidad de Atenciones por Cajero - ' + month)
    else:
        titles.append('Total de Ventas por Mesero - Anual')
        titles.append('Cantidad de mesas atendidas por Mesero - Anual')
        titles.append('Cantidad de Atenciones por Cajero - Anual')
    labels = {'1':list(data['waiter'].keys()), '2':list(data['waiter'].keys()), '3':list(data['cashier'].keys())}
    default_items = {'1':[i['total'] for i in data['waiter'].values()], '2':[i['quantity'] for i in data['waiter'].values()], '3':[i['quantity'] for i in data['cashier'].values()]}
    data = {"labels": labels, "default": default_items, "titles" : titles, 'tag': tag}

    return JsonResponse(data) # http response


