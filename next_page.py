@router_resale.callback_query(F.data == 'next_show_more')
async def next_show_more(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()

    # Проверяем, инициализирован ли пул соединений
    if db_manager.pool is None:
        print("Пул соединений не инициализирован. Попытка создания.")
        await create_db_pool()
        if db_manager.pool is None:
            print("Ошибка: db_manager.pool не инициализирован.")
            return

    try:
        # Получаем текущий индекс из состояния
        current_index_data = await state.get_data()
        current_index = current_index_data.get('current_index', 0)

        async with db_manager.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                # Выполняем SQL-запрос SELECT для таблицы Краснодар
                sql = "SELECT * FROM Краснодар"
                await cursor.execute(sql)

                # Получаем строки из результата запроса
                results = await cursor.fetchall()

                # Проверяем, есть ли следующее объявление
                if current_index < len(results):
                    result = results[current_index]

                    # Обновляем состояние с новым индексом
                    await state.update_data(current_index=current_index + 1)

                    # Ваш код для вывода объявления...
                    id_anct = result[0]
                    await state.update_data(ids=id_anct)
                    print(f'Значение в переменной id_anct: {id_anct}')
                    data = await state.get_data()
                    print(f"Сохраненные айди показанных объявлений: {data.get('ids')}")
                    # Получаем значения из столбиков image_1, image_2, image_3, image_4, image_5, image_6
                    image_urls = [
                        result[3],
                        result[4],
                        result[5],
                        result[6],
                        result[7],
                        result[8]
                    ]

                    # Проверяем, есть ли хотя бы одна рабочая ссылка
                    if any(url and url.startswith('http') for url in image_urls):
                        # Формируем подпись с остальной информацией
                        caption = (f"Адрес: {result[9]}\n\n"
                                   f"Общая площадь:{result[11]}\n"
                                   f"Площадь кухни:{result[12]}\n"
                                   f"Количество комнат:{result[13]}\n"
                                   f"Балкон:{result[14]}\n"
                                   f"Санузел:{result[15]}\n"
                                   f"Тип ремонта:{result[16]}\n"
                                   f"Тип дома:{result[17]}\n"
                                   f"Тип лифта:{result[18]}\n"
                                   f"Договор:{result[21]}\n"
                                   f"Тип сделки:{result[22]}\n"
                                   f"Материнский капитал:{result[23]}\n\n"
                                   f"Описание:{result[25]}\n\n"
                                   f"Цена: {result[19]}\n"
                                   f"{result[20]}\n")

                        # Формируем медиагруппу
                        album_builder = MediaGroupBuilder(caption=caption)

                        # Добавляем непустые и рабочие изображения в медиагруппу
                        for url in image_urls:
                            if url and url.startswith('http'):
                                try:
                                    async with aiohttp.ClientSession() as session:
                                        async with session.head(url) as resp:
                                            # Проверяем, что ответ содержит изображение (Content-Type: image/*)
                                            if resp.content_type.startswith('image'):
                                                album_builder.add(type="photo", media=url)
                                except Exception as e:
                                    print(f"Ошибка при проверке типа изображения: {e}")

                        try:
                            # Отправляем медиагруппу
                            await bot.send_media_group(
                                chat_id=callback_query.from_user.id,
                                media=album_builder.build(),
                            )
                        except AiogramError as photo_error:
                            print(f"Ошибка при отправке медиагруппы: {photo_error}")
                            # Если возникла ошибка, отправляем только текстовое сообщение
                            await bot.send_message(callback_query.from_user.id, caption)
                    else:
                        # Если нет рабочих ссылок, отправляем только caption
                        caption = (f"Адрес: {result[9]}\n\n"
                                   f"Общая площадь:{result[11]}\n"
                                   f"Площадь кухни:{result[12]}\n"
                                   f"Количество комнат:{result[13]}\n"
                                   f"Балкон:{result[14]}\n"
                                   f"Санузел:{result[15]}\n"
                                   f"Тип ремонта:{result[16]}\n"
                                   f"Тип дома:{result[17]}\n"
                                   f"Тип лифта:{result[18]}\n"
                                   f"Договор:{result[21]}\n"
                                   f"Тип сделки:{result[22]}\n"
                                   f"Материнский капитал:{result[23]}\n\n"
                                   f"Описание:{result[25]}\n\n"
                                   f"Цена: {result[19]}\n"
                                   f"{result[20]}\n")
                        await bot.send_message(callback_query.from_user.id, caption)

                    # После отправки 10 строк отправим клавиатуру
                    await bot.send_message(callback_query.from_user.id, "Хотите увидеть еще?",
                                           reply_markup=kb.keyboard_menu)

                else:
                    await bot.send_message(callback_query.from_user.id, "Вы достигли конца списка объявлений.")
                    # Предложение начать заново или выполнить другие действия

    except Exception as e:
        # Обработка ошибок
        print(f"Ошибка: {e}")
        await bot.send_message(callback_query.from_user.id,
                               "Произошла ошибка при получении данных. Пожалуйста, попробуйте еще раз.")