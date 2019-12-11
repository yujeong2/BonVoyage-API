from urllib.request import urlopen
import json
import urllib


def content(sigungu, start, end):
    sigunguCode = sigungu
    eventStartDate = start
    eventEndDate = end

    content_id = []
    content_title = []

    ServiceKey = "YNhxiZW4fi0XnstyKLJ7oDiIwuPRChN734raioSF2Zh4dOxn2SFGi5PzjB6kBoBc3x3iOLnndBfbXUYvzP7TKA%3D%3D"

    url_s = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchFestival?ServiceKey=" + ServiceKey + \
            "&MobileOS=ETC&MobileApp=TourAPI3.0_Guide&areaCode=1&numOfRows=3&listYN=Y&arrange=B&_type=json"

    url_search = url_s + "&sigunguCode=" + str(sigunguCode) + "&eventStartDate=" + str(
        eventStartDate) + "&eventEndDate=" + str(eventEndDate)

    request = urllib.request.Request(url_search)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        data = json.loads(response_body.decode('utf-8'))

        global data_num
        data_num = data["response"]["body"]["totalCount"]

        if data_num == 1:
            for i in range(0, 1):  # 정보가 1개일때
                content_title.append(data["response"]["body"]["items"]["item"]['title'])
                content_id.append(data["response"]["body"]["items"]["item"]['contentid'])

        elif data_num > 3:
            for i in range(0, 3):  # 정보가 3개보다많을때
                content_title.append(data["response"]["body"]["items"]["item"][i]['title'])
                content_id.append(data["response"]["body"]["items"]["item"][i]['contentid'])

        else:
            for i in range(data_num):  # 정보가2개 or 3개일때
                content_title.append(data["response"]["body"]["items"]["item"][i]['title'])
                content_id.append(data["response"]["body"]["items"]["item"][i]['contentid'])

        return content_id, content_title

    else:
        return {"Error Code:": rescode}
