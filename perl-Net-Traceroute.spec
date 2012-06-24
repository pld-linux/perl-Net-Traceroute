%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Traceroute
Summary:	Net::Traceroute perl module
Summary(pl):	Modu� perla Net::Traceroute
Name:		perl-Net-Traceroute
Version:	1.07
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Net-ext
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Traceroute - traceroute(1) functionality in perl.

%description -l pl
Net::Traceroute - traceroute(1) dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net/Traceroute.pm
%{_mandir}/man3/*
