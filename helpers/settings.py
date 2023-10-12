# (c) @AbirHasan2005

import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, MessageNotModified

from helpers.database.access_db import db


async def ShowSettings(event: Message, user_id: int):
    """
    Show Custom Settings Panel with Updated Data.

    :param event: Pass Editable Message object.
    :param user_id: Pass User ID to Get Data of that User.
    """

    service_on = await db.get_service_on(user_id)
    footer_ = await db.get_footer_text(user_id)
    # Bug >>>
    also_footer2text = await db.get_add_text_footer(user_id)
    also_footer2photo = await db.get_add_photo_footer(user_id)
    channel_id = await db.get_channel_id(user_id)
    markup = [
        [InlineKeyboardButton(f"الخدمة {'مفعلة' if (service_on is True) else 'معطلة'} ✅", callback_data="triggerService")],
        [InlineKeyboardButton("ضبط حقوق القناه ", callback_data="setFooterText")],
        [InlineKeyboardButton(f"وضع الحقوق ع الصور  {'مفعل' if (also_footer2text is True) else 'معطل'} ✅", callback_data="setAlsoFooter2Text")],
        [InlineKeyboardButton(f"وضع الحقوق على النصوص {'مفعل' if (also_footer2photo is True) else 'معطل'} ✅", callback_data="setAlsoFooter2Photo")]
    ]
    # Bug <<<
    if footer_ is not None:
        markup.append([InlineKeyboardButton("حذف حقوق القناة", callback_data="rmFooterText"),
                       InlineKeyboardButton("عرض الحقوق الحاليه", callback_data="showFooterText")])
    if channel_id is None:
        markup.append([InlineKeyboardButton("ضبط ايدي القناة", callback_data="setChannelID")])
    else:
        markup.append([InlineKeyboardButton("تغيير ايدي القناة", callback_data="setChannelID")])
    try:
        await event.edit(
            text="من هنا تستطيع تغيير الاعدادات:",
            reply_markup=InlineKeyboardMarkup(markup)
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await ShowSettings(event, user_id)
    except MessageNotModified:
        pass
