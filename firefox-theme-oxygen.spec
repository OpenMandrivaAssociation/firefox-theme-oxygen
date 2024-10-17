%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define _mozillaextpath %{firefox_mozillapath}/extensions

Summary: Oxygen Icons for Mozilla Firefox
Name: firefox-theme-oxygen
Version: 0.1
Release: %mkrel 30
License: MPLv1.1 and LGPLv2+
Group: Networking/WWW
URL: https://websvn.kde.org/trunk/playground/artwork/Oxygen/firefox/Oxygen
Source: mozilla-firefox-theme-oxygen-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox = %{firefox_epoch}:%{firefox_version}
Obsoletes: mozilla-firefox-theme-oxygen < %{version}-%{release}
Provides: mozilla-firefox-theme-oxygen = %{version}-%{release}
BuildRequires: firefox-devel

%description
Oxygen theme is a KDE4-like theme using Oxygen icons for Mozilla Firefox.

%prep
%setup -q -n Oxygen

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING
%dir %firefox_mozillapath
%{_mozillaextpath}


%changelog
* Thu Jan 06 2011 Thierry Vignaud <tv@mandriva.org> 0.1-30mdv2011.0
+ Revision: 628973
- rebuild for new firefox

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.1-29mdv2011.0
+ Revision: 561841
- rebulid for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1-28mdv2010.1
+ Revision: 549357
- rebuild with FF 3.6.6

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.1-27mdv2010.1
+ Revision: 531112
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 0.1-26mdv2010.1
+ Revision: 526994
- rebuild

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 0.1-25mdv2010.1
+ Revision: 494807
- rebuild

* Sun Nov 08 2009 Funda Wang <fwang@mandriva.org> 0.1-24mdv2010.1
+ Revision: 462802
- rebuild for new ff

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.1-23mdv2010.0
+ Revision: 417679
- buildrequire firefox-devel, which provides the new macros for building extensions
- make use of the firefox package macros
- rebuild for firefox 3.5.2

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 0.1-22mdv2010.0
+ Revision: 410509
- rebuild for new ff
- rebuild for new ff

* Wed Jul 22 2009 Raphaël Gertz <rapsys@mandriva.org> 0.1-18mdv2010.0
+ Revision: 398618
- Rebuild

* Wed Jul 22 2009 Raphaël Gertz <rapsys@mandriva.org> 0.1-17mdv2010.0
+ Revision: 398612
- Revert to equal 3.0.11

* Fri Jul 17 2009 Raphaël Gertz <rapsys@mandriva.org> 0.1-15mdv2010.0
+ Revision: 396864
- Allow firefox >= 3.0.11 instead of just 3.0.11

* Wed Jul 15 2009 Raphaël Gertz <rapsys@mandriva.org> 0.1-14mdv2010.0
+ Revision: 396443
- Rebuild

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 0.1-13mdv2010.0
+ Revision: 385781
- rebuild for new ff

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.1-12mdv2010.0
+ Revision: 369818
- rebuild for new ff

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.1-11mdv2009.1
+ Revision: 361857
- rebuild for firefox 3.0.8

* Sat Mar 14 2009 Funda Wang <fwang@mandriva.org> 0.1-10mdv2009.1
+ Revision: 354815
- rebuild for new ff

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 0.1-9mdv2009.1
+ Revision: 337339
- rename tarball
- rename to firefox
- rename to ff

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.1-8mdv2009.1
+ Revision: 318928
- rebuild for new ff

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 0.1-7mdv2009.1
+ Revision: 303708
- rebuild for new ff

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 0.1-6mdv2009.0
+ Revision: 289180
- rebuild for new FF

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 0.1-5mdv2009.0
+ Revision: 257881
- rebuild for ff 3.0.1

* Wed Jul 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-4mdv2009.0
+ Revision: 236363
- rebuilt for mozilla-firefox-2.0.0.16

* Fri Jul 04 2008 Funda Wang <fwang@mandriva.org> 0.1-3mdv2009.0
+ Revision: 231501
- New snapshot of theme

* Thu Jul 03 2008 Tiago Salem <salem@mandriva.com.br> 0.1-2mdv2009.0
+ Revision: 231264
- Rebuild for firefox 2.0.0.15

  + Funda Wang <fwang@mandriva.org>
    - fix URL and license
    - import mozilla-firefox-theme-oxygen

