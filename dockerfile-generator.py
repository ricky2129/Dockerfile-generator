import argparse

def generate_dockerfile(base, cmd, port=None, env=None, workdir=None, run=None, entrypoint=None, copy=None, volume=None, label=None):
    dockerfile_lines = [f"FROM {base}"]
    
    if workdir:
        dockerfile_lines.append(f"WORKDIR {workdir}")
    
    if env:
        for env_var in env.split(';'):
            dockerfile_lines.append(f"ENV {env_var}")
    
    if run:
        for run_cmd in run.split(';'):
            dockerfile_lines.append(f"RUN {run_cmd}")
    
    if copy:
        for copy_cmd in copy.split(';'):
            src, dest = copy_cmd.split(':')
            dockerfile_lines.append(f"COPY {src} {dest}")
    
    if volume:
        for volume_path in volume.split(';'):
            dockerfile_lines.append(f"VOLUME {volume_path}")
    
    if entrypoint:
        dockerfile_lines.append(f"ENTRYPOINT {entrypoint}")
    
    if port:
        dockerfile_lines.append(f"EXPOSE {port}")
    
    if label:
        for label_entry in label.split(';'):
            dockerfile_lines.append(f"LABEL {label_entry}")
    
    dockerfile_lines.append(f'CMD {cmd}')
    
    dockerfile_content = "\n".join(dockerfile_lines)
    
    with open("Dockerfile", "w") as dockerfile:
        dockerfile.write(dockerfile_content)
        print("Dockerfile generated successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dockerfile Generator Script")
    parser.add_argument("--base", required=True, help="The base image for the Dockerfile")
    parser.add_argument("--cmd", required=True, help="The default command to run in the container")
    parser.add_argument("--port", help="The port to expose in the container", type=int)
    parser.add_argument("--env", help="Environment variables to set in the container (semicolon-separated KEY=VALUE pairs)")
    parser.add_argument("--workdir", help="The working directory in the container")
    parser.add_argument("--run", help="Commands to execute during the build (semicolon-separated)")
    parser.add_argument("--entrypoint", help="Entrypoint for the container")
    parser.add_argument("--copy", help="Files or directories to copy into the container (semicolon-separated 'src:dest' pairs)")
    parser.add_argument("--volume", help="Volumes to mount in the container (semicolon-separated paths)")
    parser.add_argument("--label", help="Labels to apply to the image (semicolon-separated KEY=VALUE pairs)")
    
    args = parser.parse_args()
    
    generate_dockerfile(args.base, args.cmd, args.port, args.env, args.workdir, args.run, args.entrypoint, args.copy, args.volume, args.label)
