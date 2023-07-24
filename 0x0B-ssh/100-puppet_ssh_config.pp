# Changes SSH config file
exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/id_rsa\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
