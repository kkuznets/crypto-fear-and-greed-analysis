terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
    credentials = ""
    region = ""
    zone = ""
}

