from core.models import Flat
from core.serailizers import FlatSerializer
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging


logger = logging.getLogger(__name__)

class FlatList(APIView):
    """
    Lists all flats, or create a flat listing
    """
    def get(self, request, format=None):
        flats = Flat.objects.all()
        serializer = FlatSerializer(flats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['posted_by']=request.user.id
        photo_urls_req = request.data.get('photo_urls')
        if not photo_urls_req:
            return Response({"message": "A filename is required"}, status=status.HTTP_400_BAD_REQUEST)

        policy_expires = int(time.time()+5000)

        data = request.data
        serializer = FlatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlatDetail(APIView):
    """
    Retrieve, update or delete a flat instance.
    """
    def get_object(self, pk):
        try:
            return Flat.objects.get(pk=pk)
        except Flat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flat = self.get_object(pk)
        serializer = FlatSerializer(flat)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        serializer = FlatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400HTTP_400_BAD_REQUEST)
