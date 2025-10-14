import os
import subprocess
import docker
from datetime import datetime

# Initialize Docker client
client = docker.from_env()

# Backup directory
BACKUP_DIR = "/tmp/docker_backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

def backup_docker():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    print(f"[INFO] Starting Docker backup at {timestamp}...")

    # Backup images
    for image in client.images.list():
        image_name = image.tags[0] if image.tags else image.short_id
        safe_name = image_name.replace("/", "_").replace(":", "_")
        file_path = os.path.join(BACKUP_DIR, f"{safe_name}_{timestamp}.tar")
        print(f"[BACKUP] Saving image {image_name} -> {file_path}")
        subprocess.run(["docker", "save", "-o", file_path, image_name], check=True)

    # Backup volumes
    volumes = client.volumes.list()
    for vol in volumes:
        vol_name = vol.name
        file_path = os.path.join(BACKUP_DIR, f"{vol_name}_{timestamp}.tar.gz")
        print(f"[BACKUP] Archiving volume {vol_name} -> {file_path}")
        subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{vol_name}:/data",
            "-v", f"{BACKUP_DIR}:/backup",
            "alpine",
            "sh", "-c",
            f"tar czf /backup/{vol_name}_{timestamp}.tar.gz -C /data ."
        ], check=True)

    print("[INFO] Backup completed successfully.\n")

def troubleshoot_docker():
    print("[INFO] Running Docker troubleshooting checks...\n")

    # Check Docker service
    try:
        subprocess.run(["systemctl", "is-active", "--quiet", "docker"], check=True)
        print("[OK] Docker service is running.")
    except subprocess.CalledProcessError:
        print("[ERROR] Docker service is NOT running!")

    # List containers
    containers = client.containers.list(all=True)
    if containers:
        print(f"[INFO] Found {len(containers)} containers.")
        for c in containers:
            print(f" - {c.name} ({c.status})")
    else:
        print("[WARNING] No containers found.")

    # Check disk usage
    try:
        result = subprocess.check_output(["docker", "system", "df"]).decode()
        print("\n[INFO] Docker disk usage:\n")
        print(result)
    except Exception as e:
        print(f"[ERROR] Could not check disk usage: {e}")

    # Logs for unhealthy containers
    for c in containers:
        if c.attrs.get("State", {}).get("Health", {}).get("Status") == "unhealthy":
            print(f"[ALERT] Container {c.name} is UNHEALTHY! Last logs:")
            logs = c.logs(tail=10).decode()
            print(logs)

    print("\n[INFO] Troubleshooting finished.\n")

if __name__ == "__main__":
    print("==== Docker Backup & Troubleshooting ====")
    backup_docker()
    troubleshoot_docker()
