### Инструкция по созданию и работе со стартовым проектом на Python с использованием Poetry

#### 1. Установка Poetry

Poetry — это менеджер зависимостей и инструмент для создания виртуальных окружений. Для начала работы с Poetry его необходимо установить:

##### 1.1 Установка Poetry на Linux/macOS:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

##### 1.2 Установка Poetry на Windows:

Для Windows используйте PowerShell:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

##### 1.3 Проверка установки:

После установки убедитесь, что Poetry был установлен корректно, проверив его версию:

```bash
poetry --version
```

#### 2. Создание нового проекта

Для создания нового проекта на Python с использованием Poetry выполните следующие шаги:

##### 2.1 Инициализация проекта:

Перейдите в каталог, где хотите создать проект, и выполните команду:

```bash
poetry new my_project
```

Эта команда создаст новую директорию `my_project`, содержащую базовую структуру Python-проекта:

```
my_project/
│
├── my_project/         # Папка с исходным кодом
│   └── __init__.py     # Маркер пакета Python
├── tests/              # Папка с тестами
│   └── __init__.py
├── pyproject.toml      # Файл конфигурации проекта
├── README.rst          # Описание проекта
└── .gitignore          # Игнорируемые файлы для Git
```

##### 2.2 Инициализация существующего проекта:

Если у вас уже есть существующий проект, вы можете инициализировать Poetry в нём:

```bash
cd existing_project
poetry init
```

Poetry предложит заполнить базовые параметры проекта, такие как имя, версия, описание, автор и т.д.

#### 3. Работа с зависимостями

Poetry позволяет управлять зависимостями проекта и автоматически разрешает их версии.

##### 3.1 Установка зависимостей:

Для добавления библиотеки выполните:

```bash
poetry add <название_библиотеки>
```

Например, для установки библиотеки `requests`:

```bash
poetry add requests
```

Poetry автоматически добавит зависимость в файл `pyproject.toml` и установит её в виртуальное окружение проекта.

##### 3.2 Установка зависимостей для разработки:

Вы можете добавить библиотеки, необходимые только для разработки (например, тестовые фреймворки):

```bash
poetry add pytest --dev
```

##### 3.3 Установка всех зависимостей:

Для установки всех зависимостей, указанных в `pyproject.toml`, выполните:

```bash
poetry install
```

#### 4. Управление виртуальным окружением

Poetry автоматически создает и управляет виртуальным окружением для каждого проекта.

##### 4.1 Активация виртуального окружения:

Чтобы активировать виртуальное окружение для текущего проекта:

```bash
poetry shell
```

##### 4.2 Выполнение команд без активации окружения:

Если не хотите активировать виртуальное окружение, но необходимо выполнить команду, можно использовать:

```bash
poetry run <команда>
```

Например:

```bash
poetry run python my_project/main.py
```

#### 5. Работа с файлами проекта

##### 5.1 Файл `pyproject.toml`:

Это основной файл конфигурации проекта, в котором описаны зависимости, скрипты, метаданные проекта. Пример его содержимого:

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "My Python project"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.25.1"

[tool.poetry.dev-dependencies]
pytest = "^6.2.4"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

##### 5.2 Запуск приложения:

Чтобы запустить приложение, можно использовать Python через Poetry:

```bash
poetry run python my_project/main.py
```

#### 6. Тестирование проекта

Poetry поддерживает интеграцию с тестовыми фреймворками, такими как `pytest`.

##### 6.1 Добавление pytest:

Установите pytest как зависимость для разработки:

```bash
poetry add pytest --dev
```

##### 6.2 Написание тестов:

Тесты размещаются в папке `tests/`. Пример теста:

```python
# tests/test_sample.py
def test_example():
    assert 2 + 2 == 4
```

##### 6.3 Запуск тестов:

Для запуска тестов выполните:

```bash
poetry run pytest
```

##### 6.4 Устранение проблем с отсутствующими тестами:

Если при выполнении команды `pytest` выводится сообщение: `no tests ran in 0.04s`, это может быть вызвано несколькими причинами:

1. **Неправильные имена файлов или функций тестов:**

   - Убедитесь, что имена файлов тестов начинаются с `test_` или заканчиваются на `_test.py`.
   - Функции тестов должны начинаться с `test_`. Пример:

   ```python
   # tests/test_sample.py
   def test_example():
       assert 2 + 2 == 4
   ```

2. **Тесты в неправильной директории:**

   - `pytest` ищет тесты в папке `tests/` по умолчанию. Убедитесь, что тесты находятся в правильной директории. Если они находятся в другой папке, используйте:

   ```bash
   poetry run pytest path/to/tests/
   ```

3. **Отсутствие тестов:**

   - Проверьте, что в каждом файле есть хотя бы одна тестовая функция, начинающаяся с `test_`.

4. **Запуск конкретного файла:**
   - Если проблема остается, можно явно указать файл:
   ```bash
   poetry run pytest tests/test_sample.py
   ```

#### 7. Решение проблемы с сообщением "Command Executed now, took ..."

Если при выполнении команды `poetry run main` появляется сообщение с красным маркером и текстом `Command Executed now, took ...`, это может означать следующее:

##### 7.1 **Ошибка в вызове файла**:

Проверьте, правильно ли указан путь к файлу. Вместо `poetry run main` используйте полную команду:

```bash
poetry run python my_project/main.py
```

##### 7.2 **Проблемы с зависимостями**:

Переустановите зависимости для проекта:

```bash
poetry install
```

##### 7.3 **Проблемы с виртуальным окружением**:

Попробуйте пересоздать виртуальное окружение:

```bash
poetry env remove <python_version>
poetry install
```

Замените `<python_version>` на используемую версию Python (например, `python3.8`).

##### 7.4 **Обновление Poetry**:

Проверьте, что используете последнюю версию Poetry:

```bash
poetry self update
```

#### 8. Управление версиями и публикация

##### 8.1 Изменение версии:

Для изменения версии проекта вручную отредактируйте поле `version` в файле `pyproject.toml` или используйте:

```bash
poetry version <новая_версия>
```

##### 8.2 Публикация пакета:

Poetry позволяет публиковать пакеты на PyPI. Для этого выполните:

```bash
poetry publish --build
```

#### 9. Удаление зависимостей

##### 9.1 Удаление библиотеки:

Чтобы удалить библиотеку, используйте команду:

```bash
poetry remove <название_библиотеки>
```

#### 10. Заключение

Poetry — это мощный инструмент для управления проектами Python, который упрощает работу с зависимостями, виртуальными окружениями и публикацией пакетов. Он обеспечивает стандартизацию процессов разработки и облегчает работу как для индивидуальных разработчиков, так и для команд.