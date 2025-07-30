FROM ubuntu:22.04 as builder

RUN apt-get update && apt-get install -y \
    python3.10 python3.10-venv python3-pip build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3.10 -m venv /opt/venv

COPY requirements.txt .

RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install -r requirements.txt

COPY . .

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3.10 python3.10-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app /app

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# EXPOSE nên đi kèm thông tin
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn landingpage.wsgi:application --bind 0.0.0.0:8000"]
