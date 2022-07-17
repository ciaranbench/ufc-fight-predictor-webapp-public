# UFC Fight Predictor Webapp
## (Public Repository)
![](demo_gif.gif)

This is the public version of the webapp repo. Model files and other datasets are not included.

### TensorFlow.js
TensorFlow.js is used to perform calculations with the pretrained model. 

### Python Backend
The user is initially presented with a starting page that has an html form to take user inputs (slection from dropdown menu of fighters). A list of all fighters in the database is used to render the dropdown menus on this page.

When this html form is submitted, the stats of each fighter will be acquired, their difference taken, and the resultant array normalised to prepare it for the pretrained network.

The network output is used to render the results page.

The results page will display an error message if no fighters, or only one fighter, is selected.

There are also two other pages that display additional information (accessible with hyperlinks).
