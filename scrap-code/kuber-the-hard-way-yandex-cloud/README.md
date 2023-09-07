# kuber-the-hard-way-yandex-cloud

Nah, kinda a mess here, need to clean everything up...

Kubernetes the hard way in yandex cloud with Terraform, vault, packer and cloud-init.

## Cluster Details
- Kubernetes
- Terraform
- Vault
- Packer
- cloud-init

## Whole process

### Day 1

So, at day one, let's learn the whole stack that gonna be used.


- <a href='https://cloud.yandex.com/en-ru/docs/cli/quickstart'>yc cli</a>
- <a href='https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart'>yandex cloud tutorials</a>
- <a href='https://cloud.yandex.ru/docs/iam/quickstart-sa'>Service account creation</a>
- <a href='https://developer.hashicorp.com/terraform/cli/config/config-file#explicit-installation-method-configuration'>More about terraform config file</a>
- <a href='https://terraform-provider.yandexcloud.net//'>Provider docs</a>

BTW, if you use .terraform.lock.hcl (as i did), remember to execute <code>terraform providers lock -net-mirror=https://terraform-mirror.yandexcloud.net -platform=linux_amd64 -platform=darwin_arm64 yandex-cloud/yandex</code>, so the config could be used on different platforms (because when i was first creating it, i've created it only for linux, my bad), then run <code>terraform providers lock</code>



### Day 2
