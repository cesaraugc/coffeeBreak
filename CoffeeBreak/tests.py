import unittest
import datetime
from CoffeeBreak.models import Usuario

# Create your tests here.
class UsuarioTestCase(unittest.TestCase):
    def setUp(self):
        self.joao = Usuario.objects.create(nome_usuario= "joao", nome="joao1", senha="12345", email="joao@gmail.com")

    def testSpeaking(self):
        self.assertEquals(self.joao.nome_usuario, "joao")
        self.assertEquals(self.joao.nome, "joao1")
        self.assertEquals(self.joao.senha, "12345")
        self.assertEquals(self.joao.email, "joao@gmail.com")