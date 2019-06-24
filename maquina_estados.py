class Estado:
    """
    Classe padrão de estados.
    """
    def __init__(self, nome, numero, proximo=None):
        """
        Inicialização da classe estado.
        :param nome: String contendo o nome deste estado.
        :param numero: Integer contendo o número deste estado.
        :param proximo: String nomeando o próximo estado.
        """
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

    def get_estado(self):
        return self.atual

    def set_estado(self, estado):
        self.atual = self.estados[estado]

    def get_proximo(self):
        proximo = self.atual.proximo
        if proximo:
            if proximo in self.estados:  # Se não existe o estado retorna nada. TODO: Subir erro?
                return self.estados[self.atual.proximo]
            else:
                print('Próximo estado: {}, não existe!!!'.format(proximo))
                return None
        return None

    def to_proximo(self):
        self.atual = self.get_proximo()

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
        self.atual.executa(**kwargs)

    def ciclo(self, **kwargs):
        """
        Percorre cada um dos estados, executa eles, até que o próximo seja None.
        :param kwargs:
        :return:
        """
        while self.atual is not None:
            self.executa(**kwargs)
            self.to_proximo()



