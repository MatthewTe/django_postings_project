from django.shortcuts import render

# Importing blog database models:
from .models import ArticleModel, PaperModel

def blog_homepage(request, category=None):
	"""The view method that is used to render the template for the home
	page of the blog.

	It contains the logic for querying specific blog posts from the database
	and passing them into the blog template through the context parameter.	  

    Args:
        request (http request): The http request that is sent to the server from
            the client.
    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.	
    Todo: 

    	* On frontend find out how to add a "load more" feature.
	"""
	# Declaring empty context to be populated:
	context = {}

	# Logic that parses the category param if it is passed:
	if category != None:

		# Performing database query for articles of specific category:
		articles = ArticleModel.objects.filter(article_category=category)

	else:
		# Performing database query for articles:
		articles = ArticleModel.objects.all()

	# Logic that queries the database for articles based on search param:
	search_keywords = request.GET.get('search_keywords')
	if search_keywords is not None:

		articles = articles.filter(article_title__icontains=search_keywords)

	# Populating context w/ ArticleModel objects:
	context['articles'] = articles
 

	return render(request,'blog/blog_home.html', context=context)


# Method that renders a single blog post from markdown:
def blog_post(request, slug):
	"""The view method that is used to render the template displaying
	an individual article.

	The method queries the database for an article containing the slug
	extracted from the url parameter. The Article data model is passed
	to the front-end via the context and is then rendered using the
	templating engine.  

    Args:
        request (http request): The http request that is sent to the server from
            the client.
		
		slug (str): The slug string passed from the url that is used to query
			the specific Article model instance.

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.	

	"""
	# Empty context to be populated:
	context = {}

	# Querying the database for article w/ specific slug:
	article = ArticleModel.objects.get(article_slug__exact=slug)

	# Populating Context:
	context['article'] = article
	context['slug'] = slug

	return render(request, 'blog/individual_article.html', context=context)


def papers_homepage(request, category=None):
	"""The view method that is used to render the template for the papers
	homepage.

	It contains the logic for querying specific paper posts from the database
	and passing them into the paper template through the context parameter.

    Args:
        request (http request): The http request that is sent to the server from
            the client.
    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.	

	Todo:
		* Do reasearch on how pdf files should be served and displayed.

	"""
	# Creating empty context to be populated:
	context = {}

	# Logic performing custom paper database query based on category param:
	if category != None:

		# Performing the custom query for papers based on categories:
		papers = PaperModel.objects.filter(paper_category=category)

	else:
		# Performing query for all papers if no category query:
		papers = PaperModel.objects.all()

	# Logic performing additional filtering of papers based on serach param:
	search_keywords = request.GET.get('search_keywords')
	if search_keywords is not None:

		papers = papers.filter(paper_title__icontains=search_keywords)
	

	# Populating context:
	context['papers'] = papers

	return render(request, 'blog/papers_home.html', context=context)

def paper_download(request, pdf_path):
	"""The method that serves the pdf indicated by the path to the user.

	TODO: Add logic to serve a paper indicated by the path of the FileField
	as a downloadable file. Click --> Download --> Open as PDF. 

    Args:
        request (http request): The http request that is sent to the server from
            the client.
		
		slug (str): The slug string passed from the url that is used to query
			the specific Article model instance.

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.	

	"""
	return render(request, 'blog/individual_article.html')





