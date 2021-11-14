# OVAAS2 Backend
 
## 実行環境
 - Docker
 - Docker Compose
 - Python 3.9
 
***
 
## 環境構築

GitHub リポジトリをダウンロード
 
```bash
git clone [git@github.com:OVaaS/ovaas2-backend.git](https://github.com/OVaaS/ovaas2-backend.git)
cd ovaas2-backend
code .
```

Pipenvをインストール

```
pip install pipenv
```

環境変数を設置

```bash
# Linux or Mac
cp example.env .env
# Windows
copy example.env .env
```

依頼項目をインストール

```bash
make install
```
 
コンテナをビルド

```bash
make build
```

開発環境を起動

```
make start
```
 
[http://localhost:8000](http://localhost:8000)にアクセスし、起動を確認。

linterで構文チェック

```
pipenv lint
```

linterで自動修正

```
pipenv format
```
