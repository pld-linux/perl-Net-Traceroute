%include	/usr/lib/rpm/macros.perl
Summary:	Net-Traceroute perl module
Summary(pl):	Modu³ perla Net-Traceroute
Name:		perl-Net-Traceroute
Version:	1.03
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Traceroute-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Net-ext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Traceroute - traceroute(1) functionality in perl.

%description -l pl
Net-Traceroute - traceroute(1) dla perla.

%prep
%setup -q -n Net-Traceroute-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Traceroute.pm
%{_mandir}/man3/*
