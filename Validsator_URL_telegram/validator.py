import string
from urllib.parse import urlparse

from Validsator_URL_telegram.utils import exceptions, utils

MAIN_HOST = 't.me'
POSSIBLE_HOSTS = ['t.me', 'telegram.me']
ALLOWED_CHARACTERS = string.digits + string.ascii_lowercase + string.ascii_uppercase


def validate_url(url: str) -> str:
    """
    Validate Telegram URL

    Parameters:
        url (``str``):
            Url to validate

    Returns:
        :obj:`str`: validated URL

    Raises:
        CantFindHostnameError:
            Can't find URL's hostname.

        HostNotInPossibleHostsError:
            URL's host not in possible hosts.

        TelegramInvalidHashError:
            URL's hash does not comply with Telegram rules.

    """
    if url.startswith('https://') or url.startswith('http://'):
        parsed_url = urlparse(url=url)
    elif url.startswith('@'):
        parsed_url = urlparse(url='https://t.me/' + url.strip('@'))
    else:
        parsed_url = urlparse(url=f'https://{url}')

    if parsed_url.hostname is None:
        raise exceptions.CantFindHostnameError(url=url)

    hostname = utils.get_hostname(hostname=parsed_url.hostname, hostnames=POSSIBLE_HOSTS)
    if hostname is None:
        raise exceptions.HostNotInPossibleHostsError(url=url, possible_hosts=POSSIBLE_HOSTS)

    hostname = parsed_url.hostname.replace(hostname, MAIN_HOST)
    url_hash = utils.validate_hash(
        url=url,
        url_hash=parsed_url.path,
        allowed_characters=set(ALLOWED_CHARACTERS),
    )

    if parsed_url.path.startswith('/+'):
        return f'https://{hostname}/joinchat/{url_hash}'
    return f'https://{hostname}/{url_hash}'