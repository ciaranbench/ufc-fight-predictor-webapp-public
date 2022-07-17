# UFC Fight Predictor Webapp
## (Public Repository)

![](demo_gif.gif)
[http://ufc-fight-predictor.com](http://ufc-fight-predictor.com)
A webapp where users can use a pretrained model to predict fight outcomes. This is the public version of the webapp repo that does not include model files and datasets. More details about the model can be found [here](https://medium.com/@ciaranbench/how-to-make-money-with-machine-learning-value-betting-on-predicted-ufc-fight-outcomes-46ef6e916912). 

### TensorFlow.js
TensorFlow.js is used to perform calculations with the pretrained model. 

### Python Backend
The user is initially presented with a starting page that has an html form to take user inputs (slection from dropdown menu of fighters). A list of all fighters in the database is used to render the dropdown menus on this page.

When this html form is submitted, the stats of each fighter will be acquired, their difference taken, and the resultant array normalised to prepare it for the pretrained network.

The network output is used to render the results page.

The results page will display an error message if no fighters, or only one fighter, is selected.

There are also two other pages that display additional information (accessible with hyperlinks).
