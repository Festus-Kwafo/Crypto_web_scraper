from rest_framework.decorators import api_view
from crypto.web_scraping import scrap_data_2
from rest_framework.views import APIView
from rest_framework.response import Response
from crypto.models import Crypto
from crypto.serializers import CryptoSerializer
import pandas as pd
from datetime import datetime


class StartScraping(APIView):
    def get(self, request):
        try:
            scrap_data_2()
            return Response({"detail": "Task started successfully in the background"})
        except Exception as e:
            return Response({"detail": "Error in starting the task"})


@api_view(['GET', 'DELETE'])
def records_list(request):
    all_records = Crypto.objects.all()
    if request.method == 'GET':
        serializer = CryptoSerializer(all_records, many=True)
        return Response(serializer.data, status=200)
    if request.method == 'DELETE':
        all_records.delete()
        return Response({'detail': 'All records has been deleted'}, status=202)


def create_data_excel():
    crypto = Crypto.objects.all()
    df = pd.DataFrame(list(crypto.values()))
    return df.to_excel('output_{}.xlsx'.format(datetime.now().strftime("%H%M%S%m%d%Y")))
