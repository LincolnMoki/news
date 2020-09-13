from flask import render_template, redirect, url_for, request
from . import main
from ..models import Sources
from ..request import get_sources, get_articles


@main.route('/')
def index():

    # get  news

    top_news = get_sources('top')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    tech_news = get_sources('tech')
    science_news = get_sources('science')
    health_news = get_sources('health')


    title = 'top news coverage'

    return render_template('index.html', title=title, top=top_news, Business=business_news,
                           Entertainment=entertainment_news, Sports=sports_news, Tech=tech_news,
                           Science=science_news, Health=health_news)



@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id, per_page):
    '''
    Function that returns articles based on their sources
    '''

    news_source = get_articles(source_id, per_page)
    title = f'{source_id} | All Articles'
    return render_template('articles.html', title=title, name=source_id, news=news_source)


