#coding: utf-8

import argparse

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

import httplib2
from oauth2client import client, file, tools

class Analytics:
	servico = None
	perfil = None

	def __init__(self, emailAutenticacao, arquivoChave):
		f = open(arquivoChave, 'rb')
		chave = f.read()
		f.close()

		escopo = ['https://www.googleapis.com/auth/analytics.readonly']

		#Conectando...
		credenciais = SignedJwtAssertionCredentials(emailAutenticacao, chave, scope=escopo)
		http = credenciais.authorize(httplib2.Http())
		self.servico = build('analytics', 'v3', http=http)
		
		contas = self.servico.management().accounts().list().execute()
		if contas.get('items'):
			conta = contas.get('items')[0].get('id')
			propriedades = self.servico.management().webproperties().list(accountId=conta).execute()
			if propriedades.get('items'):
				propriedade = propriedades.get('items')[0].get('id')
				perfis = self.servico.management().profiles().list(accountId=conta, webPropertyId=propriedade).execute()
				if perfis.get('items'):
					self.perfil = perfis.get('items')[0].get('id')
		return None
					
	def resultados(self, dataInicio, dataFim, metricas, dimensoes, ordem = None):
		perfilId = 'ga:' + self.perfil
		if ordem:
			dados = self.servico.data().ga().get(
				ids = perfilId,
				start_date = dataInicio,
				end_date = dataFim,
				metrics = metricas,
				dimensions = dimensoes,
				sort = ordem
			).execute()
		else:
			dados = self.servico.data().ga().get(
				ids = perfilId,
				start_date = dataInicio,
				end_date = dataFim,
				metrics = metricas,
				dimensions = dimensoes
			).execute()
		return dados.get('rows')
