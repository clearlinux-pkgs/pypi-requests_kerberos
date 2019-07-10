#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-kerberos
Version  : 0.12.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/14/61/85737ebe1e65cd4bf023d9e4610df70851bd7638e003b81a44a9b901feae/requests-kerberos-0.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/14/61/85737ebe1e65cd4bf023d9e4610df70851bd7638e003b81a44a9b901feae/requests-kerberos-0.12.0.tar.gz
Summary  : A Kerberos authentication handler for python-requests
Group    : Development/Tools
License  : ISC
Requires: requests-kerberos-license = %{version}-%{release}
Requires: requests-kerberos-python = %{version}-%{release}
Requires: requests-kerberos-python3 = %{version}-%{release}
Requires: cryptography
Requires: kerberos
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : kerberos
BuildRequires : requests
Patch1: 0001-Switch-to-kerberos-package-name.patch

%description
===============================================

%package license
Summary: license components for the requests-kerberos package.
Group: Default

%description license
license components for the requests-kerberos package.


%package python
Summary: python components for the requests-kerberos package.
Group: Default
Requires: requests-kerberos-python3 = %{version}-%{release}

%description python
python components for the requests-kerberos package.


%package python3
Summary: python3 components for the requests-kerberos package.
Group: Default
Requires: python3-core

%description python3
python3 components for the requests-kerberos package.


%prep
%setup -q -n requests-kerberos-0.12.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1562790865
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests-kerberos
cp LICENSE %{buildroot}/usr/share/package-licenses/requests-kerberos/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests-kerberos/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
