#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	B
%define	pnam	Hooks-EndOfScope
Summary:	B::Hooks::EndOfScope - Execute code after a scope finished compilation
#Summary(pl.UTF-8):	
Name:		perl-B-Hooks-EndOfScope
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/B/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83d941d374d6718cdd5c2721c40f660f
URL:		http://search.cpan.org/dist/B-Hooks-EndOfScope/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Variable::Magic) >= 0.27
BuildRequires:	perl-Sub-Exporter
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to execute code when perl finished compiling
the surrounding scope.

# %description -l pl.UTF-8
# TODO

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
%doc Changes
%{perl_vendorlib}/B/Hooks
%{_mandir}/man3/*
