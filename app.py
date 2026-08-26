from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sandeep - Cloud & DevOps Engineer</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 60px auto;
                padding: 30px;
                line-height: 1.7;
            }

            h1 {
                font-size: 42px;
            }

            h2 {
                font-size: 28px;
            }

            .skills {
                font-weight: bold;
            }

            .tag {
                display: inline-block;
                padding: 8px 14px;
                margin: 5px;
                border: 1px solid #ccc;
                border-radius: 20px;
            }
        </style>
    </head>

    <body>

        <h1>Hi, I'm Sandeep 👋</h1>

        <h2>Cloud & DevOps Engineer</h2>

        <p>
            I'm Sandeep, a Cloud & DevOps enthusiast passionate about
            cloud infrastructure, automation, containerization, and
            continuous delivery.
        </p>

        <p>
            I work with technologies including AWS, Docker, Kubernetes,
            Terraform, Linux, Git, and CI/CD. I enjoy turning applications
            into reliable, scalable, and automated cloud deployments.
        </p>

        <p>
            Currently, I'm focused on strengthening my expertise in AWS
            and DevOps while building real-world projects and preparing
            for a career in Cloud Engineering and DevOps.
        </p>

        <h2>☁️ Technologies</h2>

        <div class="skills">
            <span class="tag">AWS</span>
            <span class="tag">Docker</span>
            <span class="tag">Kubernetes</span>
            <span class="tag">Terraform</span>
            <span class="tag">Linux</span>
            <span class="tag">Git</span>
            <span class="tag">CI/CD</span>
            <span class="tag">Python</span>
        </div>

        <h2>🚀 My DevOps Journey</h2>

        <p>
            Learning → Building → Automating → Deploying
        </p>

        <p>
            This application is containerized with Docker and deployed
            on Amazon EKS using Kubernetes and automated CI/CD with
            GitHub Actions.
        </p>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
