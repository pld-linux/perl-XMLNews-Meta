#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	XMLNews-Meta
Summary:	XMLNews::Meta Perl module - for reading and writing XMLNews metadata files
Summary(pl):	Modu³ Perla XMLNews::Meta - odczyt i zapis plików z metadanymi XMLNews
Name:		perl-XMLNews-Meta
Version:	0.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/DMEGG/%{pnam}-%{version}.tar.gz
# Source0-md5:	6b7dd68ce7e1d6e85e5ef250f3859360
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-XML-Parser >= 2.19
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XML-Parser >= 2.19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XMLNews::Meta module handles the import, export, and programmatic
manipulation of metadata for XMLNews resources. You can read or write
a metadata file using a single method call, and can easily add or
remove values.

%description -l pl
Modu³ XMLNews::Meta obs³uguje import, eksport i programow± obróbkê
metadanych dla zasobów XMLNews. Mo¿na odczytywaæ i zapisywaæ metadane
za pomoc± pojedynczego wywo³ania metody oraz ³atwo dodawaæ i usuwaæ
warto¶ci.

%prep
%setup -q -n %{pnam}-%{version}

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
%doc Changes README
%dir %{perl_vendorlib}/XMLNews
%{perl_vendorlib}/XMLNews/Meta.pm
%{_mandir}/man3/*
