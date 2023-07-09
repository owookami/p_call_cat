import statistics
import time
import math
import random
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company
from .serializers import CompanySerializer


# 요청 URL
# http://www.localdata.go.kr/platform/rest/TO0/openDataApi?authKey=ygGgGPDZ0EuMzUN6IZ3SZoXx0XoicwAEkzlUPK=8BvA=
# 개발 서비스 키 운영 시 서비스 키 재 요청 필요.
# ygGgGPDZ0EuMzUN6IZ3SZoXx0XoicwAEkzlUPK=8BvA=

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")
    
@api_view(['GET'])
def randomQuiz(request, id):
    total = Company.objects.all()
    # randomQuizs = random.sample(list(total), id)
    serializer = CompanySerializer(total, many=True)
    

        
@api_view(['GET'])
def getLocalDATA(request):
    
    auth_key = "ygGgGPDZ0EuMzUN6IZ3SZoXx0XoicwAEkzlUPK=8BvA="
    result_type = "json"    
    page_size = "500"
    get_data(1)
    total_count, rows = get_data(1)
    
    # #필요 값 list 추가
    result_list = []
    result_list.extend(rows)  
    # # loopCount = math.ceil(int(total_count)/int(page_size))
    
    if int(total_count) > int(page_size):
        # num_pages = total_count / page_size + 1  
        num_pages = math.ceil(int(total_count) / int(page_size))
        
        for page in range(2, num_pages+1):
            print(f"numpages / page = {num_pages} / {page}")
            # 강제 끊김을 방지하기 위한 sleep - ConnectionResetError(10054, '현재 연결은 원격 호스트에 의해 강제로 끊겼습니다'
            time.sleep(3)
            _,rows = get_data(page)
            result_list.extend(rows)
            print('result_list.extend############## ')
        
    print('totalCount:',total_count) # 전체 데이터수        
    print('result_list . end :',total_count) # 전체 데이터수        
    # print('rows:', result_list)#오픈 API 호출 결과 데이터의 개수 확인 및 저장
    data = {'meassage': 'success','totalCount':total_count, 'data':result_list}
    return Response(data)
    
def get_data(page):
    url = "http://www.localdata.go.kr/platform/rest/TO0/openDataApi"
    auth_key = "ygGgGPDZ0EuMzUN6IZ3SZoXx0XoicwAEkzlUPK=8BvA="
    result_type = "json"
    # API 호출 파라미터
    params = {
        'authkey': auth_key,
        'resultType': result_type,
        'pageSize': 500,
        'pageIndex': page,      
    }
    try:    
        response = requests.get(url, params=params)
        
        #JSON 데이터 추출
        json_data = response.json()
        
        #필요한 값 추출 
        total_count = json_data["result"]["header"]["paging"]["totalCount"]
        page_size = json_data['result']['header']['paging']['pageSize']
        page_index =json_data ['result']['header']['paging']['pageIndex']
        rows = json_data['result']['body']['rows']
        process_code = json_data['result']['header']['process']['code']
        process_message = json_data['result']['header']['process']['message']
        
        print('total_count : ' ,total_count)
        print('page_size : ' ,page_size)
        print('page_index : ' ,page_index)
        print('process_code : ' ,process_code)
        print('process_message : ' ,process_code)
        
        return total_count, rows
    except Exception as e :
        print('get_data 호출 오류 발생.', e)
        error_data = {'message': 'Error'}
        return Response(error_data, status=statistics.HTTP_500_INTERNAL_SERVER_ERROR)
    
