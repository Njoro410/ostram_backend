from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import MemberSerializer, ResidentialAreaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class StandardResultSetPagination(PageNumberPagination):
    """
    Returns paginated response
    """
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


@api_view(['GET', 'POST'])
def members_list(request):
    """
    GET, POST
    List all members and creates new members.
    """
    if request.method == 'GET':
        try:
            all_members = members.objects.all()
        except members.DoesNotExist:
            return Response({'Error': 'There are no members'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MemberSerializer(all_members, many=True)
        pagination_class = StandardResultSetPagination
        return Response({"message": "Success", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Member created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Member creation failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, member_no):
    """
    GET, PUT/PATCH, DELETE
    Display individual member by member no. Can update, view and delete member"""

    try:
        member = members.objects.get(mbr_no=member_no)
    except members.DoesNotExist:
        return Response({'message': 'Member does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response({"message": "Success", "data": serializer.data})

    elif request.method == 'PUT':
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Member updated successfully", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message": "Member update failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        return Response({"message": "Member deleted successfullly"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def residential_list(request):
    """
    Lists all residential areas and creates new residential areas.
    """
    if request.method == 'GET':
        try:
            residentials = residential_areas.objects.all()
        except residential_areas.DoesNotExist:
            return Response({'Error': 'There are no residential areas'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ResidentialAreaSerializer(residentials, many=True)
        pagination_class = StandardResultSetPagination
        return Response({"message": "Success", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ResidentialAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Residential area created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Residential area creation failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def residential_area_detail(request, residential_id):
    """
    Display, update or delete residential area
    """
    try:
        residential_area = residential_areas.objects.get(pk=residential_id)
    except residential_areas.DoesNotExist:
        return Response({'message': 'Residential area does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ResidentialAreaSerializer(residential_area)
        return Response({"message": "Success", "data": serializer.data})

    elif request.method == 'PUT':
        serializer = ResidentialAreaSerializer(
            residential_area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Residential area updated successfully", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message": "Residential area update failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        residential_area.delete()
        return Response({"message": "residential area deleted successfullly"}, status=status.HTTP_204_NO_CONTENT)
