brain-games: # Запуск проекта
	uv run brain-games

build: # Сборка проекта
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl
