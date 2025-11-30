.PHONY: fmt
fmt:
	uv run ruff format
	uv run ruff check --fix --fix-only
