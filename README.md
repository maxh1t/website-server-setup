# Website Server Setup

This repository provides an automated setup for configuring Nginx to handle a main domain and multiple subdomains, each routing to separate applications on specified ports.

### Prerequisites

- **VPS with root access**
- **Operating System**: This setup assumes you are using a Linux-based OS, preferably **Ubuntu 20.04** or later.
- **Python 3**: Required to run the setup script

### Usage

1. **Copy** the example environment file to `.env` and fill in your values:

```bash
cp .env.example .env
```

2**Run the setup script**:

```bash
sudo python3 setup_nginx.py
```
