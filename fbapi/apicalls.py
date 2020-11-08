import requests
import json
from .models import *



def page_info():
    AToken = "EAAMFzcYJMwwBAPwU9mu1rZBU1RGgh3uZCiu2QbP98jZCZBWZBhpevapOlynGQOMdDkGZAcRtnhoNzihZAUT3IKGSiBhrYZBZByQNznbKjuX9Oss5307aB7yxCLYn1xzZAh5WZB3CmNXQoPvNtMGiwHeJ6Hnm5KZBbv4hNgO00S77vD265dWk5330RLt20eM9ADKZCML4JLBs2ZBeiVRZCUywElYdMKVZBeVTD48cUKxIrzEaOWfXtAZDZD"
    info = requests.get("https://graph.facebook.com/v8.0/923260908017503?fields=name%2Cfan_count&access_token="+AToken)
    dataa = info.json()
    print(type(dataa))
    print(dataa)
    pname = dataa["name"]
    fcount = dataa["fan_count"]
    _page , page_ = Page.objects.get_or_create(page_name=str(pname),page_likes=str(fcount))