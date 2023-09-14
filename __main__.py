from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    return render_template_string(
        """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Telegram Auth Demo</title>
    </head>
    <body>
        <button onclick="window.location.href='http://oauth.telegram.org/auth?bot_id=6599087218&origin=http://43.153.207.126:8085&request_access=write&return_to=http://43.153.207.126:8085/test'">
            Login with Telegram
        </button>
    </body>
    </html
    """
    )


@app.route("/test")
def test():
    html_content = """
    <html>
    <head>
        <title>My Page</title>
    </head>
    <body>
        <h1>Welcome to My Page</h1>
        <p>This is a simple HTML page.</p>
        <script async src="https://telegram.org/js/telegram-widget.js?22" data-telegram-login="TaskOn_st_telegram_bot" data-size="large" data-onauth="onTelegramAuth(user)" data-request-access="write"></script>

        <script type="text/javascript">
        function onTelegramAuth(user) {
            alert('Logged in as ' + user.auth_date + ' ' + user.hash + ' '+ user.photo_url + ' ' + user.first_name + ' ' + user.last_name + ' (' + user.id + (user.username ? ', @' + user.username : '') + ')');
        }
        </script>
    </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
