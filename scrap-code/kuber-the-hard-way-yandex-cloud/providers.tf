terraform {

  backend "local" {
    workspace_dir = "state"
  }

  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"

}

provider "yandex" {
  zone      = "<zone>"
}
