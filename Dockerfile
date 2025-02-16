# Python 3.10 をベースにする
FROM python:3.10

# 作業ディレクトリを `/app` に設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# ホストのファイルをコンテナにコピー
COPY . .

# Pythonの依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# 静的ファイルを収集
RUN python manage.py collectstatic --noinput

# GunicornでDjangoを起動
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]