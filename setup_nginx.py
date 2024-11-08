import os
import subprocess
import sys
from dotenv import load_dotenv

load_dotenv()

DOMAIN_NAME = os.getenv("DOMAIN_NAME")
EMAIL = os.getenv("EMAIL")
WEBSITE_PORT = os.getenv("WEBSITE_PORT")
CLOCK_PORT = os.getenv("CLOCK_PORT")


if not all([DOMAIN_NAME, EMAIL, WEBSITE_PORT, CLOCK_PORT]):
    print("set .env file with DOMAIN_NAME, EMAIL, WEBSITE_PORT, CLOCK_PORT")
    sys.exit(1)

nginx_conf_path = "./nginx.conf"
nginx_server_path = f"/etc/nginx/sites-available/{DOMAIN_NAME}"


def install_packages():
    print("Installing Nginx and Certbot...")
    subprocess.run("sudo apt update && sudo apt install -y nginx certbot python3-certbot-nginx", shell=True)


def configure_nginx():
    print("Configuring Nginx...")
    with open(nginx_conf_path, "r") as file:
        config = file.read()
        config = config.replace("{{domain_name}}", DOMAIN_NAME)
        config = config.replace("{{website_port}}", WEBSITE_PORT)
        config = config.replace("{{clock_port}}", CLOCK_PORT)

    with open(nginx_server_path, "w") as file:
        file.write(config)

    subprocess.run(f"sudo ln -s {nginx_server_path} /etc/nginx/sites-enabled/", shell=True)
    subprocess.run("sudo nginx -t && sudo systemctl reload nginx", shell=True)


def setup_ssl():
    print("Setting up SSL with Certbot...")
    subprocess.run(
        f"sudo certbot --nginx -d {DOMAIN_NAME} -d www.{DOMAIN_NAME} -d app1.{DOMAIN_NAME} -d app2.{DOMAIN_NAME}"
        f" --non-interactive --agree-tos -m {EMAIL}",
        shell=True)


install_packages()
configure_nginx()
setup_ssl()
print("Nginx setup and SSL configuration complete!")
