import requests
import json
from .models import *


AToken = "EAAL4k0Xs5XUBABjj9uOsIDYhRmu3AE0X0LRyJovAVl3XLQrfwHYZCV13frQScIyvXWutZAvtVLuGgCktckDoyAYZByWgsBDuokRbjx0cxQD3eZBZCDvI2X3f3kzlVi23ik2x0P97qwLjbYHHu88EWx0ByNpZCJdfYZCTNZC640AYKQuekgbYL60wLKqSuqPTXUkZD"
def page_info():
    info = requests.get("https://graph.facebook.com/v9.0/133182234162903?fields=username%2Cname%2Cfan_count%2Cabout&access_token="+AToken)
    dataa = info.json()
    pname = dataa["name"]
    fcount = dataa["fan_count"]
    about = dataa["about"]
    purl = "https://www.facebook.com/"+dataa['username']
    _page , page_ = Page.objects.get_or_create(page_id=dataa['id'],page_name=str(pname),page_fans=str(fcount),page_about=str(about),page_url=str(purl))


def post_info():
    post_info = requests.get("https://graph.facebook.com/v9.0/133182234162903/posts?access_token="+AToken)
    post_data = post_info.json()
    for i in post_data['data']:
        post_id= i['id']
        posts_info = requests.get("https://graph.facebook.com/v9.0/"+post_id+"?fields=message%2Cshares%2Cfull_picture%2Cpermalink_url%2Creactions.summary(total_count)%2Clikes.summary(total_count)%2Ccreated_time&access_token="+AToken)
        posts_data = posts_info.json()
        pageid = Page.objects.get(page_id=posts_data['id'].split('_')[0])
        po_id = str(posts_data['id'])
        if 'full_picture' in posts_data:
            po_photo = str(posts_data['full_picture'])
        else:
            po_photo = "No Photo in Post"
        if 'message' in posts_data:
            po_message = str(posts_data['message'])
        else:
            po_message = "No Message On Post"
        po_permalink = str(posts_data['permalink_url'])
        po_likes_count = posts_data['likes']['summary']['total_count']
        if 'shares' in posts_data:
            po_shares_count = posts_data['shares']['count']
        else:
            po_shares_count = 0
        po_reaction = posts_data['reactions']['summary']['total_count']
        po_time = str(posts_data['created_time'])
        _post, post_ = Posts.objects.get_or_create(page_fid=pageid,post_id=po_id,post_photo=po_photo,post_message=po_message,post_permalink=po_permalink,post_likes_count=po_likes_count,post_shares_count=po_shares_count,post_reaction=po_reaction,post_time=po_time)