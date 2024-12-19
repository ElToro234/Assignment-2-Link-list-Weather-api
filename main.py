from news_Api import newsApiHandler
from LinkedList import Linkedlist

def main():
    api_key = 'API_KEY'
    news_api = newsApiHandler(api_key)

    headlines = news_api.get_top_headlines()
    articles_list= Linkedlist(None)


    article_1 = headlines[0]["title"]
    article_2 = headlines[1]["title"]
    article_3 = headlines[2]["title"]
    article_4 = headlines[3]["title"]
    article_5 = headlines[4]["title"]
    article_6 = headlines[5]["title"]
    article_7 = headlines[6]["title"]

    articles_list.append(article_1)
    articles_list.append(article_2)
    articles_list.append(article_3)
    articles_list.append(article_4)
    articles_list.append(article_5)
    articles_list.append(article_6)
    articles_list.prepend(article_7)

    articles_list.remove_first()
    articles_list.remove_last()

    print('The size of this linkedlist is: ', articles_list.get_size())
    print("\nArticles in the Linked List:")
    articles_list.print_linkedlist()

if __name__ == '__main__':
    main()