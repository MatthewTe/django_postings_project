# Autodidactism  

## Introduction
Autodidactism is the process of self education, the process of education without guidance or masters. This website was built with the goal of helping me with and documenting my path of autodidactism. As I explore various fields of interest the autodidactism site allows me to post Articles and Papers of interest. I designed the site to reflect my philosophy of education and by extension software design which is essentially a poor man’s Occam's razor: minimizing unnecessary complexity with a focus on simplicity and practicality over style.

I may add more functionality to the site if it becomes necessary however the site was not intended to host any other web based projects, only blog posts and pdf files.

## Backend Description
The site is written solely in python using the django framework. In keeping with the philosophy of simplicity and minimizing unnecessary complexity the front-end of the site is almost exclusively HTML with basic CSS. CSS is kept to a minimum, mainly used to keep content neatly as opposed to aesthetically displayed. Additional functionality may be needed that requires javascript to be executed on the front-end such as JQuery. If that becomes necessary this section will be updated to reflect the javascript that is used however as it stands all functionality and front-end is handled by stock HTML and primary CSS styling.

## Hosting and Production Environment
The django site is currently hosted on [Heroku](https://www.heroku.com/) and uses a PostgreSQL backend to store file path information about each Article and Paper database model instance. Heroku compiles the environment as a container from a Dockerfile in the main repository. 

In the django production environment static files such as pdf and markdown files are served via the [`WhiteNoise`](http://whitenoise.evans.io/en/stable/) web application. PDF files are rendered in the browser directly and blog posts are written and uploaded to the site as a markdown file. The contents of this markdown file is then rendered as an HTML page via the [`markdownify`](https://pypi.org/project/markdownify/) package. This makes all blog posts and papers stored within the internal docker environment’s file system as static files. This also means that pdfs and markdown files can be found in the [git repository](https://github.com/MatthewTe/django_postings_project) for the project. This is not the most efficient way of storing and uploading content to a site however for a single user (myself) and for a relatively small number of files and database transactions it should be sufficient (and in keeping with the philosophy of practicality above all else).

## Conclusion
Overall this site is not meant to provide much functionality. It is meant to serve as a platform for publishing and accessing articles and papers that are relevant to my educational endeavours. The site reflects this basic functionality need and is appropriately bare bones. It is not intended to look nice or be complex enough to require regular maintenance. This is a set and forget Heroku hosted site that allows me an easy way to publish. It is nothing more, nothing less.   