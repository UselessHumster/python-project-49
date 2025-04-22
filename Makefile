brain-games: # Запуск проекта
	uv run brain-games

build: # Сборка проекта
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games