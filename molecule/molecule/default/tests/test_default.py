
import pytest
import warnings
import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('webservers')

@pytest.mark.parametrize("name,version", [
    ("epel-release", "9"),
    ("htop", "3.3"),
    ("httpd", "2.4.57"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)

@pytest.mark.parametrize("user,group", [
    ("webapp", "webapp"),
])
def test_users(host, user, group):
    usr = host.user(user)
    assert usr.exists
    assert usr.group == group

def test_httpd_port(host):
    host.socket("tcp://:::80").is_listening    

def test_httpd_live(host):
    cmd = "curl localhost"
    run = host.run(cmd)
    assert run.rc == 0
    assert "welcome to my web server" in run.stdout    

@pytest.mark.parametrize("filename,owner,group,mode", [
    ("/opt/webapp/app.conf", "webapp", "webapp", 0o755),
])
def test_file(host, filename, owner, group, mode):
    target = host.file(filename)
    assert target.exists
    assert target.user == owner
    assert target.group == group
    assert target.mode == mode
