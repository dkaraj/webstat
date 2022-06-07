from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from mainapp.error_msg import __format_error_response
from mainapp.models import Website
from mainapp.permission import Check_API_KEY_Auth
from mainapp.serializers import WebsiteSerializer, WebsiteDisplaySerializer


@api_view(["POST"])
@permission_classes((Check_API_KEY_Auth,))
def create_website(request):
    """
    It takes a request, validates it, and saves it to the database.

    :param request: The request object
    :return: The data is being returned as a dictionary.
    """

    try:
        data = {}
        serializer = WebsiteSerializer(
            data=request.data)
        if serializer.is_valid():
            website = Website(
                name=serializer.data["name"],
                code=serializer.data["code"],
                development_mode=serializer.data["development_mode"],
                support_email=serializer.data[
                    "support_email"],
                no_reply_email=serializer.data["no_reply_email"],
                developer_email=serializer.data["developer_email"],
                timezone=serializer.data["timezone"],

            )

            website.save()

            data["message"] = "Website Created successfully"
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)

        return Response(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(["POST"])
@permission_classes((Check_API_KEY_Auth,))
def remove_website(request, code):
    """
    If the user is authenticated,then delete the
    Website

    :param request: The request object
    :param code: The code of the Website you want to delete
    :return: The response is a JSON object with two keys: status and message.
    """

    website = get_object_or_404(Website, code=code)
    website.delete()

    return JsonResponse({"status": 200, "message": "Website Removed successfully"})


@api_view(["GET"])
@permission_classes((Check_API_KEY_Auth,))
def get_website_by_code(request, code):
    website = Website.objects.filter(code=code)
    if website:
        serializer_class = WebsiteDisplaySerializer(
            website, many=True).data
        return JsonResponse(serializer_class, safe=False)
    else:
        return JsonResponse({"status": 200, "message": "Website Removed successfully"})


@api_view(['POST'])
@permission_classes((Check_API_KEY_Auth,))
def update_website(request, code):
    """
    Get the Website object with the code passed in the url, then
    update the Website object with the data passed in the request

    :param request: The request object
    :param code: the code of the Website
    :return: The data is being returned as a JsonResponse.
    """

    website = get_object_or_404(Website, code=code)

    serializer = WebsiteDisplaySerializer(
        instance=website, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    else:
        errors = __format_error_response(serializer.errors)
        res = {}
        res['message'] = errors
        res['code'] = 400
        raise ValidationError(res)


@api_view(["GET"])
@permission_classes((Check_API_KEY_Auth,))
def retrive_all_websites(request):
    """
    It takes a request, gets all the objects from the Website model, serializes them and returns
    them as a JsonResponse

    :param request: The request object
    :return: A list of dictionaries.
    """

    queryset = Website.objects.all()
    serializer_class = WebsiteDisplaySerializer(queryset, many=True).data
    return JsonResponse(serializer_class, safe=False)


class WebsiteListView(generics.ListAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteDisplaySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id']
    search_fields = ['code', 'name']
