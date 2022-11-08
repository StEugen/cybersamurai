from crypt import methods
from flask import redirect
from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import send_file


app = Flask(__name__, template_folder='./template')

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        f = open('./sh-files/test.sh', 'w')
        checked =  request.form.getlist('check')
        print(checked)
        if "docker-ubuntu-22" in checked:
            text = [
                '#start of docker installation',
                'sudo apt-get update',
                'sudo apt install -y apt-transport-https ca-certificates curl software-properties-common',
                'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg',
                'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null',
                'sudo apt update',
                'sudo apt install -y docker-ce',
                '#end of docker installation'
            ]
            f.write('\n'.join(text))
            f.write('\n')
        if "portainer" in checked:
            text = [
                '#start of portainer in docker installation',
                'docker volume create portainer_data',
                'docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest',
                '#end of portainer in docker installation'
            ]
            f.write('\n'.join(text))
            f.write('\n')
        return redirect(url_for('download'))
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    path = './sh-files/test.sh'
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

