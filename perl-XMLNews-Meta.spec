#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pnam	XMLNews-Meta
Summary:	XMLNews::Meta Perl module - for reading and writing XMLNews metadata files
Summary(pl):	Modu� Perla XMLNews::Meta - do odczytu i zapisu plik�w z metadanymi XMLNews
Name:		perl-XMLNews-Meta
Version:	0.01
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/DMEGG/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-Parser >= 2.19
BuildRequires:	rpm-perlprov >= 4.0.2-104
Requires:	perl-XML-Parser >= 2.19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XMLNews::Meta module handles the import, export, and programmatic
manipulation of metadata for XMLNews resources. You can read or write
a metadata file using a single method call, and can easily add or
remove values.

%description -l pl
Modu� XMLNews::Meta obs�uguje import, eksport i programow� obr�bk�
metadanych dla zasob�w XMLNews. Mo�na odczytywa� i zapisywa� metadane
za pomoc� pojedynczego wywo�ania metody oraz �atwo dodawa� i usuwa�
warto�ci.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitelib}/XMLNews
%{perl_sitelib}/XMLNews/Meta.pm
%{_mandir}/man3/*
