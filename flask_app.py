import json
from flask import Flask, make_response, request, render_template, send_file
from datetime import datetime
import x


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

    name = str(datetime.now()) + ".svg"
    name = name.replace(":", "")
    string = ""
   
    for i in range(0,len(data)):
        string += str(data[i]['entity'] + '\n')
        attributes = ','.join(data[i]['attributes'])
        # attributes = attributes.replace('(','1(')
        if i!=len(data)-1:
            string += str(attributes + '\n')
        else:
            string += str(attributes)


    # print(string)
    try:
        dwg = x.begin(string)
        dwg.save()
        response = make_response(dwg.tostring())
        response.headers['Content-Type'] = 'image/svg+xml'
        response.headers['Content-Disposition'] = 'attachment; filename=example.svg'

        return response
    
    except Exception as e :
        string = string.replace('\n','\\n')
        if("Arrow" in e.args[0]):
            return render_template('error.html',error=string , e=e)
        else:
            return render_template('error.html',error=string,e='null')
        # return """There is a missing arrow destination/source, please go back double check all arrows<br><br><br>This is your code copy it:<br><br><br>"""+string



    

    # return send_file(name, mimetype='image/svg+xml', as_attachment=True)






    return 'Data successfully converted and saved to input.txt'

if __name__ == '__main__':
    app.run(host='port=5000',debug=True)
