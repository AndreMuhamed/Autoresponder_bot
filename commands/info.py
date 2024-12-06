async def handle_info(client, chat_id):
    await client.send_message(
        chat_id,
        "📢 **Андрей Мухамед** — креативный предприниматель и создатель инновационных проектов в сфере рекламы, технологий и цифрового контента. "
        "Он объединяет идеи и возможности, чтобы вдохновлять и создавать новое.\n\n"
        "**Основные команды для взаимодействия:**\n"
        "`!инфо` — Информацию о создателе и многом другом.\n"
        "`!тясицу` — Уникальный чат для поклонников создателя.\n"
        "`!реклама` — Узнайте о рекламе и ознакомьтесь с ценами.\n"
        "`!run` — Полный список доступных команд сервиса.\n"
        "`!донат` — Поддержите нас и помогите развивать проекты.\n"
        "`!подарок` — Специальные предложения для вас!\n"
        "`!чаво` — Популярные вопросы и ответы.\n"
        "`!боты` — Все боты разработаны командой Muhamed IT Solutions.\n\n"
        "🎯 Для получения более подробной информации, просто подождите, я скоро вам напишу!",
        file="Фото_материал/1 copy.png"  # Замените путь на файл вашей картинки
    )

