from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.cache import cache_page
from django.contrib import messages
from . import models
import json
import difflib

def ramo_best_match_from_text(request):
	if request.method == "GET":
		input_text = request.GET["data"]

		# Patch por si no ponen nada
		if input_text == "":
			messages.error(request, "Debe escribir algo en el buscador.")
			return redirect('/')
		ramos_data = [
			(ramo.nombre[:len(input_text)], len(ramo.nombre), ramo.pk) 
			for ramo in models.Ramo.objects.all()
		] + [
			(patch.nombre_alternativo[:len(input_text)], len(patch.nombre_alternativo), patch.ramo.pk)
			for patch in models.BuscadorPatch.objects.all()
		]
		matches = sorted(
			ramos_data,
			key=lambda x: difflib.SequenceMatcher(None, x[0], input_text).ratio(), 
			reverse=True
		)
		best_match = matches[0]

		# Ajustar best match si hay dos ramos con nombre similar
		if len(matches) > 1:
			best = 999 # MAGIC NUMBER
			best_index = 0
			for i in range(len(matches)):
				if matches[i][0] == best_match[0]:
					if matches[i][1] < best:
						best = matches[i][1]
						best_index = i
				else:
					break
			best_match = matches[best_index]


		#print(difflib.SequenceMatcher(None, best_match[0], input_text).ratio())
		if difflib.SequenceMatcher(None, best_match[0], input_text).ratio() < 0.5:
			messages.error(request, 'El ramo %s no fue encontrado. Por favor verifica tu búsqueda o prueba con otro ramo.' % input_text)
			return redirect('/')
		return redirect('ramo/%s' % str(best_match[2]))

# Obtenedor de ramos
def get_ramos(request):
	queryset = models.Ramo.objects.all()
	ramos = [ramo.nombre for ramo in queryset]
	response_data = {
		"ramos": ramos,
	}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

#View principal
class IndexSite(View):
	site_name = "Página principal"
	template = "core/index.html"
	def get(self, request, *args, **kwargs):
		context = {
			"site_name": self.site_name
		}
		return render(request, self.template, context=context)

#View de ramo
class Ramo(View):
	template = "core/ramo.html"
	def get(self, request, ramo_id, *args, **kwargs):
		"""
			Recibe un ramo_id, y retorna los datos del ramo junto con todos los archivos asociados a este.
			Retorna:
				"ramo": (object) Objeto del modelo ramo
				"tabla_evaluaciones": (lista) Lista de filas que contiene lo siguiente:
					[
						"tipo": (string) El tipo de evaluacion de la fila
						"evaluaciones": (lista) Una lista con los objetos de las evaluaciones de ese tipo.
					]
				"tabla_materiales": (lista) Lista de objetos del modelo material.
		"""
		ramo = get_object_or_404(models.Ramo, pk=ramo_id)
		evaluaciones = ramo.evaluaciones.all()
		materiales = ramo.materiales.all()

		tipos_evaluaciones = []
		tabla_evaluaciones = []

		# Llenado de datos de tabla_evaluaciones
		for evaluacion in evaluaciones:
			tipo = evaluacion.tipo.nombre
			if tipo not in tipos_evaluaciones:
				# Caso en que el tipo no existe en la tabla
				tipos_evaluaciones.append(tipo)
				tabla_evaluaciones.append(
					{
						"tipo": tipo,
						"evaluaciones": [evaluacion],
					}
				)
			else:
				# Caso en que el tipo si existe en la tabla
				for fila in tabla_evaluaciones:
					if fila["tipo"] == tipo:
						fila["evaluaciones"].append(evaluacion)

		# Llenado de datos de tabla_material


		# === Hacer cualquier ordenamiento aquí ===

		context = {
			"ramo": ramo,
			"tabla_evaluaciones": tabla_evaluaciones,
			"tabla_materiales": materiales,
			"site_name": ramo.nombre,
		}
		#print(context)
		return render(request, self.template, context=context)
