FROM python:3.14-slim

# uv est disponible en image officielle : on copie juste le binaire.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# On copie D'ABORD les fichiers de dépendances : tant qu'ils ne changent pas,
# Docker réutilise cette couche en cache et la reconstruction est instantanée.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .

EXPOSE 8000

# --host 0.0.0.0 : sans lui, le serveur n'écoute que l'intérieur du conteneur
# et reste injoignable depuis l'extérieur. Erreur classique.
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
