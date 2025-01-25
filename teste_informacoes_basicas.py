import unittest
from robo import *
import time
time.clock = time.time

class TesteInformacoesBasicas(unittest.TestCase):
    def setUp(self):
        self.robo = iniciar()

    def testar_documentos_necessarios(self):
        mensagens = ["quais documentos são exigidos para viagens internacionais?", "quais são os requisitos para viajar para o exterior?", "viagem para o exterior?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Para viagens internacionais, os principais documentos necessarios sao: 1. Passaporte valido (verifique a validade minima exigida para o seu destino). 2. Visto, se necessario, de acordo com o pais de destino. 3. Comprovante de vacinacao (dependendo do destino). 4. Seguro de viagem (recomendado para seguranca e assistencia durante a viagem). 5. Documentos relacionados a viagem, como bilhetes de aviao e reservas de hoteis. Lembre-se de verificar as exigencias especificas do pais para o qual voce esta viajando.", resposta.text)

    def testar_informacoes_de_seguranca(self):
        mensagens = ["poderia me fornecer dicas de segurança?", "dicas de segurança?", "Quais cuidados de segurança devo ter?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Aqui estao algumas dicas para garantir uma viagem segura: 1. Mantenha seus documentos e objetos de valor, como dinheiro e cartoes, em um local seguro, como uma bolsa ou pochete anti-roubo. 2. Tenha uma copia de todos os seus documentos importantes, como passaporte e bilhetes de viagem, em um lugar separado. 3. Evite exibir itens de valor, como cameras e joias, em locais publicos. 4. Fique atento aos seus arredores, especialmente em areas turisticas. 5. Mantenha um contato regular com familiares ou amigos para informar sobre sua localizacao e seguranca. 6. Conheca as leis e costumes locais para evitar mal-entendidos.", resposta.text)
            
    def testar_cambio(self): 
        mensagens = ["como funciona o câmbio?", "Como acontece a conversão de moedas?", "Como posso entender o câmbio de moedas?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("O cambio e o processo de troca de uma moeda por outra, utilizado quando voce viaja para outro pais. Aqui estao alguns pontos importantes: 1. Taxa de cambio: A taxa de cambio e o valor pelo qual uma moeda e trocada por outra. Isso pode variar dependendo da oferta e demanda. 2. Onde trocar: Voce pode trocar dinheiro em casas de cambio, bancos ou ate no aeroporto, embora as taxas no aeroporto geralmente nao sejam as mais favoraveis. 3. Cartoes de credito e debito: Muitos cartoes internacionais permitem fazer compras em outros paises com a conversao automatica de moeda. No entanto, e importante verificar as taxas do seu banco. 4. Dica: Troque dinheiro com antecedencia, especialmente se for viajar para destinos onde o cambio nao seja facil de realizar. Compare as taxas de cambio para garantir uma boa conversao.", resposta.text)


    def testar_como_fazer_a_troca_de_dinheiro(self): 
        mensagens = ["Como faço para trocar dinheiro antes de viajar? ", "Onde posso fazer câmbio antes da minha viagem?", "Qual é o melhor lugar para trocar dinheiro antes de viajar"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Voce pode trocar dinheiro em casas de cambio", resposta.text)

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoesBasicas))

    executor = unittest.TextTestRunner()
    executor.run(testes)
