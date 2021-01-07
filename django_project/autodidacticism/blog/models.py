# Importing the native django methods: 
from django.db import models
from django.utils.text import slugify


class ArticleModel(models.Model):
	"""A Model Object representing an article stored in the database.

	The Article Model contains the follwing fields:

	* An Article Title

	* A Date Uploaded

	* A description that summarizes the content of the article that is used
		in the thumbnail.

	* An associated markdown file that contains all of the content for 
		the actial article (This is what is rendered when an article is
		 navigated to.)

	* A 'slug' value that will be used to uniquely indentify each article. 

	* A string containing the category that the article belongs to.

	Attributes:
		article_title (models.CharField): The string representing the title 
			of The article.

		upload_date (models.DateTimeField): A database attribute representing
			the date that the article was uploaded (when the model instance was
			created). This model auto-generates upon creation of an instance.
		
		article_description (models.CharField): A string of text that represents
			a description of the article. This is the text that is rendered in the
			thumbnail.

		articel_content (models.FileField): This is the markdown file that contains
			the actual article contents. This is the file that is rendered when
			the atual article is clicked on.

		article_slug (models.SlugField): A slug string that is created by an internal
			method that is called every time a new model instance is created. It is
			used to uniquely identify each article for the purposes of dynamic rendering
			and url routing.

		article_category (models.CharField): A string that represents the category that
			the article belongs to. This field is a string that is selected from a list
			of pre-existing choices and is used primarily for internal SEO.
	"""
	# Defining main Article model fields:
	article_title = models.CharField(
		max_length=250,
		verbose_name="Article Titile")

	upload_date = models.DateTimeField(auto_now=True)

	article_description = models.CharField(
		max_length=500,
		verbose_name="Article Description")

	# Upload to the MEDIA_ROOT/articles folder:
	articel_content = models.FileField(
		upload_to="articles/",
		verbose_name="Article Content Markdown File")

	# Parameter is auto-generated upon model instance creation:
	article_slug = models.SlugField(
		max_length=250,
		unique=True,
		blank=True)

	article_category = models.CharField(
		max_length=50,
		null=True,
		verbose_name="Article Category",
		choices=(
			('FinTech & Investing','fintech_investing'),
			('Machine Learning','machine_learning'),
			('Computational Biology','computational_biology'),
			('Data Engineering','data_engineering'),
			('Web Development', 'web_development'))
		)

	# Nested class describing the metadata for the model:
	class Meta:
		
		# Sorting by most recent:
		ordering = ['-upload_date']

		verbose_name_plural="Articles"

	def save(self, *args, **kwargs):
		"""Overwrites the default models.Model save method in order
		to generate a slug value upon creation.

		The method is called when a Model instance is created. It 
		converts the article_title field for said instance and 
		'slugifys' it. This slugify-ed parameter is the param saved
		in the article_slug field.

		The process for saving a model instance is as follows:

		Instance is created --> This save method is called -->
		save method creates slug value and assigns it to parameter 
		article_slug --> save method for models.Model is called w/ *args and 
		**kwargs --> instance is save to db with default save implementation.

        Args:
            *args (*args): Boilerplate arguments for the default 'save' method.
            
            **kwargs (*kwargs): Boilerplate kew-word arguments for the default
		"""
		# Converting article title into slug and assigning value to article_slug:
		self.article_slug = slugify(self.article_title) 

		# Saving the model instance:
		super(ArticleModel, self).save(*args, **kwargs)   

	def get_markdown_text(self):
		"""The method that opens and converts the model instance's markdown 
		file into a string containing all contents of said file.
		
		This method can be called either on the back-end and passed into the
		template or called directly in the template.

		Returns:
			str: The markdown string containing all the content from the markdown
				file.

		"""
		# Opening Markdown file to extract markdown text:
		mkdn_file = open(self.articel_content.path, 'r')

		return mkdn_file.read()

	# Method for representing the object:
	def __str__(self):
		return self.article_title

	

class PaperModel(models.Model):
	"""An object representing a pdf Paper stored in the database.
	
	The PaperModel contains the following fields:

	* Title of the Paper

	* Date Uploaded/Written

	* The Date the Paper was published 

	* Authors

	* A Short Description of the paper/abstract

	* The category that the paper belongs in

	* The actual paper stored as a pdf file.

	* A slug representing the pdf paper based on the title.

	These fields are represented in the Model by the following fields:

	Attributes:

		paper_title (models.CharField): The string representing the title
			of the assocaited pdf file.

		upload_date (models.DateTimeField): The datetime object representing
			when the paper was uploaded to the database.
	
		published_date (models.DateTimeField): The datetime object representing
			when the paper was published if their is a publcation date.

		authors (models.CharField): The string representing the author or authors of
			the paper.

		paper_description (models.CharField): A long string representing a description
			of the paper.
		
		paper_category (models.CharField): A string that represents the category that
			the paper belongs to. This filed is selected from categorical choices

		paper (models.FileField): The pdf of the actual paper. This is the object
			that represents the pdf file. It allows the upload of a pdf file.

		paper_slug (models.SlugField): A slug string that is created by an internal
			method that is called every time a new model instance is created. It is
			used to uniquely identify each paper for the purposes of dynamic rendering
			and url routing.

	"""
	# Declaring model parameters:
	paper_title = models.CharField(
		max_length=200,
		verbose_name = "Paper Title")

	upload_date = models.DateTimeField(auto_now=True)
	published_date = models.DateTimeField(
		null=True,
		verbose_name="Published Date",
		blank=True)

	authors = models.CharField(
		max_length=400,
		verbose_name="Authors",
		null=True)

	paper_description = models.CharField(
		max_length=500,
		verbose_name="Report Description")

	paper_category = models.CharField(
		max_length=50,
		verbose_name="Paper Category",
		choices=(
			('FinTech & Investing','fintech_investing'),
			('Machine Learning','machine_learning'),
			('Computational Biology','computational_biology'),
			('Data Engineering','data_engineering'),
			('Web Development', 'web_development'))
		)

	paper = models.FileField(
		upload_to='papers/',
		verbose_name='Paper PDF')

	paper_slug = models.SlugField(
		max_length=200,
		unique=True,
		blank=True)

	# Nested class describing the metadata for the model:
	class Meta:
		
		# Sorting by most recent:
		ordering = ['-upload_date']

		verbose_name_plural="Papers"

	def save(self, *args, **kwargs):
		"""Overwrites the default models.Model save method in order
		to generate a slug value upon creation.

		The method is called when a Model instance is created. It 
		converts the paper_title field for said instance and 
		'slugifys' it. This slugify-ed parameter is the param saved
		in the paper_slug field.

		The process for saving a model instance is as follows:

		Instance is created --> This save method is called -->
		save method creates slug value and assigns it to parameter 
		paper_slug --> save method for models.Model is called w/ *args and 
		**kwargs --> instance is save to db with default save implementation.

        Args:
            *args (*args): Boilerplate arguments for the default 'save' method.
            
            **kwargs (*kwargs): Boilerplate kew-word arguments for the default
		"""
		# Converting article title into slug and assigning value to article_slug:
		self.paper_slug = slugify(self.paper_title) 

		# Saving the model instance:
		super(PaperModel, self).save(*args, **kwargs)   

	# Method for representing the object:
	def __str__(self):
		return self.paper_title
