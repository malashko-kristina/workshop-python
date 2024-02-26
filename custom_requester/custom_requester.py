import logging
import os
from http import HTTPStatus
from enums.host import BASE_URL


class CustomRequester:
    #Словарь с базовыми заголовками
    base_headers = dict({"Content-Type": "application/json", "Accept": "application/json"})

    #Метод инициализации класса
    def __init__(self, session):
        self.session = session
        self.base_url = BASE_URL
        self.logger = logging.getLogger(__name__) #активируем логгер, для этого определим атрибут логгер в классе


    #Метод отправки запросов
    def send_request(self, method, endpoint, data=None, expected_status=HTTPStatus.OK, need_logging=True):
        """
        Враппер для запроса. позволяет прикручивать различную логику

        :param method: Метод запроса
        :param endpoint: Эндпоинт для склейки с BASE_URL в переменной "url"
        :param data: Тело запроса. По умолчанию пустое, чтобы пропускало NO_CONTENT ответы
        :param expected_status: Ожидаемый статус ответа. Если ожилается иной от SC_OK - передать в методе api-класса
        :param need_logging: Передача флага для логгирования. По умолчанию = True
        :return: Возвращает объект ответа
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, json=data)
        if need_logging:
            self.log_request_and_response(response)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}")
        return response


    #Метод обновления хедеров, он используется только для внутреннего использования в классе
    # **kwargs позволяет ф-ции принимать любое кол-во аргументов или не принимать вообще
    def _update_session_headers(self, **kwargs): #позволяет принимать любое количество аргументов, в том чсиле не принимать их вообще
        self.headers = self.base_headers.copy()
        self.headers.update(kwargs) #обновляется значение словоря
        self.session.headers.update(self.headers) #обновляет заголовки сессии,копирует базовые заголовки с помощью представленных аргументов kwargs, затем обновленные заголовки применяются к сесссии

   #Добавление логирования
    def log_request_and_response(self, response):

        """
        Логгирование запросов и ответов. Настройки логгирования описаны в pytest.ini Преобразует вывод в curl-like
        (-H хедеры), (-d тело)

        :param response: Объект response получаемый из метода "send_request"

        """
        try:
            request = response.request #объект запроса, связанный с ответом
            GREEN = '\033[32m'
            RED = '\033[31m'
            RESET = '\033[0m' #сброс цвета к стандартному
            headers = "\\\n".join([f"-H '{headers}: {value}'" for headers, value in request.headers.items()])
            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}" #Добавим в логи вывод названия теста

    #Отформатируем тело запроса
            body = ""
            if hasattr(request, 'body') and request.body is not None:
                if isinstance(request.body, bytes):
                    body = request.body.decode('utf-8') #???
            body = f"-d '{body}' \n" if body != '{}' else ''

    #Отформатируем и выведем информацию о запросе в логи
    #Сформированная строка передается в метод info объекта logger, который записывает эту информацию в лог
            self.logger.info(
                  f"{GREEN} {full_test_name}{RESET}\n"
                  f"curl -X {request.method} '{request.url}' \\\n"
                  f"{headers} \\\n"
                  f"{body}"
                  )

    #Ответ логируем только при неуспешном запросе (красный свет), для этого добавляем проверку статус кода
            response_status = response.status_code #извлечение HTTP статус-кода ответа
            is_success = response.ok #проверяет, находится ли статус код в диапозоне 200-299
            response_data = response.text #возвращает тело запроса в виде строки

            if not is_success:
                self.logger.info(f"\tRESPONSE:"
                         f"\nSTATUS_CODE: {RED}{response_status}{RESET}"
                         f"\nDATA: {RED}{response_data}{RESET}")


        except Exception as e:
            self.logger.info(f"\nLogging went wrong: {type(e)} - {e}")







