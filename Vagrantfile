# -*- mode: ruby -*-
# vi: set ft=ruby :
NUMBERWORKERS=4

$hostsfile_update = <<-'SCRIPT'
echo -e '192.168.5.1 control.example.com control\n192.168.5.1 node1.example.com node1\n192.168.5.2 node2.example.com node2\n192.168.5.3 node3.example.com node3\n192.168.5.4 node4.example.com node4' >> /etc/hosts
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "bento/debian-12"
  config.vm.synced_folder '.', '/vagrant', disabled: true
  # config.vm.network :forwarded_port, guest: 22, host: 2222

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 1024
    vb.cpus = 2
  end

  config.vm.provision "shell", privileged: true, inline: <<-SHELL
    timedatectl set-timezone Europe/Moscow
    sudo apt-get -y install nano curl tar wget nmon jq net-tools mc conntrack apt-transport-https ca-certificates zip unzip git lzma gpg python3 python3-pip kmod debian-archive-keyring tzdata software-properties-common lsb-release apt-transport-https apt-utils sudo coreutils --no-install-recommends
    echo "root:root" | chpasswd
    echo "vagrant:vagrant" | chpasswd
    useradd ansible
    echo "ansible:ansible" | chpasswd
    sudo mkdir /root/.ssh/
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAr53uTiK0O/sbacgMcsHGp2mL0XvjpxI9O6n2KOPduFbmwKF/ZxLZm6nR1K6Dkj5aeg+BEFft1lrkh08ubJCYkF7/5vXy5dlzlLokCwc3aEOIIxD2WsOaFizmiy/b3KE16bvpkM7WzydlW6LyTaF3BoAikiw5D5IibroSij2mFWGVieXxXJSyryu+xmsNqGywuKc+4DjoaqEJJooBU53OdTkg8RGeN4dCrEWbJIc7agl5MDaBpL8aO6vH4OuGM7u3UFCTgDe6KRlK+bgYs4QEqb55RiNIp0vAOET4jH2QBhP489+5R1V6B/ozx2n0rDo3F3Hrha2Cp835KGoJVl2Gmw== rsa-key-20211028" > /root/.ssh/authorized_keys2
    echo -e "-----BEGIN RSA PRIVATE KEY-----\nMIIEoAIBAAKCAQEAr53uTiK0O/sbacgMcsHGp2mL0XvjpxI9O6n2KOPduFbmwKF/\nZxLZm6nR1K6Dkj5aeg+BEFft1lrkh08ubJCYkF7/5vXy5dlzlLokCwc3aEOIIxD2\nWsOaFizmiy/b3KE16bvpkM7WzydlW6LyTaF3BoAikiw5D5IibroSij2mFWGVieXx\nXJSyryu+xmsNqGywuKc+4DjoaqEJJooBU53OdTkg8RGeN4dCrEWbJIc7agl5MDaB\npL8aO6vH4OuGM7u3UFCTgDe6KRlK+bgYs4QEqb55RiNIp0vAOET4jH2QBhP489+5\nR1V6B/ozx2n0rDo3F3Hrha2Cp835KGoJVl2GmwIBJQKCAQAJfiiOmheUih0oUACs\nQdNi/slJl/53u8v1YyIQDFEsjxNkW8Gyi2W1YyAZVYqSSI9E3j5T6RPGZccp6Jq5\nwqB2gaz3ukR7IILJxN9aisS5hxwdkjbUeUaZajX5r49YCLbOXS84Qogm34jwMlJJ\nYqx85FTlTn+f+g+y9U0cOq8IEwXq3gIijCd2BPXLix72a5IN954pYHrr1cE9kPoi\n/NXvsTVpTcMv1E+NmugBCFRRUy5qrHhWghQvIaehwYgEjDv5eRupe3DEEhcI4CzY\n8zciRq0XXZhn1KpgeLsQFGPmcrwpFLABKWLDWOo+KpDch3iVB9luih3HI0NIuUcn\n3KQdAoGBANQzOtVR5IhG4TpNhMqD19BlRQlL/rU4MxkTk+0VzTLqjzgaFg76KhWC\nqa7UYzOP4MfJr2zuzdB1NHWqcVUm4WvJzdviI6MMQOTIlOyCk7lEzcL8/b4Xp0kT\ncLGmyPVnVhCZlS/aTNLeLHeTUb+DuMPSShOqzblQIgB2ZNqKr82vAoGBANPdn/SL\nj1Bg7sFDWIZVztJQ/UeWwVEne3kf/AC2iyW4W4y63PRIhW1t6ig9Ce/5pdaxEGJ1\nitReiLUF/dy4t/X/QjfeqHDxibwM7+6DXM9q1TQY4gcOxicsGsI8O2J3c09iS9FX\niwQL4M62BL04tzyAFqFd5KJzn5vwoYpqO9zVAoGAPxYmP2tfniLpA37Uc476+MQp\nR/P/najsmMChmYMFp1p9mw6snKs88aNi4PMIvE1egJXoC6DxFHXfKeaQZWxsh9Q2\nSEomRTr+iTS2py29NxR0hhPcu/kxu8eCXlQt6BfNeo6GTH8rmKLqoBcKdzT/lCnC\n/u2XG2rZrRxHfz386h8CgYByhaKSBj+hEc0qMj2wZbvnTl9k94sXHEK+A3N2Ac6s\nmwENzMp2NQnaSUBNGhM1m7OWpOZDDxqcTsZvsDYyHqigpadAy2H33IHNbsbhyndb\nXFeRyELTYe6Rtvm1GaOPK8+giCj7iUQ5ieFNJB48xLYS3XQEMsDGg7A4nb8aYu/s\n/QKBgCiWdRFRyG0t03Kp8WsSAPkSa6KV/8bPS2IJc2Zgmt0KozHJUxTvfy3AD8ju\nGzKRJAaeseoBFxEJOPb5jRA+wGFhoykGssdejoroXdKI8JXxDzJiQqSYdx6kpo53\n4f0LxRpwmODaKdoKrGeMUNqBFPzrdVQ1R3DOtsGgbMZ1Lqj8\n-----END RSA PRIVATE KEY-----" > /root/.ssh/id_rsa
    chmod 600 /root/.ssh/id_rsa
    chmod 600 /root/.ssh/authorized_keys2
    mkdir -p /home/ansible/.ssh/
    cp /root/.ssh/id_rsa /home/ansible/.ssh/
    cp /root/.ssh/authorized_keys2 /home/ansible/.ssh/
    chown -R ansible /home/ansible/.ssh/
    cp /root/.ssh/id_rsa /home/vagrant/.ssh/
    cp /root/.ssh/authorized_keys2 /home/vagrant/.ssh/
    chown -R vagrant /home/vagrant/.ssh/
   
    sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
    sed -i 's/#PasswordAuthentication no/PasswordAuthentication no/g' /etc/ssh/sshd_config
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config

    sed -i "s|^#PermitRootLogin .*|PermitRootLogin yes|g" /etc/ssh/sshd_config
    systemctl restart sshd
    cat << "EOF" >> ~/.bashrc
    alias a='ansible'
    alias ap='ansible-playbook'
    alias ad='ansible-doc'
    HISTCONTROL=ignorespace:ignoredups:erasedups
    alias n='nano'
    alias m='molecule'
    alias cls='clear'
EOF

    mkdir -p ~/.config/pip
    echo '[global]\n break-system-packages = true' >> ~/.config/pip/pip.conf
    pip install setuptools pip 'molecule' pytest-testinfra molecule-plugins[docker] molecule-plugins[vagrant] molecule-lint flake8
    molecule --version
    apt update && apt install ansible ansible-lint --no-install-recommends -y
  SHELL
  config.vm.provision "shell", inline: $hostsfile_update  

  (1..NUMBERWORKERS).each do |i|
    config.vm.define "node#{i}" do |node|
      node.vm.hostname = "node#{i}"
      node.vm.network "private_network", ip: "192.168.5.#{i}"
      node.vm.network :forwarded_port, guest: 22, host: "22#{i}"
      node.vbguest.auto_update = false
    end
    
  end

end
