# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#    return "Hello World!"

# if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)



from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Demo - Vasanth</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
        }
        .container {
            text-align: center;
            padding: 3rem;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 25px 50px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 90%;
            animation: fadeIn 1s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .badge {
            display: inline-block;
            background: #00d9ff;
            color: #1a1a2e;
            padding: 0.5rem 1.5rem;
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 1.5rem;
            text-transform: uppercase;
        }
        h1 { font-size: 3rem; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        p { font-size: 1.2rem; opacity: 0.9; margin-bottom: 2rem; line-height: 1.6; }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 1rem;
            margin-top: 2rem;
        }
        .feature-card {
            background: rgba(255,255,255,0.15);
            padding: 1.5rem;
            border-radius: 12px;
            transition: transform 0.3s, background 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            background: rgba(255,255,255,0.25);
        }
        .feature-icon { font-size: 2rem; margin-bottom: 0.5rem; }
        .feature-title { font-size: 0.95rem; font-weight: 600; }
        .footer { margin-top: 2rem; font-size: 0.85rem; opacity: 0.7; }
        .pulse {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #00ff88;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(0,255,136,0.7); }
            70% { box-shadow: 0 0 0 10px rgba(0,255,136,0); }
            100% { box-shadow: 0 0 0 0 rgba(0,255,136,0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge"><span class="pulse"></span>Live CI/CD Pipeline</div>
        <h1>Hello Vasanth! 👋</h1>
        <p>Welcome to your fully automated deployment. This site was built, tested, and deployed using GitHub Actions + Docker.</p>
        <div class="features">
            <div class="feature-card"><div class="feature-icon">🐳</div><div class="feature-title">Docker</div></div>
            <div class="feature-card"><div class="feature-icon">⚡</div><div class="feature-title">GitHub Actions</div></div>
            <div class="feature-card"><div class="feature-icon">🧪</div><div class="feature-title">Pytest</div></div>
            <div class="feature-card"><div class="feature-icon">🚀</div><div class="feature-title">Auto Deploy</div></div>
        </div>
        <div class="footer">Built with ❤️ | Flask + Python | Deployed via CI/CD</div>
    </div>
</body>
</html>
"""

@app.route("/")
def hello():
    return render_template_string(HTML_PAGE)

@app.route("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
