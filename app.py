# 文章发表时间过滤器
# handle_time
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        "uptime": datetime(2017, 8, 1, 9, 12, 0)
    }
    return render_template('index.html', **context)


@app.template_filter('handle_time')
def up_time(uptime):
    if isinstance(uptime, datetime):
        timestamp = datetime.now() - uptime
        time = timestamp.total_seconds()
        if time < 60:
            return "刚刚"
        elif time < 60 * 60:
            return "{}分钟前".format(int(time / 60))
        elif time < 60 * 60 * 24:
            return "{}小时前".format(int(time / (60 * 60)))
        elif time < 60 * 60 * 24 * 30:
            return "{}天前".format(int(time / (60 * 60 * 24)))
        else:
            return uptime.strftime('%Y/%m/%d %H:%M')

