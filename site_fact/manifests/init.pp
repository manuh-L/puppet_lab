class site_fact {
  $fact_dir = ['/etc/puppetlabs/facter', '/etc/puppetlabs/facter/facts.d',]

  file { $fact_dir:
    ensure => 'directory',
  }

  file { '/etc/puppetlabs/facter/facts.d/site.py':
    source => 'puppet:///modules/site_fact/site.py',
    owner  => 'root',
    group  => 'root',
    mode   => '0755',
  }
}
