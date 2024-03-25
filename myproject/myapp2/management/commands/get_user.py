from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    heplp = 'Get user by id.'

    def add_arguments(self, parser):
        """
        Этот метод имеет параметр parser.
        Этот метод позволит передавать в командной строке вместе с вызовом модуля - передавать
        ещё и аргумент. В нашем случае, мы указали что этот аргумент будет хранится под именем 'id'
        :param parser:
        :return:
        """
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        """
        Здесь мы из словаря будем вытаскивать наш аргумент из командной строки, который мы
        предварительно сохранили под именем 'id'. Сохраняем это значение в переменной id.
        Далее мы создаем переменную user, где у модели User обращаемся к записям и указываем, что
        хотим получить запись, у которой значение в столбце id совпадает с аргументом переданным
        в командной строке. Однако у метода get есть недостаток - он вернет ошибку, если ввести в
        командной строке число, превышающее значение id в БД. Чтобы обойти это, лучше использовать
        метод filter вместо get.
        :param args:
        :param kwargs:
        :return:
        """
        pk = kwargs['pk'] # лучше не использовать переменную с именем id, т.к. это зарезервированное
        # имя в пайтон. Поэтому использем имя 'pk'
        #user = User.objects.get(id=id)
        user = User.objects.filter(pk=pk).first()
        '''
        Запоминаем в БД sql - id, в django pk, это одна и та же сущность.
        Теперь команда вернет None, если такого pk в БД нет. Исключения не будет.
        '''
        self.stdout.write(f'User: {user}')