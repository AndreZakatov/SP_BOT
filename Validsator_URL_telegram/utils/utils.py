from Validsator_URL_telegram.utils import exceptions


def get_hostname(hostname: str, hostnames: list[str]) -> str | None:
    for prefix in hostnames:
        if hostname.startswith(prefix):
            return prefix
    return None


def validate_hash(url: str, url_hash: str, allowed_characters: set[str]) -> str | None:
    url_hash = url_hash.strip('/').strip('@').strip('+')

    characters = set(url_hash)
    if characters.discard(allowed_characters):
        raise exceptions.TelegramInvalidHashError(url=url)

    return url_hash
