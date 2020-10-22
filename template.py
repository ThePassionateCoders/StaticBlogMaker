#Importing required modules
from blog import ask, dumpit, year
import os
import json
import shutil
from datetime import date

today = date.today()
currentdate=today.strftime("%B %d, %Y")

#Asking for which blog post to be created
print("\nHi Let's create the post")
prevBlogs=[x for x in os.listdir() if os.path.isdir(x)]
prevBlogs.remove("__pycache__")
if len(prevBlogs)==0:
	print("\nYou don't have any previously created blogs. First creat a Blog to create template")
	choice=input("\nDo you want to create blog right now(y/n) :")
	while True:
		if choice.lower()=="y":
			os.system("python3 blog.py")
			os.system("python3 template.py")
			quit()
		elif choice.lower()=="n":
			print("\nHope to see you soon!")
			quit()
		else:
			choice=input("\nChoose correct option: ")
			
#Asking for blog for which the post should be created
print("\nChoose the blog for which you want to create post")
for i, blog in enumerate(prevBlogs):
		print(f"[{i+1}]{blog}")
while True:
	try:
		required=int(input())
		if required==0:
			raise Exception("")		
		sitename=prevBlogs[required-1]
		#Loading Data of the blog
		try:
			with open(f"{sitename}/userInputs.json") as f:
				userInputs=f.read()
			#Converting json data in python readable form	
			userInputs=json.loads(userInputs)
			break
		except :
			print("\nThis Blog file is corrupt. Please choose another :")
	except:
		print("\nChoose correct option: ")
		
def binarychoice(string):
	print(string)
	choice=input()
	if choice.lower()=="y":
		return True
	elif choice.lower()=="n":
		return False
	else:
		return binarychoice("\nChoose Correct option:")
		
def copyimg(imgpath):
	if imgpath.startswith("https://") or imgpath.startswith("http://"):
		return imgpath
	else:
		supported=["gif", "png", "jpg", "jpeg", "ico"]
		if not os.path.exists(imgpath) or imgpath.split(".")[-1] not in supported:
			imgpath=ask("File doesn't found or this format is not supported (only .gif, .png, .jpg, .jpeg and .ico formats are supported). Check the path case and type again.")
			return copyimg(imgpath)
		shutil.copy(imgpath, f"{userInputs['sitename']}/img")
		imgpath=f"{userInputs['sitename']}/img/{imgpath.split('/')[-1]}"
		return imgpath
				
#Creating post content
postbody=""
posttitle=ask("Write the Title of the post")
postsubhead=ask("Write the Subheading of the post")
creator=ask("Write your Full name")
creatordesignation=ask("Write your designation or (s/o Father's Fullname and Mother's Fullname)")

bgimg=input("\nGive two words that best describes type of your post(These will be used to get background image of page). Seprate using comma.(Example: technology,programming)\nNote:You can keep it empty if you want to use default blog categories written previously for this blog.\n")
bgimg=bgimg.replace(" ", "")
if bgimg=="":
	bgimg=userInputs["bgimg"]
else:
	while len(userInputs["bgimg"].split(","))!=2:
		bgimg=ask("Please give only 2 words seprated by comma")
		bgimg=bgimg.replace(" ", "")
bgimg_url="https://source.unsplash.com/1600x900/?"+bgimg

postdesc=ask("Give a brief description about this post.")
while len(postdesc)<100 or len(postdesc)>150 :
		postdesc=ask("Post Description shoud be more than 100 characters and less than 150 characters.")
		
postkeys=ask("Give keywords for SEO related to your blog.(seprate using comma(,))")
while len(postkeys.split(","))<10:
		postkeys=ask("Keywords shoud be more than 10.")

postpara=ask("Write intoductory paragraph of this post.")
postbody+="\n<p>"+postpara+"</p>\n"
if binarychoice("\nDo you want to add a quote after this paragraph(y/n)"):
	postbody+="\n<blockquote class='blockquote'><p style='text-align:center'>"+ask("Write the qoute: ")+"</p></blockquote>\n"
