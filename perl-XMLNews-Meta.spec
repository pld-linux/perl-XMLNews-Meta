#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	XMLNews-Meta
Summary:	XMLNews::Meta Perl module - for reading and writing XMLNews metadata files
Summary(pl.UTF-8):	Moduł Perla XMLNews::Meta - odczyt i zapis plików z metadanymi XMLNews
Name:		perl-XMLNews-Meta
Version:	0.01
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DM/DMEGG/%{pnam}-%{version}.tar.gz
# Source0-md5:	6b7dd68ce7e1d6e85e5ef250f3859360
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Moduł XMLNews::Meta obsługuje import, eksport i programową obróbkę
metadanych dla zasobów XMLNews. Można odczytywać i zapisywać metadane
za pomocą pojedynczego wywołania metody oraz łatwo dodawać i usuwać
wartości.

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
