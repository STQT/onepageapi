from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from onepageapi.stats.serializers import TgUserSerializer, UserForcingSerializer
from onepageapi.stats.models import TgUser, UserForcing


class TgUserView(APIView):
    serializer_class = TgUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            obj, created = TgUser.objects.get_or_create(**serializer.validated_data)

            return Response(self.serializer_class(obj, many=False).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserForcingView(APIView):
    serializer_class = UserForcingSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            tg_user = validated_data.pop('tg_user_id', None)
            if tg_user:
                tg_user_obj = TgUser.objects.filter(tg_id=tg_user)
                if tg_user_obj.exists():
                    tg_user_obj = tg_user_obj.first()
                    obj = UserForcing.objects.create(tg_user=tg_user_obj, json=validated_data.get('json'))
                    return Response(self.serializer_class(obj, many=False).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
