<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="">
    <img src="https://s3.ap-southeast-1.amazonaws.com/cdn.deccanchronicle.com/sites/default/files/16FOTOLIA_9041304_XS_0.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Spam and Ham Text Classifier</h3>

  <p align="center">
    An Awesome ML model that classifies betwen Ham and Spam
    <br />

  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [License](#license)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

This is a project made in python which uses NLP algorithm , classification algorithm and clustering algorithm for making this ML model thats predicts whether the text entered id Spam or Ham

many algorithms are tested and depending upon the f1 score the best model of classification is selected and used. for clustering we used minibatchkmeans which is very effective for large datasets

also we have a frontend webpages where we integrated ML model into this using Flask micro web frameworks

### Built With

* [Bootstrap](https://getbootstrap.com)
* [Python](https://docs.python.org/3/m)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)


### Installation

This are the various libraries that need to be installed prior
```sh
pip install sklearn
pip install matplotlib
pip install pandas
pip install numpy
```
2. for woking with flask frameworks you  first need to install flask
```sh
pip install flask
```
4. command for running flask server once you have all the required file in same directory assume X directory 
```JS
cd X
python app.py runserver
```





### Usage-

Our spam detection project can be used to detect a text message , whether it is spam or not.
If it is spam, it will give the result as "spam" else a "ham" text would appear.
This is useful nowadays, as there are many such spam messages circulating on social media, emails etc.
More focus of this project is for beginners who are looking forward in the field of Data science and Machine learning.
So this project is a good start for implementing different models and for visualizing data. It can also be further modified and used for industrial purpose.


 
 For more information you can refer to https://towardsdatascience.com/
 
 
 
 ### Roadmap:

These are the files included in our project-

•	src

•	app.py

•	templates- 

	o	home.html 

	o	result.html


•	styles.css

•	NB_spam_model1svm.pkl

•	NB_spam_modelsvm.pkl

•	SPAM text message 20170820 - Data.csv


### License:

MIT License

Copyright (c) 2020

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contact-

Team members- 

			  
              Lance Dsilva - codestacks123@gmail.com
			  
	         Novia Dsilva - codestacks123@gmail.com
            
