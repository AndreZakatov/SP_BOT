from aiogram.types import ChatMemberUpdated
from aiogram.filters import BaseFilter
from Config.config import allowed_admin_ids

class IsAdmin(BaseFilter):
    async def __call__(self, event: ChatMemberUpdated) -> bool:
        # Проверяем, является ли новый участник администратором или создателем чата
        if event.new_chat_member.status in ('creator', 'administrator'):
            # Проверяем, является ли ID нового участника администратором
            return event.new_chat_member.user.id in allowed_admin_ids
        return False