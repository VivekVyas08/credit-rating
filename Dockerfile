# Credit Rating tool - portable container. The 5+ GB model is NOT in the image: mount the host's
# models/ dir (-v) to reuse existing weights, or let the tool auto-download it on first start.
FROM python:3.12-slim

# Build tools so llama-cpp-python installs even where no prebuilt wheel matches; git for the
# optional startup sync.
RUN apt-get update && apt-get install -y --no-install-recommends \
        git build-essential cmake \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Dependencies first (layer-cached). CPU wheel of llama-cpp-python preferred; builds if absent.
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --prefer-binary \
        --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu \
        -r /app/requirements.txt

# Run as an unprivileged user, so a bug in the app cannot reach anything outside /app.
# models/ is created here so a fresh named volume mounted on it is owned by that user too.
RUN useradd --create-home --uid 10001 app
COPY --chown=app . /app
RUN mkdir -p /app/models && chown app /app /app/models
USER app

# Serve from the container; skip the git-pull sync (the image already carries the code).
# Serving beyond localhost needs a login, so pass one:  -e RATING_PASSWORD=...  (the app refuses
# to start without it), and publish on the host's loopback only:  -p 127.0.0.1:5050:5050
ENV RATING_HOST=0.0.0.0 \
    RATING_NO_SYNC=1 \
    PYTHONUNBUFFERED=1
EXPOSE 5050
CMD ["python", "webapp/app.py"]
