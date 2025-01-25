import unittest
from robo import *
import time
time.clock = time.time

class TesteSaudacoes(unittest.TestCase):
    def setUp(self):
        self.robo = iniciar()

    def testar_oi_ola(self):
        saudacoes = ["oi", "oi, tudo bem?", "tudo bem?"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao)
            print(resposta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Ola, sou o assistente virtual de viagens! Como posso ajudar voce a planejar sua proxima viagem?", 
                resposta.text
            )

    def testar_bom_dia_boa_tarde_boa_noite(self):
        saudacoes = ["Bom dia", "Boa tarde", "Boa noite"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                saudacao + "! Que legal que voce esta pensando em viajar. Como posso te ajudar hoje?",
                resposta.text
            )


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)