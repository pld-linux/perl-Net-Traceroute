%include	/usr/lib/rpm/macros.perl
Summary:	Net-Traceroute perl module
Summary(pl):	Modu� perla Net-Traceroute
Name:		perl-Net-Traceroute
Version:	1.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Traceroute-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Net-ext
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Traceroute - traceroute(1) functionality in perl.

%description -l pl
Net-Traceroute - traceroute(1) dla perla.

%prep
%setup -q -n Net-Traceroute-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/Traceroute
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Net/Traceroute.pm
%{perl_sitearch}/auto/Net/Traceroute

%{_mandir}/man3/*
