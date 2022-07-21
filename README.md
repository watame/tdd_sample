# 概要
テスト駆動開発を理解するためのサンプルレポジトリ。
わかり悪いところとかあったら指摘をお願いします！

# レポジトリ構成
座学用テキスト、コードサンプル、実行環境用コンテナ設定で構成されている。
```
tdd_sample
    ├── .devcontainer
    ├── container
    │   └── Dockerfile
    ├── sample
    │   ├── test
    │   │   └── test_sample.py
    │   ├── main.py
    │   ├── poetry.lock
    │   └── pyproject.toml
    ├── docker-compose.yml
    ├── README.md
    ├── テストで考えたい観点.md
    └── テスト駆動開発のやり方.md
```

# お試し環境の起動方法
DockerCompose, RemoteContainer のどちらでも起動できる

## DockerCompose
下記の順番でコマンドを打てばOK
1. `docker-compose up`
2. `docker-compose app exec bash`
3. `poetry install`

# RemoteContainer
1. コマンドパレットを起動
2. `Remote-Containers: Reopen in Container` とコマンドパレットに入力して起動
3. 新たなターミナルを起動
4. `poetry install`
