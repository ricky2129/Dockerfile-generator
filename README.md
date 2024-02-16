# Dockerfile-Generator
The Dockerfile Generator is a Python script designed to simplify the process of creating Dockerfiles for your containerized applications. By specifying parameters such as the base image, commands, ports, environment variables, and more, you can quickly generate a Dockerfile tailored to your needs.

## Features

* **Customizable Base Image**: Specify any base image for your Docker container.
* **Command Execution**: Define the default command or script the container should execute upon startup.
* **Port Exposing**: Expose ports for your application, making it accessible on specified network ports.
* **Environment Variables**: Set up environment variables required by your application.
* **Working Directory**: Set a working directory inside your container.
* **Build Commands**: Include any commands that need to be run during the image build process.
* **Entrypoint Configuration**: Define the entrypoint for your container.
* **File Copying**: Copy files or directories from your host to the container.
* **Volume Mounting**: Specify volumes to be mounted inside the container.
* **Labeling**: Add metadata labels to your Docker image.


## Usage

To use this script, you will need Python installed on your system. The script accepts command-line arguments for each Dockerfile component. Here's a basic example of how to use it:

```yaml
python dockerfile-generator.py --base ubuntu:latest --cmd "echo Hello, World!" --port 8080 --env MY_VAR=value --workdir /app --run "apt-get update;apt-get install -y curl" --copy "source:/dest" --volume "/data" --label "maintainer=example@example.com"
```

**Arguments**
<br>
- base: The base image for your Dockerfile (required)
- cmd: The default command to run in the container (required)
- port: The port to expose in the container
- env: Environment variables (semicolon-separated KEY=VALUE pairs)
- workdir: The working directory in the container
- run: Commands to execute during the build (semicolon-separated)
- entrypoint: Entrypoint for the container
- copy: Files or directories to copy (semicolon-separated 'src:dest' pairs)
- volume: Volumes to mount (semicolon-separated paths)
- label: Labels to apply (semicolon-separated KEY=VALUE pairs)

## Practical Applications
This script is particularly useful for developers who:
* Regularly build and deploy containerized applications and need a quick way to generate Dockerfiles.
* Prefer a scriptable, command-line approach to Dockerfile generation, integrating into automated build and deployment pipelines.
* Require a flexible tool to experiment with different Dockerfile configurations without manually editing files.


## Contribution
Contributions to enhance the script or add new features are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.
