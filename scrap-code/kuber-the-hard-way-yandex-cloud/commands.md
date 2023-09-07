# yc

<code>yc iam key create --service-account-name [service-account-name] --output key.json</code>
<code>yc config profile create [profile-name]</code>
<code>yc config set service-account-key key.json</code>
<code>yc resource-manager folder list</code>
<code>yc iam service-account list</code>
<code>yc iam service-account create --name [service-account-name]</code>
<pre>
# for setting authenticated data in PATH
export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id)
</pre>


for i in 0 1; do
  name=controller-${i}
  DNS_ZONE_ID=$(yc dns zone get kubernetes --format json | jq '.id' -r)
  INTERNAL_SG=$(yc vpc security-group get kubernetes-the-hard-way-allow-internal --format json | jq '.id' -r)
  EXTERNAL_SG=$(yc vpc security-group get kubernetes-the-hard-way-external-allow --format json | jq '.id' -r)
  BALANCER_SG=$(yc vpc security-group get kubernetes-the-hard-way-balancer-allow --format json | jq '.id' -r)
  yc compute instance create \
    --name ${name} \
    --zone ru-central1-a \
    --cores 2 \
    --memory 8 \
    --network-interface security-group-ids=\[${INTERNAL_SG},${EXTERNAL_SG},${BALANCER_SG}\],subnet-name=kubernetes,nat-ip-version=ipv4,ipv4-address=10.240.0.1${i},dns-record-spec=\{name=${name}.,dns-zone-id=${DNS_ZONE_ID},ttl=300\} \
    --create-boot-disk type=network-ssd,image-id=[<image_id>],size=100 \
    --ssh-key ~/sshkeys/key.pub \
    --labels role=controller \
    --hostname ${name} \
    --async
done


NETWORK_ID=$(yc vpc network get kubernetes-the-hard-way --format json | jq '.id' -r)
yc dns zone create --name=kubernetes --zone=. --private-visibility=true --network-ids=${NETWORK_ID}


DNS_ZONE_ID=$(yc dns zone get kubernetes --format json | jq '.id' -r)
  INTERNAL_SG=$(yc vpc security-group get kubernetes-the-hard-way-allow-internal --format json | jq '.id' -r)
  EXTERNAL_SG=$(yc vpc security-group get kubernetes-the-hard-way-external-allow --format json | jq '.id' -r)
  BALANCER_SG=$(yc vpc security-group get kubernetes-the-hard-way-balancer-allow --format json | jq '.id' -r)


for i in 0 1; do
  name=worker-${i}
  DNS_ZONE_ID=$(yc dns zone get kubernetes --format json | jq '.id' -r)
  INTERNAL_SG=$(yc vpc security-group get kubernetes-the-hard-way-allow-internal --format json | jq '.id' -r)
  EXTERNAL_SG=$(yc vpc security-group get kubernetes-the-hard-way-external-allow --format json | jq '.id' -r)
  yc compute instance create \
    --name ${name} \
    --zone ru-central1-a \
    --cores 2 \
    --memory 8 \
    --network-interface security-group-ids=\[${INTERNAL_SG},${EXTERNAL_SG}\],subnet-name=kubernetes,nat-ip-version=ipv4,ipv4-address=10.240.0.2${i},dns-record-spec=\{name=${name}.,dns-zone-id=${DNS_ZONE_ID},ttl=300\} \
    --create-boot-disk type=network-hdd,image-id=[<image_id>],size=100 \
    --ssh-key ~/sshkeys/key.pub \
    --labels role=worker \
    --metadata pod-cidr=10.200.${i}.0/24 \
    --hostname ${name} \
    --async
done


### Admin cert
cat > admin-csr.json <<EOF
{
  "CN": "admin",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "US",
      "L": "Portland",
      "O": "system:masters",
      "OU": "Kubernetes The Hard Way",
      "ST": "Oregon"
    }
  ]
}
EOF

