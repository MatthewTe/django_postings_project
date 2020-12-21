from django.shortcuts import render



def blog_homepage(request):
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
    	* Pass in query parameters form search and use said parameters to build database query.

    	* Create database model for article and use templating to dynamically generate.

    	* On frontend find out how to add a "load more" feature.
	"""


	return render(request,'blog/blog_home.html')

# Method that renders a single blog post from markdown:
def blog_post(request):
	"""
	"""
	pass


def papers_homepage(request):
	"""
    Args:
        request (http request): The http request that is sent to the server from
            the client.
    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.	

	Todo:
		* Actually create base homepage for paper pdfs like blog page.
	"""
	return render(request, 'blog/papers_home.html')






