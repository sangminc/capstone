# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from capstone.forms import *
import csv

# Create your views here.

def index(request):
	context = {}
	if request.method == 'GET':
		#context['form'] = KPIForm()
		return render(request, 'capstone/index.html', context)
	if request.method == 'POST':
		#form = KPIForm(request.POST, extra=request.POST.get('extra_field_count'))
		#context['form'] = form
		# if not form.is_valid():
		# 	return render(request, 'capstone/index.html', context)

		# context['kpi1'] = form.cleaned_data['kpi1']
		# context['kpi2'] = form.cleaned_data['kpi2']
		# context['kpi3'] = form.cleaned_data['kpi3']
		# context['kpi4'] = form.cleaned_data['kpi4']
		# context['kpi5'] = form.cleaned_data['kpi5']
		error = []
		available = {}
		if 'kpi_1' in request.POST and request.POST['kpi_1']:
			try:
				if float(request.POST['kpi_1']) < 1 or float(request.POST['kpi_1']) > 6:
					error.append("Threshold 1 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 1 must be a number")
			context['kpi_1'] = request.POST['kpi_1']

		if 'kpi_2' in request.POST and request.POST['kpi_2']:
			try:
				if float(request.POST['kpi_2']) < 1 or float(request.POST['kpi_2']) > 6:
					error.append("Threshold 2 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 2 must be a number")
			context['kpi_2'] = request.POST['kpi_2']

		if 'kpi_3' in request.POST and request.POST['kpi_3']:
			try:
				if float(request.POST['kpi_3']) < 1 or float(request.POST['kpi_3']) > 6:
					error.append("Threshold 3 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 3 must be a number")
			context['kpi_3'] = request.POST['kpi_3']

		if 'kpi_4' in request.POST and request.POST['kpi_4']:
			try:
				if float(request.POST['kpi_4']) < 1 or float(request.POST['kpi_4']) > 6:
					error.append("Threshold 4 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 4 must be a number")
			context['kpi_4'] = request.POST['kpi_4']

		if 'kpi_5' in request.POST and request.POST['kpi_5']:
			try:
				if float(request.POST['kpi_5']) < 1 or float(request.POST['kpi_5']) > 6:
					error.append("Threshold 5 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 5 must be a number")
			context['kpi_5'] = request.POST['kpi_5']

		if 'kpi_6' in request.POST and request.POST['kpi_6']:
			try:
				if float(request.POST['kpi_6']) < 1 or float(request.POST['kpi_6']) > 6:
					error.append("Threshold 6 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 6 must be a number")
			context['kpi_6'] = request.POST['kpi_6']

		if 'kpi_7' in request.POST and request.POST['kpi_7']:
			try:
				if float(request.POST['kpi_7']) < 1 or float(request.POST['kpi_7']) > 6:
					error.append("Threshold 7 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 7 must be a number")
			context['kpi_7'] = request.POST['kpi_7']

		if 'kpi_8' in request.POST and request.POST['kpi_8']:
			try:
				if float(request.POST['kpi_8']) < 1 or float(request.POST['kpi_8']) > 6:
					error.append("Threshold 8 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 8 must be a number")
			context['kpi_8'] = request.POST['kpi_8']

		if 'kpi_9' in request.POST and request.POST['kpi_9']:
			try:
				if float(request.POST['kpi_9']) < 1 or float(request.POST['kpi_9']) > 6:
					error.append("Threshold 9 must inbetween 1 and 6")
			except ValueError:
				error.append("Threshold 9 must be a number")
			context['kpi_9'] = request.POST['kpi_9']
		if error:
			context['errors'] = error
			return render(request, 'capstone/index.html', context)

		with open("kpi_threshold.csv", 'wb') as f:
			writer = csv.writer(f, delimiter=str(","), quotechar=str('|'), quoting=csv.QUOTE_MINIMAL)
			writer.writerow(['KPI', 'Threshold'])
			for key, value in context.iteritems():
				writer.writerow([key.split('_')[1], value])
			# writer.writerow(['1', context['kpi1']])
			# writer.writerow(['2', context['kpi2']])
			# writer.writerow(['3', context['kpi3']])
			# writer.writerow(['4', context['kpi4']])
			# writer.writerow(['5', context['kpi5']])
			# writer.writerow(['6', context['kpi6']])
			# writer.writerow(['7', context['kpi7']])
			# writer.writerow(['8', context['kpi8']])
			# writer.writerow(['9', context['kpi9']])

		return render(request, 'capstone/confirmKPI.html', context)







