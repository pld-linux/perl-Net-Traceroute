#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
			# require traceroute program access
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Traceroute
Summary:	Net::Traceroute perl module
Summary(pl):	Modu³ perla Net::Traceroute
Name:		perl-Net-Traceroute
Version:	1.07
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6423aaa1798b60bc4c558710d5283581
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Net-ext
%if %{with test}
BuildRequires:	traceroute
%endif
Requires:	traceroute
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net/Traceroute.pm
%{_mandir}/man3/*
