# drinking-party-ms
社内の飲み会管理システム

画面仕様
https://docs.google.com/presentation/d/1TNO_l3lOmP4rnM7k6yDS81A5CJxEUWGOTqLoQoMeL20/edit#slide=id.p


fixtureで初期データ投入
```Docker
docker-compose run --rm web python manage.py loaddata party_fixture.json accoutns_fixture.json
```
