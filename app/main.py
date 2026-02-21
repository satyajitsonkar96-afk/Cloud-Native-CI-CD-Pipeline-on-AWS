@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cloud DevOps App</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Font Awesome for icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }
            .navbar {
                background: rgba(255,255,255,0.1) !important;
                backdrop-filter: blur(10px);
            }
            .hero {
                padding: 100px 0;
                color: white;
            }
            .card-custom {
                background: rgba(255,255,255,0.1);
                backdrop-filter: blur(5px);
                border: 1px solid rgba(255,255,255,0.2);
                color: white;
                transition: transform 0.3s;
            }
            .card-custom:hover {
                transform: translateY(-5px);
                background: rgba(255,255,255,0.2);
            }
            .btn-glass {
                background: rgba(255,255,255,0.2);
                border: 1px solid rgba(255,255,255,0.3);
                color: white;
                backdrop-filter: blur(5px);
            }
            .btn-glass:hover {
                background: rgba(255,255,255,0.3);
                color: white;
            }
            .footer {
                background: rgba(0,0,0,0.3);
                color: white;
                padding: 20px 0;
                margin-top: 50px;
            }
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand" href="/">
                    <i class="fas fa-cloud-upload-alt"></i> Cloud DevOps App
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="/">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/health">Health</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/info">Info</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/metrics">Metrics</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="hero text-center">
            <div class="container">
                <h1 class="display-4 fw-bold">🚀 Cloud DevOps App</h1>
                <p class="lead">Deployed using Jenkins CI/CD on AWS | Version 1.0</p>
                <div class="mt-4">
                    <a href="/health" class="btn btn-glass btn-lg me-2"><i class="fas fa-heartbeat"></i> Health Check</a>
                    <a href="/info" class="btn btn-glass btn-lg"><i class="fas fa-info-circle"></i> App Info</a>
                </div>
            </div>
        </section>

        <!-- Feature Cards -->
        <div class="container">
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card card-custom h-100">
                        <div class="card-body text-center">
                            <i class="fas fa-code-branch fa-3x mb-3"></i>
                            <h5 class="card-title">CI/CD Pipeline</h5>
                            <p class="card-text">Automated build, test, and deployment using Jenkins.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card card-custom h-100">
                        <div class="card-body text-center">
                            <i class="fas fa-cloud fa-3x mb-3"></i>
                            <h5 class="card-title">Cloud Native</h5>
                            <p class="card-text">Hosted on AWS with auto-scaling and load balancing.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card card-custom h-100">
                        <div class="card-body text-center">
                            <i class="fas fa-shield-alt fa-3x mb-3"></i>
                            <h5 class="card-title">Observability</h5>
                            <p class="card-text">Real-time metrics, health checks, and logging.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Author Card -->
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card card-custom">
                        <div class="card-body text-center">
                            <i class="fas fa-user-circle fa-4x mb-3"></i>
                            <h4>Satyajit Sonkar</h4>
                            <p class="mb-2">DevOps Engineer | Cloud Enthusiast</p>
                            <div>
                                <span class="badge bg-light text-dark">Version 1.0</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <footer class="footer text-center">
            <div class="container">
                <p class="mb-0">&copy; 2025 Cloud DevOps App. All rights reserved.</p>
            </div>
        </footer>

        <!-- Bootstrap JS (for navbar toggle) -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
