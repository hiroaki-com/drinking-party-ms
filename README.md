# drinking-party-ms
社内の飲み会管理システム


画面仕様
https://docs.google.com/presentation/d/1TNO_l3lOmP4rnM7k6yDS81A5CJxEUWGOTqLoQoMeL20/edit#slide=id.p
<br>
<br>
## ローカル環境の構築手順

クローン
```Git
git clone https://github.com/hiroaki-com/drinking-party-ms.git
```

ビルド
```Docker
docker-compose build
```

初回マイグレート
```Docker
docker-compose run --rm web python3 manage.py migrate
```

初期データ投入
```Docker
docker-compose run --rm web python3 manage.py loaddata party_fixture.json accounts_fixture.json
```

サーバー起動
```
docker-compose up
```

ログイン情報
```
email:
guest@example.com
pass:
guestpass
```

<br>
以上でアプリがご利用になれます
<br>
<br>

## データベースを作り直したい場合
<details>
    <summary>手順</summary>
<br>

サーバー起動
```
docker-compose up
```

dockerのDBコンテナへ入る<br>
```
docker-compose exec db bash
```

PostgreSQL へ接続<br>
```
psql -U postgres
```

DBをDrop<br>
```
DROP SCHEMA public CASCADE;
```

DBのスキーマを作成<br>
```
CREATE SCHEMA public;
```
マイグレート
```Docker
docker-compose exec web python3 manage.py migrate
```
<br>
</details>