if binarychoice("\nDo you want to add an image after this paragraph(y/n)"):
	imgpath=ask("Write the path or url of image: ")
	imgpath=copyimg(imgpath)
	imgalt=ask("Please tell what to show when image is not loaded.")
	imgcap=input("\nWrite the caption of the image(If There is no Caption Please Leave it empty): \n")
	postbody+=f"""\n<img class="img-fluid" src="{imgpath}" alt="{imgalt}">\n\n<span class="caption text-muted">{imgcap}</span>\n"""
	

while binarychoice("\nDo You Want to add one more paragraph(y/n)"):
	parahead=input("\nGive Heading of this paragraph(If there is no heading Please leave empty\n")
	postbody+="\n<h2 class='section-heading'>"+parahead+"</h2>\n"
	postpara=ask("Write the paragraph.")
	postbody+="\n<p>"+postpara+"</p>\n"
	if binarychoice("\nDo you want to add a quote after this paragraph(y/n)"):
		postbody+="\n<blockquote class='blockquote'><p style='text-align:center'>"+ask("Write the qoute: ")+"</p></blockquote>\n"
	if binarychoice("\nDo you want to add an image after this paragraph(y/n)"):
		imgpath=ask("Write the path or url of image: ")
		imgpath=copyimg(imgpath)
		imgalt=ask("Please tell what to show when image is not loaded.")
		imgcap=input("\nWrite the caption of the image(If There is no Caption Please Leave it empty): \n")
		postbody+=f"""\n<img class="img-fluid" src="{imgpath}" alt="{imgalt}">\n\n<span class="caption text-muted">{imgcap}</span>\n"""
		
credits=input("\nWrite a paragrah giving credits to the deserved if needed else leave empty\n")
							
posturl=posttitle.lower().replace(" ", "-")+".html"
postpreview=f"""
<div class="post-preview">
          <a href="{posturl}">
            <h2 class="post-title">{posttitle}</h2>
            <h3 class="post-subtitle">{postdesc}</h3>
          </a>
          <p class="post-meta">Posted on {currentdate}</p>
        </div>
        <hr>      							
"""										
#Fitting contect in template
post=f"""
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="{postdesc}">
  <meta name="author" content="{sitename}">
  <meta name="author" content="{postkeys}">

  <title>{posttitle}</title>

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom fonts for this template -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

  <!-- Custom styles for this template -->
  <link href="css/clean-blog.min.css" rel="stylesheet">
  <link rel="shortcut icon" type="image/{userInputs['favicon'].split('.')[-1]}" href="img/{userInputs['favicon'].split('/')[-1]}">
  
  </head>

<body>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand" href="index.html">{sitename}</a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="index.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="olderposts.html">Posts</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="about.html">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="contact.html">Contact</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Header -->
  <header class="masthead" style="background-image: url('{bgimg_url}')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="post-heading">
            <h1>{posttitle}</h1>
            <h2 class="subheading">{postsubhead}</h2>
            <span class="meta">{currentdate}</span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Post Content -->
  <article>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          	
          	{postbody}

          <h4>Written By,<br>{creator}<br>{creatordesignation}</h4>
          {credits}
          <p>Photographs taken from <a href="https://unsplash.com/">Unsplash</a></p>
        </div>
      </div>
    </div>
  </article>

  <hr>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <ul class="list-inline text-center">
            <li class="list-inline-item">
              <a href="https://www.twitter.com/{userInputs['twun']}">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="https://www.facebook.com/{userInputs['fbun']}">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="https://www.instagram.com/{userInputs['instaun']}">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-instagram fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="https://www.github.com/{userInputs['gitun']}">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
          </ul>
          <p class="copyright text-muted">Copyright &copy; {sitename} {year}</p>
        </div>
      </div>
    </div>
  </footer>

  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>


</body>

</html>

<!-- CODE FOR POST PREVIEW
{postpreview}
-->
"""

#Creating Post page
with open(f"{sitename}/{posturl}", "w") as f:
	f.write(post)
	
#with open(f"{sitename}/index.html", "a") as f:
	
	
print("Post successfully created!")															
print(f"This is your code for post preview Pste it in index.html where other post previews are there.:\n\n{postpreview}")

#running website
os.chdir(f"{sitename}")
os.system("python -m http.server")
																																																																																																																																																																																																																																																																								
