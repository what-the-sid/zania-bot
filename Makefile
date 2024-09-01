# Define variables
PYTHON_ENV = .venv
ZANIA := $(shell pwd)/zania

# Targets
.PHONY: local production install-libs create-venv create-symlink clean

SHELL_TYPE := $(shell echo $$SHELL)
SHELL_CONFIG := $(shell \
	    if [ -f "$$HOME/.zshrc" ] && [[ "$$SHELL_TYPE" == */zsh ]]; then \
	        echo "$$HOME/.zshrc"; \
	    elif [ -f "$$HOME/.bashrc" ] && [[ "$$SHELL_TYPE" == */bash ]]; then \
	        echo "$$HOME/.bashrc"; \
	    elif [ -f "$$HOME/.profile" ]; then \
	        echo "$$HOME/.profile"; \
	    else \
	        echo "$$HOME/.zshrc"; \
	    fi)

# Default target
local: install-libs set-alias
production: install-libs set-alias

# Create a Python virtual environment
create-venv:
	@if [ ! -d "$(PYTHON_ENV)" ]; then \
		echo "Creating Python virtual environment..."; \
		python3 -m venv $(PYTHON_ENV); \
		echo "Virtual environment created."; \
	else \
		echo "Virtual environment already exists."; \
	fi

# Install libraries using pip
install-libs: create-venv
	@echo "Activating virtual environment..."
	. $(PYTHON_ENV)/bin/activate && \
	echo "Upgrading pip..." && \
	pip install --upgrade pip && \
	pip install poetry && \
	echo "Installing libraries" && \
	poetry install && \
	echo "Libraries installed."

# Create a symbolic link for the 'zania' command
set-alias:
	@echo "Setting up 'zania' alias in $(SHELL_CONFIG)..."
	@if grep -q "alias zania=" "$(SHELL_CONFIG)"; then \
		sed -i.bak '/alias zania=/d' "$(SHELL_CONFIG)"; \
	fi
	@echo "alias zania='$(ZANIA)'" >> "$(SHELL_CONFIG)"
	@echo "Alias has been added to $(SHELL_CONFIG)"
	@echo "To use the alias in this session, run:"
	@. $(SHELL_CONFIG)
	@echo "Usage: zania run-server [dev|production] | zania config"

# Clean the environment (remove venv and symlink)
clean:
	@echo "Cleaning up..."
	@rm -rf $(PYTHON_ENV)
	@echo "Removing 'zania' alias from $(SHELL_CONFIG)..."
	@if grep -q "alias zania=" "$(SHELL_CONFIG)"; then \
		sed -i.bak '/alias zania=/d' "$(SHELL_CONFIG)"; \
		echo "Alias has been removed from $(SHELL_CONFIG)"; \
	else \
		echo "Alias not found in $(SHELL_CONFIG)"; \
	fi
	@echo "To remove the alias from this session, run:"
	@echo "unalias zania"
	@echo "Cleaned up."
