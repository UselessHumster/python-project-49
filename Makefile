VERSION=0.1.1
PACKAGE=hexlet_code

create-venv: # Настройка окружения
	@pip install -r ./requirements.txt
	@uv venv --python=python3.10

build: # Сборка проекта
	@echo "Building package..."
	uv build

package-install:
	@echo "Installing package: $(PACKAGE)-$(VERSION)-py3-none-any.whl"
	@echo "To override installation please type: make package-install PACKAGE=name:string VERSION=version:string"
	@uv tool install dist/$(PACKAGE)-$(VERSION)-py3-none-any.whl

lint:
	uv run ruff check brain_games --fix

package-reinstall: build
	uv tool install --force dist/*.whl

brain-games: # Запуск проекта
	uv run brain-games

brain-calc: # Запуск игры Calc
	uv run brain-calc

brain-even: # Запуск игры Even
	uv run brain-even

brain-gcd: # Запуск игры GCD
	uv run brain-gcd

brain-prime: # Запуск игры Prime
	uv run brain-prime

brain-progression: # Запуск игры Progression
	uv run brain-progression

install: create-venv build package-install
