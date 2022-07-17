'''
This script intitially renders the starting page that has an html form to take user inputs (slection from dropdown menu of fighters). A list of all fighters in the database is processed in python, and used to render the dropdown menus on the start page.
When html form is submitted, fighter names will be processed here by result().
result() will acquire the stats of each fighter from a dataset, take their difference, and normalise each element of this array to prepare it for the network.
This script will then give the network input to result.html that will compute the prediction and display it on the results page.
On the results page, there is a link to a model_acc page for a note to the user about the model's properties.

results.html will display an error message if no fighters, or only one fighter is selected.

'''
from flask import Flask, render_template, url_for, request
#Inititliase app by calling the call Flask class
#Name this net_input
app = Flask(__name__)

 
#Create set of routes - end points for website ('pages')
@app.route('/')


@app.route('/home',methods=['POST', 'GET'])
#Loads/renders index_flask.html on /home page
def home():
    import numpy as np
    #Load dataset files
    dat = np.load('fighter_database.npy',allow_pickle=True)
    fighter_dir = []
    
    for entry in dat:
        fighter_name = entry[0]
        fighter_dir.append(fighter_name)
    #fighter_list = np.load('match_outcomes.npy',allow_pickle=True)
    #male_names = []
    #for names in fighter_list:
    #    if names[0][0] not in male_names:
    #        male_names.append(names[0][0])
    #    if names[0][1] not in male_names:
    #        male_names.append(names[0][1])
    #male_names.sort()
    #male_names = male_names[1:]
    #fighter_dir = male_names
    return render_template("index_flask.html",fighter_dir=fighter_dir )
    
#Loads/renders model_acc.html on /model_acc page
@app.route('/model_acc')
def model_acc():
    return render_template("model_acc.html")
    
#Loads/renders fav_vs_und.html on /fav_vs_und page
@app.route('/fav_vs_und')
def fav_vs_und():
    return render_template("fav_vs_und.html")

#Create /result page that will proces user inputs acquired from html form
#Calculate network input, and post to html code
@app.route('/result',methods=['POST', 'GET'])
#Performs the following on the /result page
def result():
    import numpy as np
    #Get data from html form, and convert it to dict for easy processing
    output = request.form.to_dict()
    print(output)
    fighter_1_name = output["name_1"].strip()#fave
    fighter_2_name = output["name_2"].strip()#underdog

    #Load fighter stats dataset
    dat = np.load('fighter_database.npy',allow_pickle=True)
    fighter_list = np.load('match_outcomes.npy',allow_pickle=True)
    male_names = []
    for names in fighter_list:
        print(names[0][0])
        print(names[0][1])
        male_names.append(names[0][0])
        male_names.append(names[0][1])
    
    name_1_dat = []
    name_2_dat = []

    for entry in dat:
        fighter_name = entry[0]
        if fighter_name == fighter_1_name:
            name_1_dat = entry #fav figher data
        if fighter_name == fighter_2_name:
            name_2_dat = entry #underdog fighter data
    """
    name_1_dat = []
    name_2_dat = []
    for names in male_names:
        fighter_name = entry[0]
        if fighter_name == fighter_1_name:
            for entry in dat:
                fighter_name_dat = entry[0]
                if fighter_name_dat == fighter_1_name:
                    name_1_dat = entry #fav figher data
                if fighter_name_dat == fighter_2_name:
                    name_2_dat = entry #underdog fighter data
        if fighter_name == fighter_2_name:
            for entry in dat:
                fighter_name_dat = entry[0]
                if fighter_name_dat == fighter_1_name:
                    name_1_dat = entry #fav figher data
                if fighter_name_dat == fighter_2_name:
                    name_2_dat = entry #underdog fighter data
    """
    
    input_arr = 'missing_fighter'
    #If both fighters were found in the database (i.e. user enetred two fighters), take the difference between the fighters' stats. Otherwise, this code witll output 'missing_fighter'.
    if len(name_1_dat)>2 and len(name_2_dat)>2:

        name_1_dat = (name_1_dat[1:])

        name_2_dat = (name_2_dat[1:])

        name_1_dat = name_1_dat.astype(np.float32)
        name_2_dat = name_2_dat.astype(np.float32)
        print(name_2_dat)
        print(name_1_dat)

        input_dat = np.asarray(name_1_dat)-np.asarray(name_2_dat)



        input_dat = np.expand_dims(input_dat,axis=0)
        
        #Load data needed for pre-processing network input
        dataset = np.load('dataset.npy',allow_pickle=True)
        #Process dataset to make normalisation straightforward
        all_data = []
        for example in dataset:
            example = np.hstack(example)
            all_data.append(example)
        all_data = np.vstack(all_data)
        #Normalise network input
        for i in range(0,14):
            input_dat[:,i] = (input_dat[:,i] -np.mean(all_data[:,i]))/(np.max(all_data[:,i]) - np.min(all_data[:,i]))
        input_arr = input_dat
        input_arr = input_arr.tolist()
    #return network input, alonf with fighter names. 
    return render_template('result.html', input_arr = input_arr, fighter_1_name = fighter_1_name, fighter_2_name=fighter_2_name)
    



#Run app
if __name__ == "__main__":
    app.run(debug=False)
