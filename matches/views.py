from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Match
from .serializer import MatchSerializer


@api_view(["GET", "POST"])
def matches(request):
    if request.method == "GET":
        all_matches = Match.objects.all()
        serializer = MatchSerializer(all_matches, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            new_match = serializer.save()
            {
                "test_player": "dxm.glen",
                "test_opposite": "user2",
                "player_point": 10,
                "opposite_point": 15,
                "place": "중화",
            }
            return Response(MatchSerializer(new_match).data)
        else:
            return Response(serializer.erros)
