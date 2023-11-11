

class Curso:
    def __init__(self, sigla, nome):
        self.__sigla = sigla 
        self.__nome = nome

    @property
    def Sigla(self):
        return self.__sigla

    @property
    def Nome(self):
        return self.__nome

class Estudante:
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    @property
    def NroMatric(self):
        return self.__nroMatric

    @property
    def Nome(self):
        return self.__nome

    @property
    def Curso(self):
        return self.__curso

class Equipe:
    def __init__(self, curso, listaEst):
        self.__curso = curso
        self.__litaEst = listaEst

    @property
    def Curso(self):
        return self.__curso

    @property
    def ListaEst(self):
        return self.__litaEst

    def AddEstudante(self, newStudent):
        self.__litaEst.append(newStudent)