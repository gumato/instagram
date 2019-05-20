# Instagram
## Built By pricilla 19th May 2019
## Description
This is a web application where a user is able to view images. Image details are stored in categories and tagged by Location. The admin is responsible for uploading, editing or deleting images.

# User Stories
## Users would like to:

- Sign in to the application to start using.
- Upload my pictures to the application.
- See my profile with all my pictures.
- Follow other users and see their pictures on my timeline.
- Like a picture and leave a comment on it.
Admin :

Sign in to the gallery
Create new images for showcasing
Update image post details.
Delete images
Specifications
Behaviour	Input	Output
Admin Authentication	On demand	Access Admin dashboard
Display all images	Home page	Clickable links to open any images in a modal
To add an image	Through Admin dashboard	Add and add categories and tag location of Image
To edit image	Through Admin dashboard	Redirected to the image form details and editing happens
To delete an image	Through Admin dashboard	click on image object and confirm by delete button
To search	Enter text in search bar	Users can search by category
SetUp / Installation Requirements
python3.6
pip
virtualenv
Requirements.txt
Cloning
In your terminal:

 $ git clone https://github.com/gumato/Personal-Gallery
 $ cd personal-gallery
Running the Application
Creating the virtual environment

 $ python3.6 -m venv --without-pip virtual
 $ source virtual/bin/activate
 $ curl https://bootstrap.pypa.io/get-pip.py | python
Installing Django and other Modules

 $ see Requirements.txt
To run the application, in your terminal:

 $ python3.6 manage.py runserver
Testing the Application
To run the tests for the class files:

 $ python3.6 manage.py test
Technologies Used
Python3.6
Django and postgresql
License
MIT License
Copyright (c) 2019 Pricilla Gumato Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Support and contact details
For any inquiries or contributions please contact me on gmail gumatopricilla22@gmail.com licensing. pricilla/personal gallery A web application that contain your photos,you can view,update or delete.User can also search for a photo. Language Python Last updated 8 hours ago pricilla/personal gallery May 10th Added by GitHub