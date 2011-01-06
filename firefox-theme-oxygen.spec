%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define _mozillaextpath %{firefox_mozillapath}/extensions

Summary: Oxygen Icons for Mozilla Firefox
Name: firefox-theme-oxygen
Version: 0.1
Release: %mkrel 30
License: MPLv1.1 and LGPLv2+
Group: Networking/WWW
URL: http://websvn.kde.org/trunk/playground/artwork/Oxygen/firefox/Oxygen
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
