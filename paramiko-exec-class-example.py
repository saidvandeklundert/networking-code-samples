import paramiko

class ssh_exec:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.login()

    def login(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, username=self.username,
                         password=self.password)

    def execute(self, command):
        (inp, outp, err) = self.ssh.exec_command(command)
        return outp.readlines()

    def logout(self):
        self.ssh.close()
