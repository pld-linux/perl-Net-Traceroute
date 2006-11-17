#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
			# require traceroute program access
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Traceroute
Summary:	Net::Traceroute perl module
Summary(pl):	Modu³ Perla Net::Traceroute
Name:		perl-Net-Traceroute
Version:	1.09
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f9b4d17c352984a507665798f0d5d7a
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
Net::Traceroute - traceroute(1) functionality in perl.

%description -l pl
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
%doc README
%{perl_vendorlib}/Net/Traceroute.pm
%{_mandir}/man3/*
