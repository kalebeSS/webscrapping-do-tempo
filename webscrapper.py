from bs4 import BeautifulSoup
import requests

class previsaoTempo:

	def __init__(self) -> None:
		#configuração inicial
		self.link = 'https://g1.globo.com/previsao-do-tempo/ce/fortaleza.ghtml'
		self.response = requests.get(self.link)
		self.soup = BeautifulSoup(self.response.text, 'html.parser')

	def inicia_projeto(self):
		#função que inicia o projeto dentro da class previsaoTempo
		self.temperatura()
		self.condicao_tempo()
		self.previsao_tres_dias()
		self.texto_enviar()

	def temperatura(self):
		#captura do site as temperaturas maximas e minimas
		temp_max = self.soup.find('div', class_  = 'forecast-today__temperature forecast-today__temperature--max').get_text()
		temp_min = self.soup.find('div', class_  = 'forecast-today__temperature forecast-today__temperature--min').get_text()

		return temp_max, temp_min

	def condicao_tempo(self):
		#retorna a condição do tempo atual
		condicao = self.soup.find('p', class_ = 'forecast-header__summary').get_text()
		
		return condicao
	
	def previsao_tres_dias(self):
		#cria uma lista vazia para adicionar os dados.
		prev = []
		previsoes = self.soup.find_all('div', class_ = 'forecast-table__item forecast-next-days__item')
		for previsao in previsoes:
			prev.append(previsao.get_text())
		
		return prev
	
	def texto_enviar(self):
		temp_max, temp_min = self.temperatura()
		condicao_tempo = self.condicao_tempo()
		previsao_dias = self.previsao_tres_dias()

		print(f'''temperatura em fortaleza é de máxima de {temp_max} e mínima de {temp_min}\n a condição do tempo é de {condicao_tempo} \nE a previsão dos próximos dias são\n{previsao_dias[0]},\n{previsao_dias[1]}e \n{previsao_dias[2]}''')
	
previsao = previsaoTempo()
previsao.inicia_projeto()
