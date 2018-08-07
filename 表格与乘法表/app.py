from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'books': [
            {
                'name': '西游记',
                'author': '吴承恩'
            },
            {
                'name': '三国演义',
                'author': '罗贯中'
            },
            {
                'name': '水浒传',
                'author': '施耐庵'
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹'
            }
        ]
    }
    return render_template('index.html', **context)
