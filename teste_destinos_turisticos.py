import unittest
from robo import *
import time
time.clock = time.time

class TesteDestinos(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_destinos(self):
        mensagens = ["destinos turisticos populares?", "poderia me fornecer os melhores destinos turisticos?", "lugares para viajar?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Eu recomendo os seguintes destinos: Paris, Tokyo, Rio de Janeiro, Barcelona, Dubai, Machu Picchu, Nova York, Santorini. Deseja saber mais sobre algum deles?", resposta.text
            )

    def testar_informacoes_sobre_paris(self): 
        mensagens = ["paris", "quero saber mais sobre paris", "eu escolho paris"]
        
        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A cidade luz, famosa pela Torre Eiffel, o Museu do Louvre e a Catedral de Notre-Dame. Um destino ideal para quem busca arte, historia e romance.", resposta.text
            )
    def testar_informacoes_sobre_tokyo(self): 
        mensagens = ["tokyo", "quero saber mais sobre tokyo", "eu escolho tokyo"]
        
        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Uma mistura unica de tradicao e modernidade, com templos historicos, arranha-ceus impressionantes e uma culinaria incrivel.", resposta.text
            )

    def testar_informacoes_sobre_rio_de_janeiro(self): 
        mensagens = ["rio de janeiro", "quero saber mais sobre rio de janeiro", "eu escolho rio de janeiro"]
        
        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Famosa pelas suas belas praias, como Copacabana e Ipanema, o Cristo Redentor e o Pao de Acucar. Um destino vibrante e cheio de cultura brasileira.", resposta.text
            )
    def testar_informacoes_sobre_barcelona(self): 
        mensagens = ["barcelona", "quero saber mais sobre barcelona", "eu escolho barcelona"]
        
        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Uma cidade com arquitetura deslumbrante, incluindo as obras de Gaudi, como a Sagrada Familia, e praias incriveis para relaxar.", resposta.text
            )

    def testar_informacoes_sobre_dubai(self): 
        mensagens = ["dubai", "quero saber mais sobre dubai", "eu escolho dubai"]
        
        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Conhecida por seus luxuosos shoppings, arranha-ceus imponentes e atividades de aventura no deserto. O lugar ideal para quem busca inovacao e luxo.", resposta.text
            )

    def testar_informacoes_sobre_machu_picchu(self): 
        mensagens = ["machu picchu", "quero saber mais sobre machu picchu", "eu escolho machu picchu"]
        
        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Uma das sete maravilhas do mundo, situada no Peru, e um destino imperdivel para os amantes de historia e aventura, com ruinas incas e vistas deslumbrantes.", resposta.text
            )
    def testar_informacoes_sobre_nova_york(self): 
        mensagens = ["nova york", "quero saber mais sobre nova york", "eu escolho nova york"]
        
        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A capital do mundo, conhecida por seus iconicos pontos turisticos como a Estatua da Liberdade, Times Square e Central Park.", resposta.text
            )

    def testar_informacoes_sobre_machu_picchu(self): 
        mensagens = ["santorini", "quero saber mais sobre santorini", "eu escolho santorini"]
        
        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Uma ilha grega famosa pelas suas casinhas brancas e igrejas de cupulas azuis, com vistas deslumbrantes e um por do sol incrivel.", resposta.text
            )

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteDestinos))

    executor = unittest.TextTestRunner()
    executor.run(testes)