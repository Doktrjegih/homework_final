SRC_DIR ?= ./autotests
PYTHON_PATH != which python3
PYTHON_DIR != dirname $(PYTHON_PATH)
CONFIG_FILE ?= setup.cfg

lint:
	$(PYTHON_DIR)/black --skip-string-normalization --check -C -l 120 $(SRC_DIR)
	$(PYTHON_DIR)/flake8 --jobs 4 --statistics --show-source $(SRC_DIR)
	$(PYTHON_DIR)/pylint --jobs 4 --rcfile=$(CONFIG_FILE) $(SRC_DIR)
	$(PYTHON_DIR)/mypy --cache-dir=/dev/null --config-file=$(CONFIG_FILE) $(SRC_DIR)

format:
	$(PYTHON_DIR)/isort $(SRC_DIR)
	$(PYTHON_DIR)/black --skip-string-normalization -C -l 120 $(SRC_DIR)
	$(PYTHON_DIR)/autoflake --recursive --in-place --remove-all-unused-imports --ignore-init-module-imports $(SRC_DIR)
	$(PYTHON_DIR)/unify --in-place --recursive --quote "'" $(SRC_DIR)