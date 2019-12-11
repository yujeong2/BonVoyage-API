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

        if data_num == 0:
            content_id.append("null")
            content_title.append("null")

        elif data_num == 1:
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

    else:
        return {"Error Code:": rescode}

    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailIntro?ServiceKey=" + ServiceKey + \
          "&contentTypeId=15&MobileOS=ETC&MobileApp=TourAPI3.0_Guide&introYN=Y&_type=json"

    content_num = data_num

    content_id_detail = []
    url_detail = []
    request_detail = []
    response_detail = []
    rescode_detail = [0, 0, 0]
    response_body_detail = []
    data_detail = []
    eventplace = []
    playtime = []
    usetimefestival = []

    if content_num == 0:
        content_title.append("null")
        eventplace.append("null")
        playtime.append("null")
        usetimefestival.append("null")

    elif content_num > 3:
        for a in range(0, 3):
            url_detail.append(url + "&contentId=" + str(content_id[a]))
            request_detail.append(urllib.request.Request(url_detail[a]))
            response_detail.append(urllib.request.urlopen(request_detail[a]))
            response_body_detail.append(response_detail[a].read())
            # print(response_body_detail[a].decode('utf-8'))
            data_detail.append(json.loads(response_body_detail[a].decode('utf-8')))
            eventplace.append(data_detail[a]['response']['body']['items']['item']['eventplace'])
            playtime.append(data_detail[a]['response']['body']['items']['item']['playtime'])
            usetimefestival.append(data_detail[a]['response']['body']['items']['item']['usetimefestival'])
    else:
        for a in range(content_num):
            url_detail.append(url + "&contentId=" + str(content_id[a]))
            request_detail.append(urllib.request.Request(url_detail[a]))
            response_detail.append(urllib.request.urlopen(request_detail[a]))
            response_body_detail.append(response_detail[a].read())
            # print(response_body_detail[a].decode('utf-8'))
            data_detail.append(json.loads(response_body_detail[a].decode('utf-8')))
            eventplace.append(data_detail[a]['response']['body']['items']['item']['eventplace'])
            playtime.append(data_detail[a]['response']['body']['items']['item']['playtime'])
            usetimefestival.append(data_detail[a]['response']['body']['items']['item']['usetimefestival'])

    return content_title, eventplace, playtime, usetimefestival


c = content(sCode, eSdate, eEdate)

keys = ['number', 'title', 'eventplace', 'playtime', 'usetimefestival']
if data_num == 0:
    values = ["null", "null", "null", "null", "null"]
    A = dict(zip(keys, values))
    print(A)
elif data_num == 1:
    values = ["1", c[0], c[1], c[2], c[3]]
    A = dict(zip(keys, values))
    print(A)
elif data_num == 2:
    values_1 = ["1", c[0][0], c[1][0], c[2][0], c[3][0]]
    values_2 = ["2", c[0][1], c[1][1], c[2][1], c[3][1]]
    A = dict(zip(keys, values_1))
    B = dict(zip(keys, values_2))
    print(A)
    print(B)
else:
    values_1 = ["1", c[0][0], c[1][0], c[2][0], c[3][0]]
    values_2 = ["2", c[0][1], c[1][1], c[2][1], c[3][1]]
    values_3 = ["3", c[0][2], c[1][2], c[2][2], c[3][2]]
    A = dict(zip(keys, values_1))
    B = dict(zip(keys, values_2))
    C = dict(zip(keys, values_3))
    print(A)
    print(B)
    print(C)

