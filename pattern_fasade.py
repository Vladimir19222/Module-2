import logging
import requests


class Facade:
    def __init__(self) -> None:
        self.log_ging = log_ging
        self.get_data = get_data
        self.post_data = post_data
        self.put_data = put_data
        self.delete_data = delete_data

    def start_project(self):
        self.log_ging()
        print()
        print('запрос GET')
        self.get_data(url, params)
        print()
        print('запрос POST')
        self.post_data(url, new_product)
        print()
        print('запрос put')
        self.put_data(url + params1, updated_product)
        print()
        print('запрос delete')
        self.delete_data(url, arg)


def log_ging() -> None:
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")


def get_data(link, params=''):
    response = requests.get(link, params)
    if response.status_code == 200:
        logging.info("An INFO get_data  - успешно")
        users = response.json()
        for user in users:
            print(user)
        with open("get.json()", "w") as file:
            for user in users:
                file.write(str(user))
                file.write('\n')
    else:
        print(f"Ошибка - get: {response.status_code}")
        logging.exception(f"Произошла ошибка запроса GET, код ошибки: {response.status_code}")


def post_data(link, new_product):
    response = requests.post(link, json=new_product)
    if response.status_code == 201:
        logging.info("An INFO post_data - успешно")
        users = response.json()
        print(users)
        with open("post.json()", "w") as file:
            for user in [users]:
                file.write(str(user))
    else:
        print(f"Ошибка - post: {response.status_code}")
        logging.exception(f"Произошла ошибка добавления новых данных, код ошибки: {response.status_code}")


def put_data(link, new_date):
    response = requests.put(link, new_date)
    if response.status_code == 200:
        logging.info("An INFO put_data  - успешно")
        users = response.json()
        print(users)
        with open("put.json()", "w") as file:
            for user in [users]:
                file.write(str(user))
    else:
        print(f"Ошибка - put: {response.status_code}")
        logging.exception(f"Произошла ошибка обновления, код ошибки: {response.status_code}")


def delete_data(link, params=''):
    link = link + '/' + str(params)
    response = requests.delete(link)
    if response.status_code == 200:
        logging.info("An INFO delete_data")
        print(f'код = {response.status_code} - успешно, позиция {params} удалена')
    else:
        print(f"Ошибка - delete: {response.status_code}")
        logging.exception(f"Произошла ошибка удаления, код ошибки: {response.status_code}")


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/"
    params = '&id=2&id=5&id=9'
    new_product = {"userId": 1, "id": 201, "title": "delectus aut autem", "completed": False}
    params1 = '/8'
    updated_product = {"userId": 7, "id": 141, "title": "Everything will be fine", "completed": True}
    arg = 33

    facade = Facade()
    facade.start_project()
