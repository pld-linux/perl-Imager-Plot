#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Imager
%define		pnam	Plot
%include	/usr/lib/rpm/macros.perl
Summary:	Imager::Plot - generating fancy graphic plots in color
Summary(pl.UTF-8):	Imager::Plot - generowanie ozdobnych wykresów w kolorze
Name:		perl-Imager-Plot
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	04e91bbff3bf92e28ba939aed3752a12
URL:		http://search.cpan.org/dist/Imager-Plot/
BuildRequires:	perl-Imager >= 0.41
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Imager >= 0.41
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a module for generating fancy raster plots in color. There is
support for drawing multiple datasets on the same plot, over a
background image. It's even possible to do shadows with some thinking.
It's also possible to generate clean plots without any chartjunk at
all.

%description -l pl.UTF-8
Ten moduł służy do generowania ozdobnych wykresów rastrowych w
kolorze. Obsługuje rysowanie wielu zbiorów danych na tym samym
wykresie, ponad tym samym tłem. Można nawet dodać cienie. Można też
wygenerować czyste wykresy, bez żadnych zaśmiecaczy.

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
%doc Changes README
%{perl_vendorlib}/Imager/Plot.pm
%{perl_vendorlib}/Imager/Plot
%attr(755,root,root) %{perl_vendorlib}/Imager/plot.pl
%{_mandir}/man3/*
