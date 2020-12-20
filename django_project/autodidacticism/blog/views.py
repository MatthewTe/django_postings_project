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
	"""
	return render(request,'blog/blog_home.html')