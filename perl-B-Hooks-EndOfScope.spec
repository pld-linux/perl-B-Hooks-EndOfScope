#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	B
%define	pnam	Hooks-EndOfScope
Summary:	B::Hooks::EndOfScope - Execute code after a scope finished compilation
Summary(pl.UTF-8):	B::Hooks::EndOfScope - wykonywanie kodu po skompilowaniu zakresu kodu
Name:		perl-B-Hooks-EndOfScope
Version:	0.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/B/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	99a48be0694dfd12b40482c6a495e10f
URL:		https://metacpan.org/release/B-Hooks-EndOfScope
BuildRequires:	perl-ExtUtils-CBuilder >= 0.26
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Module-Implementation >= 0.05
BuildRequires:	perl-Sub-Exporter-Progressive >= 0.001006
BuildRequires:	perl-Test-Simple >= 0.89
BuildRequires:	perl-Variable-Magic >= 0.48
%endif
Requires:	perl-Module-Implementation >= 0.05
Requires:	perl-Module-Runtime >= 0.012
Requires:	perl-Sub-Exporter-Progressive >= 0.001006
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl Tie::StdHash

%description
This module allows you to execute code when Perl finished compiling
the surrounding scope.

%description -l pl.UTF-8
Ten moduł pozwala na wykonanie kodu po zakończeniu kompilacji
otaczającego zakresu kodu przez interpreter Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	--skipdeps \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/B/Hooks
%{perl_vendorlib}/B/Hooks/EndOfScope.pm
%{perl_vendorlib}/B/Hooks/EndOfScope
%{_mandir}/man3/B::Hooks::EndOfScope*.3pm*
