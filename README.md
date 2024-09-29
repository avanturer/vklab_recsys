# VKLab Recsys - Рекомендательная система для ВКонтакте

## Описание задачи

В рамках данного проекта решается задача анализа постов из ленты «ВКонтакте» с целью предсказания конверсии из просмотра поста в различные активности: лайк, комментарий, скрытие поста, открытие поста отдельно или пересылка в личные сообщения.

Задача состоит в следующем:
- Провести предсказание вероятности конверсии поста (просмотр -> активность).
- Метрика: правдоподобие (логарифмическая потеря), а также возможность добавления дополнительных метрик.
- Использовать мультимодальные данные (текст и изображение), провести эксперименты с доступными моделями и собственными наработками.

## Основные задачи проекта:

1. **Подготовка данных:**
   - Скачивание и предварительная обработка датасета, содержащего текст поста, изображение (в сжатом формате) и метки активностей.
   - Приведение текста и изображений к формату, удобному для работы с моделями глубокого обучения.

2. **Анализ данных:**
   - Первичный разведывательный анализ (EDA), который включает изучение распределения активностей, просмотр частот слов и изображений, анализ корреляций.
   - Определение целевых переменных, с которыми будет проводиться работа (лайки, репосты, комментарии и т.д.).

3. **Моделирование:**
   - Построение мультимодальной модели на основе текстов и изображений.
   - Использование предобученных моделей для работы с текстом и изображениями (XLM-Roberta, CLIP).
   - Применение современных методов машинного обучения для предсказания вероятности активности (CatBoost для многотаргетных задач).
   - Эксперименты с различными моделями, метриками и подходами.

4. **Извлечение текстовых признаков:**
   - Применение предобученной модели `XLM-Roberta` для извлечения текстовых эмбеддингов, которые будут использоваться для предсказаний.
   - Очистка и нормализация текста, удаление лишних символов и эмодзи.

5. **Извлечение визуальных признаков:**
   - Использование модели `CLIP` для анализа изображений и присвоения категорий (мем, новость, изображение и т.д.).

6. **Выводы и рекомендации:**
   - Оценка производительности моделей.
   - Формирование рекомендаций для авторов постов о том, как улучшить вовлеченность пользователей, основываясь на анализе данных.

## Структура проекта

- `vk_project_main.ipynb`: Цельный ноутбук с итоговым результатом.
- `main_work_file.ipynb`: Файл с наработками (сейчас такой же как и vk_project_main.ipynb, только без описания).
- `future_extr_text.ipynb`: Наработки с извлечением текстовых признаков из постов ВКонтакте с использованием XLM-Roberta.
- `future_extr_photo.ipynb`: Наработки с извлечением визуальных признаков из изображений с помощью модели CLIP и др.
- `data/`: Тут будет лежать дата, необходимая для работы, после запуска одного из нотбуков или файла `data/download_data.py`.

## Установка и запуск проекта

### Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/avanturer/vklab_recsys.git
```

### Шаг 2: Установка зависимостей
```bash
pip install -r requirements.txt
```

### Шаг 3: Запуск ноутбуков

Используйте Jupyter Notebook для запуска всех файлов в следующем порядке:
1. `vk_project_main.ipynb` — подготовка данных и их первичная обработка.
2. `future_extr_text.ipynb` — извлечение текстовых признаков.
3. `future_extr_photo.ipynb` — извлечение визуальных признаков.
4. `main_work_file.ipynb` — обучение моделей и предсказание.

## Результаты

- Использование мультимодальной обработки данных (тексты + изображения) позволило значительно улучшить предсказания активности пользователей.
- Применение модели CatBoost для многотаргетного предсказания обеспечило высокую точность модели.
- На основе полученных результатов были даны рекомендации для улучшения вовлеченности пользователей.

## Рекомендации для авторов постов:
- Используйте мемы и эмоционально насыщенные изображения — это увеличивает вовлеченность пользователей.
- Лаконичные и цепляющие тексты, в которых использованы эмодзи, имеют тенденцию вызывать больше активностей.
- Посты, содержащие визуально привлекательные изображения, такие как фотографии природы или животных, также показывают более высокий уровень взаимодействия пользователей.

## Контакты
Для любых вопросов и предложений, свяжитесь со мной:

- **Email**: rodion.ork@yandex.ru
- **GitHub**: [avanturer](https://github.com/avanturer)
