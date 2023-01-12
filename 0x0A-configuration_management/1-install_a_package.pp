# Using Puppet, install puppet-lint

node default {
  package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }
}
