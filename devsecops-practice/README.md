# DevSecOps Hands-On Practice

This is a safe, isolated learning workspace. The sample application uses only
Python's standard library, so you do not need to install application packages.

## Open only this folder in VS Code

1. Select **File > Open Folder**.
2. Open the `devsecops-practice` folder.
3. If VS Code asks about trust, confirm that the path ends in
   `devsecops-practice`, then choose **Trust Folder & Continue**.

Trusting this small folder does not trust the rest of the repository.

## Learning path

### Lab 1: Run the application

Open a VS Code terminal and check Python:

```powershell
py -3 --version
```

Start the application:

```powershell
py -3 app\app.py
```

Visit <http://localhost:8000> and <http://localhost:8000/health>. Stop the
application with `Ctrl+C`.

**DevOps lesson:** A health endpoint lets automation check whether an
application is running.

### Lab 2: Run an automated test

```powershell
py -3 -m unittest discover -s app -p "test_*.py" -v
```

**DevSecOps lesson:** Fast tests should run before packaging or deploying code.
A secure pipeline stops when a test fails.

### Lab 3: Practice secret protection

The local `.gitignore` excludes `.env`, which is a common place for local
credentials.

Create a file containing only a fake value:

```powershell
Set-Content .env 'DEMO_PASSWORD=not-a-real-password'
git status --short
```

The `.env` file should not appear in Git's output. Remove it after the lab:

```powershell
Remove-Item .env
```

Never use a real password, token, or cloud key in a training file.

**Security lesson:** `.gitignore` reduces accidental commits, but secret
scanning is still needed because ignore rules can be bypassed.

### Lab 4: Review the secure container

Open `Dockerfile` and find these controls:

- A small base image
- A non-root user
- A health check
- Only the required application files copied into the image

If Docker or Podman is available, build and run it:

```powershell
docker build -t devsecops-practice .
docker run --rm -p 8000:8000 devsecops-practice
```

For Podman, replace `docker` with `podman`.

**Security lesson:** Running as non-root limits the damage if an application is
compromised.

### Lab 5: Review Kubernetes security

Open `kubernetes\deployment.yaml`. Identify:

- `runAsNonRoot`
- `allowPrivilegeEscalation: false`
- A read-only root filesystem
- Dropped Linux capabilities
- CPU and memory limits
- Liveness and readiness checks

Check its client-side syntax if `kubectl` is installed:

```powershell
kubectl apply --dry-run=client -f kubernetes\deployment.yaml
```

**Security lesson:** Container security must also be enforced where the
container runs.

### Lab 6: Review Infrastructure as Code

Open `terraform\main.tf`. It describes an encrypted S3 bucket with public
access blocked and versioning enabled.

If Terraform is installed:

```powershell
terraform -chdir=terraform fmt -check
terraform -chdir=terraform init
terraform -chdir=terraform validate
```

Do not run `terraform apply` for this lab. Applying it would attempt to create
real AWS resources and could cost money.

**DevSecOps lesson:** Infrastructure should be reviewed and scanned before it
is created.

### Lab 7: Understand the pipeline

Open `pipeline\ci.yml`. Read the jobs from top to bottom:

1. Check out the repository.
2. Run application tests.
3. Scan for secrets.
4. Scan the container definition.
5. Scan Terraform configuration.

This file is a learning example. It is stored outside `.github\workflows`, so
GitHub will not execute it automatically.

## Recommended order after this workspace

1. Git and secret scanning
2. Application testing and SAST
3. Dependency scanning
4. Container security
5. Infrastructure as Code scanning
6. Kubernetes security
7. CI/CD pipeline integration
