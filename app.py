from flask import Flask, request, jsonify, render_template
import openai
import os
import zipfile

app = Flask(__name__)

openai.api_key = "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"

def download_kaggle_dataset():
    dataset_file_path = 'simple-dialogs-for-chatbot.zip'
    if not os.path.exists(dataset_file_path):
        os.system('kaggle datasets download -d grafstor/simple-dialogs-for-chatbot')
       
        with zipfile.ZipFile(dataset_file_path, 'r') as zip_ref:
            zip_ref.extractall('kaggle_dataset')

download_kaggle_dataset()


dataset_file_path = 'simple-dialogs-for-chatbot.zip' 
with open(dataset_file_path, 'r') as file:
    dataset_text = file.read()


dataset_records = dataset_text.split('\n')


dataset_list = []

for record in dataset_records:
    parts = record.split(': ')
    if len(parts) == 2:
        column_name = parts[0].strip()
        column_value = parts[1].strip()
        dataset_list.append((column_name, column_value))

@app.route('/favicon.ico')
def favicon():
    return '', 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    if "Retrieve information for index" in user_message:
        index = int(user_message.split()[-1])
        if 0 <= index < len(dataset_list):
            response = dataset_list[index][1]  
            response = response.strip()
        else:
            response = "Index out of range."
    else:
    
        response = generate_gpt_response(user_message)
        
    return jsonify({'message': response})

def generate_gpt_response(user_message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=50
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run()
from flask import Flask, request, jsonify, render_template
import openai
import os
import zipfile

app = Flask(__name__)

openai.api_key = "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"

def download_kaggle_dataset():
    dataset_file_path = 'simple-dialogs-for-chatbot.zip'
    if not os.path.exists(dataset_file_path):
        os.system('kaggle datasets download -d grafstor/simple-dialogs-for-chatbot')
      
        with zipfile.ZipFile(dataset_file_path, 'r') as zip_ref:
            zip_ref.extractall('kaggle_dataset')

download_kaggle_dataset()


dataset_file_path = 'simple-dialogs-for-chatbot.zip'  
with open(dataset_file_path, 'r') as file:
    dataset_text = file.read()


dataset_records = dataset_text.split('\n')


dataset_list = []

for record in dataset_records:
    parts = record.split(': ')
    if len(parts) == 2:
        column_name = parts[0].strip()
        column_value = parts[1].strip()
        dataset_list.append((column_name, column_value))

@app.route('/favicon.ico')
def favicon():
    return '', 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    if "Retrieve information for index" in user_message:
        index = int(user_message.split()[-1])
        if 0 <= index < len(dataset_list):
            response = dataset_list[index][1]  
            response = response.strip()
        else:
            response = "Index out of range."
    else:
        
        response = generate_gpt_response(user_message)
        
    return jsonify({'message': response})

def generate_gpt_response(user_message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=50
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run()