from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

filename= 'MentalHealthClassifier.pkl'
MentalHealthClassifier= pickle.load(open(filename, 'rb'))

@app.route('/', methods= ['POST','GET'])
def home() :
   return render_template('index.html')

@app.route('/result', methods= ['POST','GET'])
def result():
    if request.method == 'POST':
        input= request.form

        prediction = pd.DataFrame({
            'Gender': [input['Gender']],
            'Self_Employed': [input['Self_Employed']],
            'Family_History': [input['Family_History']],
            'Work_Interfere': [input['Work_Interfere']],
            'Employee_Numbers': [input['Employee_Numbers']],
            'Tech_Company': [input['Tech_Company']],
            'Benefits': [input['Benefits']],
            'Care_Options': [input['Care_Options']],
            'Seek_Help': [input['Seek_Help']],
            'Anonymity': [input['Anonymity']],
            'Medical_Leave': [input['Medical_Leave']],
            'Mental_Health_Consequence': [input['Mental_Health_Consequence']],
            'Coworkers': [input['Coworkers']],
            'Supervisor': [input['Supervisor']],
            'Mental_Health_Interview': [input['Mental_Health_Interview']],
            'Physical_Health_Interview': [input['Physical_Health_Interview']],
            'Mental_VS_Physical': [input['Mental_VS_Physical']],
            'Observed_Consequence': [input['Observed_Consequence'],]
        })

        prediksi= MentalHealthClassifier.predict(prediction)

        if prediksi[0]==0:
            pred= 'Has not got any treatment. '

            desc = '''If you are experiencing any of the following symptoms, please seek help.\n 

                    1) Sleep or appetite changes — Dramatic sleep and appetite changes or decline in personal care. \n
                    
                    2) Mood changes — Rapid or dramatic shifts in emotions or depressed feelings. \n
                    
                    3) Withdrawal — Recent social withdrawal and loss of interest in activities previously enjoyed. \n
                    
                    4) Drop in functioning — An unusual drop in functioning, at school, work or social activities, such as quitting sports, failing in school or difficulty performing familiar tasks. \n
                    
                    5) Problems thinking — Problems with concentration, memory or logical thought and speech that are hard to explain. \n
                    
                    6) Increased sensitivity — Heightened sensitivity to sights, sounds, smells or touch; avoidance of over-stimulating situations. \n
                    
                    7) Apathy — Loss of initiative or desire to participate in any activity. \n
                     
                    8) Feeling disconnected — A vague feeling of being disconnected from oneself or one’s surroundings; a sense of unreality. \n
                    
                    9) Illogical thinking — Unusual or exaggerated beliefs about personal powers to understand meanings or influence events; illogical or “magical” thinking typical of childhood in an adult. \n
                    
                    10) Nervousness — Fear or suspiciousness of others or a strong nervous feeling. \n
                    
                    11) Unusual behavior – Odd, uncharacteristic, peculiar behavior'''

                
        else:
            pred= 'Has got the treatment.'

            desc = ''' Depression generally isn't a disorder that you can treat on your own. But in addition to professional treatment, these self-care steps can help:

                    1) Stick to your treatment plan. Don't skip psychotherapy sessions or appointments. Even if you're feeling well, don't skip your medications. If you stop, depression symptoms may come back, and you could also experience withdrawal-like symptoms. Recognize that it will take time to feel better.

                    2) Learn about depression. Education about your condition can empower you and motivate you to stick to your treatment plan. Encourage your family to learn about depression to help them understand and support you.

                    3) Pay attention to warning signs. Work with your doctor or therapist to learn what might trigger your depression symptoms. Make a plan so that you know what to do if your symptoms get worse. Contact your doctor or therapist if you notice any changes in symptoms or how you feel. Ask relatives or friends to help watch for warning signs.

                    4) Avoid alcohol and recreational drugs. It may seem like alcohol or drugs lessen depression symptoms, but in the long run they generally worsen symptoms and make depression harder to treat. Talk with your doctor or therapist if you need help with alcohol or substance use.

                    5) Take care of yourself. Eat healthy, be physically active and get plenty of sleep. Consider walking, jogging, swimming, gardening or another activity that you enjoy. Sleeping well is important for both your physical and mental well-being. If you're having trouble sleeping, talk to your doctor about what you can do.

'''

        return render_template('index.html', data = input, pred= pred, desc = desc)         
         

if __name__ == '__main__':
    app.run(use_reloader=True)