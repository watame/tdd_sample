FROM python:3.11

# DockerのWorkdirを引数として取得
ARG SOURCE_DIR
WORKDIR ${SOURCE_DIR}

# 環境変数の設定
ENV LANG=ja_JP.UTF-8 \
    LC_CTYPE=ja_JP.UTF-8 \
    TZ=Asia/Tokyo

# パッケージのアップデートと不要なパッケージの削除
RUN apt-get update && \
    apt-get clean all && \
    rm -rf /var/cache/apt

# poetryの導入
RUN pip install poetry && \
    poetry config virtualenvs.in-project true
