from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import ShortenerInputSerializer
from .models import ShortenedUrl
from .utils import shorten_url


class ShortenURL(APIView):
    def post(self, request):
        serializer = ShortenerInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.validated_data.get("url")
        user = None if request.user.is_anonymous else request.user

        shortened_url = shorten_url(url, user)

        return Response(
            {"shortened_url": shortened_url}, status=status.HTTP_201_CREATED
        )


class NavigateToOriginalURL(APIView):
    permission_classes = [AllowAny]

    def get(self, _, short_code):
        try:
            short_url = ShortenedUrl.objects.get(short_code=short_code)
        except ShortenedUrl.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(
            status=status.HTTP_307_TEMPORARY_REDIRECT,
            headers={"Location": short_url.original_url},
        )
