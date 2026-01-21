"""Classe que gerencia a padronização de saidas coloridas de prints."""

from utils.imports import *

class ColorManager:
    """Classe para gerenciar a coloração de textos."""
    @staticmethod
    def success(text: str) -> None:
        """Retorna o texto colorido de verde."""
        print(f"{Fore.GREEN}{text}{Fore.RESET}")

    @staticmethod
    def error(text: str) -> None:
        """Retorna o texto colorido de vermelho."""
        print(f"{Fore.RED}{text}{Fore.RESET}")

    @staticmethod
    def warning(text: str) -> None:
        """Retorna o texto colorido de amarelo."""
        print(f"{Fore.YELLOW}{text}{Fore.RESET}")

    @staticmethod
    def info(text: str) -> None:
        """Retorna o texto colorido de azul."""
        # return print(f"{Fore.CYAN}{text}{Fore.RESET}")
        print(f"{Fore.CYAN}{text}{Fore.RESET}")

    @staticmethod
    def custom(text: str, color: str) -> None:
        """Retorna o texto colorido com uma cor personalizada."""
        color_map = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'blue': Fore.BLUE,
            'cyan': Fore.CYAN,
            'magenta': Fore.MAGENTA
        }
        print(f"{color_map.get(color, Fore.WHITE)}{text}{Fore.RESET}")