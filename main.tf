#resource for K8s cluster creation
resource "digitalocean_kubernetes_cluster" "doks" {
  name   = "pumej-cluster"
  region = "nyc1"
  # Grab the latest version slug from `doctl kubernetes options versions`
  version = "1.28.2-do.0"
  node_pool {
    name       = "worker-pool"
    size       = "s-2vcpu-4gb"
    node_count = 3
  }
}

# Data source for our SSH key
data "digitalocean_ssh_key" "pumej-dokey" {
  name = "pumej"
}

# Creating a Digital Ocean Droplet
resource "digitalocean_droplet" "pumej-droplet" {
  image    = var.image
  name     = var.droplet_name
  region   = var.droplet_region
  size     = var.image_size
  ssh_keys = [data.digitalocean_ssh_key.pumej-dokey.id]
}