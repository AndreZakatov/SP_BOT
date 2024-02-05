class BaseValidationError(Exception):
    pass


class HostNotInPossibleHostsError(BaseValidationError):
    def __init__(self, url: str, possible_hosts: list[str]):
        self.url = url
        self.possible_hosts = possible_hosts

    def __str__(self):
        return f"URL's ({self.url}) host not in possible hosts: {', '.join(self._get_possible_hosts_in_quotes())}"

    def _get_possible_hosts_in_quotes(self) -> list[str]:
        return [f'"{prefix}"' for prefix in self.possible_hosts]


class CantFindHostnameError(BaseValidationError):
    def __init__(self, url: str):
        self.url = url

    def __str__(self):
        return f"Can't find hostname for URL {self.url}"


class BaseTelegramValidationError(BaseValidationError):
    pass


class TelegramInvalidHashError(BaseTelegramValidationError):
    def __init__(self, url: str):
        self.url = url

    def __str__(self):
        return f'URL {self.url} has invalid hash'