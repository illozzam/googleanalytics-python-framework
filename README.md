# googleanalytics-python-framework
<a href="#ingles">English</a><br/>
Pequeno framework para acessar dados do Google Analytics via Python.

Criado por Ricardo Lima Mazzolli usando códigos do Google.

## Documentação

Antes de utilizar, é necessário ativar a API do Analytics para a sua conta, criar uma chave de acesso, configurá-lo com as permissões desejadas dentro do seu Analytics e instalar a aplicação de cliente da API do Google Analytics. Para isso, siga as etapas 1 e 2 desse passo-a-passo:
https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py

Observação: As etapas 3 e 4 do passo-a-passo informado são interessantes como introdução para fins didáticos caso haja interesse mas não são necessárias para a utilização deste framework.

Depois de configurada a sua conta, para facilitar, certifique-se que o arquivo P12 esteja localizado na mesma pasta da aplicação que está desenvolvendo. Este framework não é compatível com credenciais no formato JSON.

## Exemplo de Utilização do Framework:

```python
from googleAnalytics import Analytics

conexao = Analytics('email_de_acesso', 'localizacao/do/arquivo/P12')
dados = conexao.resultados(
	dataInicio = '2015-01-01',
	dataFim = '2015-12-31',
	metricas = 'ga:sessions',
	dimensoes = 'ga:city',
  ordem = '-ga:sessions, ga:region'
)
```

## Listas de Dimensões e Métricas possíveis:
https://developers.google.com/analytics/devguides/reporting/core/dimsmets

<a name="ingles"></a>
#googleanalytics-python-framework
<a href="#">Original</a>

Small framework to access Google Analytics data via Python.

Created by Ricardo Lima Mazzolli using Google code .

## Documentation

Before using , you must enable the Analytics API to your account , create an access key, set it to the desired permissions within your Analytics and install the client application on the Google Analytics API. To do this , follow steps 1 and 2 of this step -by-step:
https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py

NOTE: Steps 3 and 4 of informed step-by-step are interesting as an introduction for teaching purposes if there is interest but are not necessary for using this framework.

Once you set your account, to make it easier, make sure that the P12 file is located in the same application folder that is developing. This framework is not compatible with credentials in JSON format.

## Usage Example:

```python
from googleAnalytics import Analytics

connection = Analytics('access_email', 'location/of/P12/file')
data = connection.results(
	start_date = '2015-01-01',
	end_date = '2015-12-31',
	metrics = 'ga:sessions',
	dimensions = 'ga:city',
	sort_by = '-ga:sessions, ga:region'
)
```

## Possible Dimensions and metrics list:
https://developers.google.com/analytics/devguides/reporting/core/dimsmets
