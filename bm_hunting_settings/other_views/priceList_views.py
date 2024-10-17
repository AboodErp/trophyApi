from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from ..other_serializers.price_list_serializers import (
    CreateHuntingPriceTypePackageSerializer,
    CreateSalesPackageSerializer,
    CreateHuntingPriceListSerializer,
    CreateHuntingPriceListTypeSerializer,
    GetHuntingPriceListSerializer,
    GetHuntingPriceTypePackageSerializer,
    CreateSalesPackageSpeciesSerializer,
    GetSalesPackageSerializer,
)

from ..models import (
    SalesPackage,
    HuntingPriceList,
    HuntingPriceListType,
    HuntingPriceTypePackage,
    SalesPackageSpecies,
)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from pprint import pprint


class PriceListViewSet(viewsets.ModelViewSet):
    serializer_class = GetHuntingPriceListSerializer
    queryset = HuntingPriceList.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # pprint(request.data)

        sales_package_data = {
            "user": request.user.id,
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "sales_quota": request.data.get("sales_quota_id"),
        }
        price_list_data = {
            "area": request.data.get("area"),
            "user": request.user.id,
            "start_date": request.data.get("start_date", None),
            "end_date": request.data.get("end_date", None),
        }
        price_list_type_data = {
            "amount": request.data.get("amount"),
            "currency": request.data.get("currency"),
            "hunting_type": request.data.get("hunting_type_id"),
            "duration": request.data.get("duration"),
        }

        sales_package = None
        price_list = None
        price_list_type = None

        with transaction.atomic():
            # Create the Sales Package
            sales_package_serializer = CreateSalesPackageSerializer(
                data=sales_package_data
            )
            sales_package_serializer.is_valid(raise_exception=True)
            sales_package = sales_package_serializer.save()

            # Create the Hunting Price List
            price_list_data["sales_package"] = sales_package.id
            price_list_serializer = CreateHuntingPriceListSerializer(
                data=price_list_data
            )
            if not price_list_serializer.is_valid():
                sales_package.delete()  # Delete the previously created sales_package
                return Response(price_list_serializer.errors)

            price_list = price_list_serializer.save()

            # Create the Hunting Price List Type
            price_list_type_data["price_list"] = price_list.id
            price_list_type_serializer = CreateHuntingPriceListTypeSerializer(
                data=price_list_type_data
            )
            if not price_list_type_serializer.is_valid():

                price_list.delete()  # Delete the previously created price_list
                sales_package.delete()  # Delete the previously created sales_package
                return Response(price_list_type_serializer.errors)

            price_list_type = price_list_type_serializer.save()

            # Create the Hunting Price Type Package
            hunting_price_type_package_data = {
                "price_list_type": price_list_type.id,
                "sales_package": sales_package.id,
            }
            hunting_price_type_package_serializer = (
                CreateHuntingPriceTypePackageSerializer(
                    data=hunting_price_type_package_data
                )
            )
            if not hunting_price_type_package_serializer.is_valid():
                price_list_type.delete()  # Delete the previously created price_list_type
                price_list.delete()  # Delete the previously created price_list
                sales_package.delete()  # Delete the previously created sales_package
                return Response(hunting_price_type_package_serializer.errors)

            hunting_price_type_package_serializer.save()

            # Create Sales Package Species Data
            species_object_list = request.data.get("species_object_list", [])
            for species_data in species_object_list:
                sales_package_species_data = {
                    "sales_package": sales_package.id,
                    "species": species_data.get("id"),
                    "quantity": species_data.get("quantity"),
                    "amount": species_data.get("amount"),
                }
                sales_package_species_serializer = CreateSalesPackageSpeciesSerializer(
                    data=sales_package_species_data
                )
                if not sales_package_species_serializer.is_valid():
                    # Clean up the previously created objects
                    hunting_price_type_package_serializer.save()  # Assuming this can be re-saved or skip deletion
                    price_list_type.delete()  # Delete the previously created price_list_type
                    price_list.delete()  # Delete the previously created price_list
                    sales_package.delete()  # Delete the previously created sales_package
                    return Response(sales_package_species_serializer.errors)

                sales_package_species_serializer.save()

        return Response(sales_package_serializer.data, status=status.HTTP_201_CREATED)
