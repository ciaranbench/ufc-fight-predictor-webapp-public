# UFC Fight Predictor Webapp (Public Repository)  
## [http://ufc-fight-predictor.com](http://ufc-fight-predictor.com) 

![](demo_gif.gif)  
 
A Flask webapp (deployed to Heroku) where users can use a pretrained model to predict fight outcomes. This is the public version of the webapp repo that does not include model files and datasets. More details about the model can be found [here](https://medium.com/@ciaranbench/how-to-make-money-with-machine-learning-value-betting-on-predicted-ufc-fight-outcomes-46ef6e916912). 

### TensorFlow.js
TensorFlow.js is used to perform calculations with the pretrained model. 

### Other notes
The user is initially presented with a starting page that has an HTML form to take user inputs (selection from dropdown menu of fighters).

When this HTML form is submitted, the stats of each fighter will be acquired, their difference taken, and the resultant array normalised to prepare it for the pretrained network.

The results page displays the network output.

The results page will display an error message if no fighters, or only one fighter, is selected.

There are also two other pages that display additional information (accessible with hyperlinks).

### Resources
I was able to build this webapp using the following resources:  
[Tensorflow.js model in as little code as possible (GitHub Gist)](https://gist.github.com/jamescalam/f87bc4e941a86b66a782b90980f045de)  
[Run Python Script Clicking Html Button | Latest 2021](https://www.youtube.com/watch?v=0meTbQQaosU)  
[How to Deploy a Flask App to Heroku | Flask Heroku Deployment](https://www.youtube.com/watch?v=D2GLVoiEZyE)  
[How to Add Custom Domain Name to Heroku App - Heroku Custom Domain Name](https://www.youtube.com/watch?v=_tzkF68ZjVE)
