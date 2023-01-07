# drinking-party-ms
社内の飲み会管理システム


画面仕様
https://docs.google.com/presentation/d/1TNO_l3lOmP4rnM7k6yDS81A5CJxEUWGOTqLoQoMeL20/edit#slide=id.p

## ローカル環境構築の手順

ビルド
```
docker-compose build
```

サーバー起動
```
docker-compose up
```

初回マイグレート
```Docker
docker-compose exec web python manage.py migrate
```

fixtureで初期データ投入
```Docker
docker-compose exec web python manage.py loaddata party_fixture.json accoutns_fixture.json
```
