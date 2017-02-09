from django.shortcuts import render
from datetime import datetime
from mainsite.scraper import fetch_twitter_posts

def index(request):
    '''
    Render the main page, with tweets specified by a keyword.
    The number of tweets queried is specified by 'count', defaults to 1000
    '''
    template_items = {}
    keyword = request.GET.get('keyword', None)
    count = request.GET.get('count', None)
    if count:
        try:
            count = int(count)  # convert unicode to integer
        except ValueError:      # invalid literal for count get parameter
            count = 1000

    if keyword:                 # if a keyword is defined
        template_items['keyword'] = keyword
        response, status = fetch_twitter_posts(keyword=keyword, count=count)
        template_items['response'] = response
        template_items['status'] = status

    template_items['now'] = datetime.now() # get the datetime at this moment
    
    return render(request, 'index.html', template_items)
