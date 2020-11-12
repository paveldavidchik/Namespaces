from typing import Union


class Namespace:
    """Класс", представляющий пространство имен"""

    def __init__(self, name: str, parent_namespace: object = None):
        self.__name = name  # Имя пространства имен
        self.__variables = []  # Переменные в данном пространстве имен
        self.__parent_namespace = parent_namespace  # Родительское пространство имен
        self.__child_namespaces = []  # Дочерние пространства имен

    def create_namespace(self, namespace: str, parent: str) -> bool:
        """
        Метод создает пространство имен
        :param namespace:                 # Имя создаваемого пространства имен
        :param parent:                    # Имя родительского пространства имен для создаваемого
        """
        if self.__name == parent:
            self.__child_namespaces.append(Namespace(namespace, self))
            return True
        elif len(self.__child_namespaces) == 0:
            return False
        else:
            for space in self.__child_namespaces:
                if space.create_namespace(namespace, parent):
                    return True

    def add_var(self, namespace: str, var: str) -> bool:
        """
        Метод добавляет переменную в пространство имен
        :param namespace:                 # Пространство имен, в которое необходимо добавить переменную
        :param var:                       # Переменная, которую необходимо добавить
        """
        if self.__name == namespace:
            self.__variables.append(var)
            return True
        elif len(self.__child_namespaces) == 0:
            return False
        else:
            for space in self.__child_namespaces:
                if space.add_var(namespace, var):
                    return True

    def get_namespace(self, namespace: str, var: str, is_find_namespace: bool = False) -> Union[str, None]:
        """
        Метод возвращает имя пространства имен, в котором содержится переменная
        :param namespace:                 # Пространство имен, с которого начинается поиск
        :param var:                       # Переменная, область видимости которой необходимо найти
        :param is_find_namespace          # Найдено ли место, откуда начнется поиск
        :return:                          # Возвращает имя области видимости или None, если переменная не найдена
        """
        if not is_find_namespace:
            if self.__name == namespace:
                is_find_namespace = True
            elif len(self.__child_namespaces) == 0:
                return None
            else:
                for space in self.__child_namespaces:
                    result = space.get_namespace(namespace, var)
                    if result is not None:
                        return result
        if var in self.__variables:
            return self.__name
        elif self.__parent_namespace is None:
            return None
        else:
            return self.__parent_namespace.get_namespace(namespace, var, is_find_namespace)
