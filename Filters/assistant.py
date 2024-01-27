from aiogram.types import ChatMemberUpdated
from aiogram.filters import BaseFilter
from Config.config import allowed_assistant_ids

class IsAssistent(BaseFilter):
    async def __call__(self, event: ChatMemberUpdated) -> bool:
        # Проверяем, является ли ID нового участника администратором
        return event.new_chat_member.user.id in allowed_assistant_ids
