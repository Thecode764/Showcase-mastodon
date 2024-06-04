from flask import Flask, render_template, request

from mastodon import Mastodon

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
       access_token = request.form.get("access_token")
       project_name = request.form.get("project_name")
       project_description = request.form.get("project_description")
       project_source_url = request.form.get("project_source_url")
       base_url = request.form.get("base_url")
       mastodon = Mastodon(
           access_token=access_token,
           api_base_url=base_url
       )
       mastodon.status_post(f"""Hi 👋 

I have new project ❤️ 

💻 {project_name} 💻 
----------------------------------------------
{project_description}
🌐 Source 🌐 
{project_source_url}

Power by Showcase bot""")
       return render_template("post.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)