# drinking-party-ms
社内の飲み会管理システム


画面仕様
https://docs.google.com/presentation/d/1TNO_l3lOmP4rnM7k6yDS81A5CJxEUWGOTqLoQoMeL20/edit#slide=id.p
<br>
<br>
## UI
|<img width="1100px" height="auto" alt="login" src="https://user-images.githubusercontent.com/92197575/213452181-c8637b7a-b185-46f9-83eb-073adbed8f51.png">|<img width="100%" height="auto" alt="Index" src="https://user-images.githubusercontent.com/92197575/213450074-6107a264-373a-4e53-b542-f74f01ef03e3.png">|<img width="100%" height="auto" alt="Detail" src="https://user-images.githubusercontent.com/92197575/213450088-2d513641-1e2e-4183-8bcc-2211f943dd83.png">|<img width="100%" height="auto" alt="Create" src="https://user-images.githubusercontent.com/92197575/213450102-49ee5366-e655-4952-b331-6774d22511f2.png">|
|:---:|:---:|:---:|:---:|
|Login|Home|Detail|Create|
<br>
<br>

## ローカル環境の構築手順 - Get Started -

インストール
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
docker-compose up -d
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
docker-compose up -d
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

