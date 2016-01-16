# googleanalytics-python-framework
Pequeno framework para acessar dados do Google Analytics via Python.

Criado por Ricardo Lima Mazzolli usando códigos do Google.

##Documentação:

Antes de utilizar, é necessário ativar a API do Analytics para a sua conta, criar uma chave de acesso, configurá-lo com as permissões desejadas dentro do seu Analytics e instalar a aplicação de cliente da API do Google Analytics. Para isso, siga as etapas 1 e 2 desse passo-a-passo:
https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py

Observação: As etapas 3 e 4 do passo-a-passo informado são interessantes como introdução para fins didáticos caso haja interesse mas não são necessárias para a utilização deste framework.

Depois de configurada a sua conta, para facilitar, certifique-se que o arquivo P12 esteja localizado na mesma pasta da aplicação que está desenvolvendo. Este framework não é compatível com credenciais no formato JSON.

##Exemplo de Utilização do Framework:

'''python
from googleAnalytics import Analytics

conexao = Analytics('email_de_acesso', 'localizacao/do/arquivo/P12')
dados = conexao.resultados(
	dataInicio = '2015-01-01',
	dataFim = '2015-12-31',
	metricas = 'ga:sessions',
	dimensoes = 'ga:city',
	ordem = '-ga:sessions, ga:region'
)
'''

##Listas de Dimensões e Métricas possíveis:
https://developers.google.com/analytics/devguides/reporting/core/dimsmets
