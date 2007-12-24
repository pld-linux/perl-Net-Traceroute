#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
			# require traceroute program access
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Traceroute
Summary:	Net::Traceroute - traceroute(1) functionality in Perl
Summary(pl.UTF-8):	Net::Traceroute - traceroute(1) dla Perla
Name:		perl-Net-Traceroute
Version:	1.10
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9344803cd997071b23136d39877005d
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
