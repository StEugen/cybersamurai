resource "yandex_vpc_subnet" "<resource address prefix>" {
  name           = "<name>"
  description    = "<description>"
  v4_cidr_blocks = ["<ips>"]
  zone           = "<zone>"
  network_id     = "<net_id>"
}

resource "yandex_vpc_security_group" "<prefix>"{
  name = "<name>"
  description = "<description>"
  network_id = var.network_id

  ingress {
    protocol = "ANY"
    description = "rule to allow internal communication using any protocol"
    v4_cidr_blocks = ["<ips>"]
    from_port = 0
    to_port = 65535
  }

}

