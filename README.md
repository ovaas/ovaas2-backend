# OVAAS2 Backend
 
## 実行環境
 - Docker
 - Docker Compose
 - Python 3.9
 
***
 
## 環境構築

GitHub リポジトリをダウンロード
 
```bash
git clone git@github.com:OVaaS/ovaas2-backend.git
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

```bash
make start
```
 
[http://localhost:8000](http://localhost:8000)にアクセスし、起動を確認。

linterで構文チェック

```bash
pipenv lint
```

linterで自動修正

```bash
pipenv format
```

## django 管理

**開発環境が起動した状態で実行してください！**

マイグレーションの作成

```bash
make create-migration
```

マイグレート

```bash
make migrate
```

スーパーユーザーの作成

```bash
make create-superuser
```

## 依頼管理

パッケージのインストール

```bash
pipenv install <package>
```

パッケージの削除

```bash
pipenv uninstall <package>
```
