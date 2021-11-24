import requests

from src.error import BaseError, RequestError


def request_all() -> None:
    try:
        submarino_response = request_submarino()

        if not submarino_response.ok:
            raise BaseError("O Submarino não deu bom galera")

        print("O Submarino ta legal")
        
        americanas_response = request_americanas()
        
        if not americanas_response.ok:
            raise BaseError("A Americanas não deu bom galera")

        print("A Americanas ta legal")

    except RequestError as ex:
        print("Putz rapeize, deu ruim")


def request_submarino() -> requests.Response:
    return requests.get(url=get_submarino_url())


def request_americanas() -> requests.Response:
    return requests.get(url=get_americanas_url())


def get_submarino_url() -> str:
    return "https://www.submarino.com.br"


def get_americanas_url() -> str:
    return "https://www.americanas.com"
