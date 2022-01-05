# Let’s practice using Puppet to make
# changes to our configuration file.
# Just as in the previous configuration
# file task, we’d like you to set up your
# client SSH configuration file so that you
# can connect to a server without typing a password.
#
#   Your SSH client configuration must be
# configured to use the private key ~/.ssh/school
#   Your SSH client configuration must be
# configured to refuse to authenticate using a password

file_line { 'Declare identity file':
path    => '/etc/ssh/ssh_config',
line    => '    IdentityFile ~/.ssh/school',
replace => true,
}

file_line { 'Turn off passwd auth':
path    => '/etc/ssh/ssh_config',
line    => '    PasswordAuthentication no',
replace => true,
}
