from rest_framework import serializers
from api.models import Player, Game
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username')


class PlayerSerializer(serializers.ModelSerializer):
    n_wins = serializers.IntegerField()
    n_games = serializers.IntegerField()
    n_ranked = serializers.IntegerField()
    n_unranked = serializers.IntegerField()
    pct_win = serializers.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        model = Player
        fields = ('player_name', 'n_wins', 'n_games', 'n_ranked', 'n_unranked', 'pct_win')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_outcome = serializers.IntegerField()
    ranked_status = serializers.IntegerField()
    ts = serializers.DateTimeField(format='%d %b %Y')
    # players = serializers.CharField(max_length=1000)

    class Meta:
        model = Game
        fields = ('game_outcome', 'ranked_status', 'ts')
