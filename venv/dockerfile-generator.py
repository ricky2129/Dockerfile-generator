import argparse
import os

def generate_dockerfile(base_image, command, port):
    content = f"""
    FROM {base_image}
    CMD {command}
    EXPOSE {port}
    """
    with open("Dockerfile", "w") as f:
        f.write(content.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dockerfile Generator")
    parser.add_argument("--base", required=True, help="Base image")
    parser.add_argument("--cmd", required=True, help="Command to run")
    parser.add_argument("--port", type=int, default=80, help="Port to expose")

    args = parser.parse_args()
    generate_dockerfile(args.base, args.cmd, args.port)
