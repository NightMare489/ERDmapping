from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/convert', methods=['POST'])
def convert():
    entity_names = request.form.getlist('entity')
    attribute_lists = request.form.getlist('attributes')

    data = []

    for i in range(len(entity_names)):
        entity = {}
        entity['entity'] = entity_names[i]
        entity['attributes'] = [attr.strip() for attr in attribute_lists[i].split(',')]
        data.append(entity)

    data_json = json.dumps(data)

    with open('input.txt', 'w') as f:
        for entity in data:
            f.write(entity['entity'] + '\n')
            attributes = ','.join(entity['attributes'])
            attributes = attributes.replace('(','1(')
            f.write(attributes + '\n')

    return 'Data successfully converted and saved to input.txt'

if __name__ == '__main__':
    app.run(host='port=5000',debug=True)
