class Estado:
    """
    Classe padrão de estados.
    """
    def __init__(self, nome, numero, proximo=None):
        self.nome = nome
        self.numero = numero
        self.proximo = proximo

    def __str__(self):
        return self.nome

    def executa(self, **kwargs):
        """
        Executa o estado atual de acordo com parametros passados e retorna o próximo.
        :param kwargs: dicionário de parametros.
        :return:
        """
        pass


class Maquina:
    """
    Máquina de Estados.
    """
    def __init__(self, estados, inicial):
        """
        Estados deve ser um dicionário, inicial deve ser o primeiro estado.
        :param estados: lista de estados.
        :param inicial: estado inicial.
        """
        self.estados = self.inicializa(estados)
        self.atual = self.estados[inicial]

    @staticmethod
    def inicializa(estados):
        """
        Recebe uma lista de Estados e converte para um dicionário com o nome e objeto instanciado da classe.
        :param estados: lista ou dicionário de dados.
        :return: dicionario dos estados e nome.
        """
        if isinstance(estados, dict):
            return estados
        iniciados = dict()
        for estado in estados:
            obj = estado()
            nome = obj.nome
            iniciados[nome] = obj
        return iniciados

    def executa(self, **kwargs):
        """
        Executa o estado atual e vai para o próximo.
        :return: None.
        """
        self.atual = self.atual.executa(kwargs)

    def percorre_todos(self):
        """
        Executa os estados na sequência em que foram passados.
        :return: None.
        """
        for estado in self.estados:
            self.atual = estado
            self.executa()

    def get_estado(self):
        return self.estados[self.atual]

    def get_proximo(self):
        proximo = self.atual.proximo
        if proximo:
            return self.estados[self.atual.proximo]
        return None

