from urllib.parse import unquote

url = 'https://ltlnf6jv.r.us-east-1.awstrack.me/L0/https:%2F%2Fprod-api.mailtag.io%2Flink-events%3Fmt__url=https%253A%252F%252Flc1.shktrk.com%252Fr%252Fe%252F1zN0RsZGzraIJpQlp%26mt__id=8c2117e3-9749-4600-89e2-a82e2ced04e2%23bWljaGFlbC5zY2hlZmZsZXJAcWlhZ2VuLmNvbQ==%2639-0/1/01000187dc1113fd-3d0396f1-0f9f-4a4a-aebc-1439cbe05c53-000000/y17IITSt7ooZ1R9vN5hGatbf8bw=320'
#url = 'https://www.rila.org/resources.download?downloadPath=https%3A%2F%2Fpanpp1j1.cafeteo.com%2F%2F%2F%2F%2F%2F%2F%2FaHR0cHM6Ly9lbnRodXNpYXN0aWMtZWR1Y2F0ZWQtY29uY2F2ZW5hdG9yLmdsaXRjaC5tZT8vYW5uYS5ob2x5c3pld3NrYUBxaWFnZW4uY29t'
temp = unquote(url)

try:
    print("orig: "+url)
    while(temp != url):
        url = temp
        temp = unquote(url)

    print("\n\nUnquoted:" + url)

    splitted = url.split('http')
    splitted.remove(splitted[0])

    URLS = []
    for url in splitted:
        joined = 'http' + url
        URLS.append(joined)
        print("\nBlock: "+joined)


    print(URLS)
    x = ' , '.join(URLS)

    print("\n"+x)
    #raise Exception("xxx")
except(Exception) as e:
    print("sdsa: "+ str(e))