cfssl gencert \
  -ca=../ca.pem \
  -ca-key=../ca-key.pem \
  -config=../ca-config.json \
  -profile=kubernetes \
  admin-csr.json | cfssljson -bare admin


### Kubelet

for instance in worker-0 worker-1; do
cat > ${instance}-csr.json <<EOF
{
  "CN": "system:node:${instance}",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "US",
      "L": "Portland",
      "O": "system:nodes",
      "OU": "Kubernetes The Hard Way",
      "ST": "Oregon"
    }
  ]
}
EOF

EXTERNAL_IP=$(yc compute instance get ${instance} --format json | jq '.network_interfaces[0].primary_v4_address.one_to_one_nat.address' -r)

INTERNAL_IP=$(yc compute instance get ${instance} --format json | jq '.network_interfaces[0].primary_v4_address.address' -r)

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -hostname=${instance},${EXTERNAL_IP},${INTERNAL_IP} \
  -profile=kubernetes \
  ${instance}-csr.json | cfssljson -bare ${instance}
done

### Controller Manager

cat > kube-controller-manager-csr.json <<EOF
{
  "CN": "system:kube-controller-manager",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "US",
      "L": "Portland",
      "O": "system:kube-controller-manager",
      "OU": "Kubernetes The Hard Way",
      "ST": "Oregon"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=kubernetes \
  kube-controller-manager-csr.json | cfssljson -bare kube-controller-manager


### Kube proxy

cat > kube-proxy-csr.json <<EOF
{
  "CN": "system:kube-proxy",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "US",
      "L": "Portland",
      "O": "system:node-proxier",
      "OU": "Kubernetes The Hard Way",
      "ST": "Oregon"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=kubernetes \
  kube-proxy-csr.json | cfssljson -bare kube-proxy



### API keys

KUBERNETES_PUBLIC_ADDRESS=$(yc vpc address get kubernetes-hard-way-address --format json | jq '.external_ipv4_address.address' -r)

KUBERNETES_HOSTNAMES=kubernetes,kubernetes.default,kubernetes.default.svc,kubernetes.default.svc.cluster,kubernetes.svc.cluster.local

cat > kubernetes-csr.json <<EOF
{
  "CN": "kubernetes",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "US",
      "L": "Portland",
      "O": "Kubernetes",
      "OU": "Kubernetes The Hard Way",
      "ST": "Oregon"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -hostname=10.32.0.1,10.240.0.10,10.240.0.11,10.240.0.12,${KUBERNETES_PUBLIC_ADDRESS},127.0.0.1,${KUBERNETES_HOSTNAMES} \
  -profile=kubernetes \
  kubernetes-csr.json | cfssljson -bare kubernetes




### Service accounts


cat > service-account-csr.json <<EOF
{
  "CN": "service-accounts",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "US",
      "L": "Portland",
      "O": "Kubernetes",
      "OU": "Kubernetes The Hard Way",
      "ST": "Oregon"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=kubernetes \
  service-account-csr.json | cfssljson -bare service-account




## Certs distribution

for instance in worker-0 worker-1; do
  EXTERNAL_IP=$(yc compute instance get ${instance} --format json | jq '.network_interfaces[0].primary_v4_address.one_to_one_nat.address' -r)
  for filename in ca.pem ${instance}.pem ${instance}-key.pem; do
    scp -i ../sshkeys/key $filename yc-user@$EXTERNAL_IP:~/
  done
done



for instance in controller-0 controller-1; do
  EXTERNAL_IP=$(yc compute instance get ${instance} --format json | jq '.network_interfaces[0].primary_v4_address.one_to_one_nat.address' -r)
  for filename in ca.pem ca-key.pem kubernetes-key.pem kubernetes.pem service-account-key.pem service-account.pem; do
    scp -i ../sshkeys/key $filename yc-user@$EXTERNAL_IP:~/
  done
done
