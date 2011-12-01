Name:           perl-Authen-SASL
Version:        2.13
Release:        2%{?dist}
Summary:        SASL Authentication framework for Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Authen-SASL/
Source0:        http://www.cpan.org/authors/id/G/GB/GBARR/Authen-SASL-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Digest::HMAC)
BuildRequires:  perl(GSSAPI)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all
protocols should be able to share.

%prep
%setup -q -n Authen-SASL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc api.txt Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.13-2
- rebuild against perl 5.10.1

* Mon Oct  5 2009 Stepan Kasal <skasal@redhat.com> - 2.13-1
- new upstream version, BR Test::More

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 01 2008 Steven Pritchard <steve@kspei.com> 2.12-1
- Update to 2.12.

* Thu May 15 2008 Steven Pritchard <steve@kspei.com> 2.11-1
- Update to 2.11.
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- Reformat to resemble cpanspec output.
- Drop explicit perl build dependency.

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.10-2
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.10-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sat Apr 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.10-1
- Update to 2.10.

* Fri Feb 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.09-4
- Rebuild for FC5 (perl 5.8.8).

* Sat May 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.09-3
- Add dist tag.

* Tue Apr 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.09-2
- Update to 2.09.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Apr  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.08-1
- Drop Epoch: 0 and 0.fdr release prefix.

* Wed Jul 21 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.08-0.fdr.1
- Update to 2.08.
- Bring up to date with current fedora.us Perl spec template.

* Fri Jan 30 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.06-0.fdr.1
- First build.
