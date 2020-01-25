#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
			# require traceroute program access
#
%define		pdir	Net
%define		pnam	Traceroute
Summary:	Net::Traceroute - traceroute(1) functionality in Perl
Summary(pl.UTF-8):	Net::Traceroute - traceroute(1) dla Perla
Name:		perl-Net-Traceroute
Version:	1.13
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a6d6b6c8b1210ac6cd9f610298d88425
URL:		http://search.cpan.org/dist/Net-Traceroute/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Net-ext
%if %{with test}
BuildRequires:	traceroute
%endif
Requires:	traceroute
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Traceroute - traceroute(1) functionality in Perl.

%description -l pl.UTF-8
Net::Traceroute - traceroute(1) dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/Net/Traceroute.pm
%{_mandir}/man3/*
