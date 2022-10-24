#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-requests_kerberos
Version  : 0.14.0
Release  : 45
URL      : https://files.pythonhosted.org/packages/3d/ca/cad727db9eaae0db743982a8197c8a58cc85ed142354abfade1567ede9dc/requests-kerberos-0.14.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/ca/cad727db9eaae0db743982a8197c8a58cc85ed142354abfade1567ede9dc/requests-kerberos-0.14.0.tar.gz
Summary  : A Kerberos authentication handler for python-requests
Group    : Development/Tools
License  : ISC
Requires: pypi-requests_kerberos-license = %{version}-%{release}
Requires: pypi-requests_kerberos-python = %{version}-%{release}
Requires: pypi-requests_kerberos-python3 = %{version}-%{release}
Requires: pypi(kerberos)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cryptography)
BuildRequires : pypi(kerberos)
BuildRequires : pypi(pyspnego)
BuildRequires : pypi(requests)

%description
requests Kerberos/GSSAPI authentication library
===============================================

%package license
Summary: license components for the pypi-requests_kerberos package.
Group: Default

%description license
license components for the pypi-requests_kerberos package.


%package python
Summary: python components for the pypi-requests_kerberos package.
Group: Default
Requires: pypi-requests_kerberos-python3 = %{version}-%{release}

%description python
python components for the pypi-requests_kerberos package.


%package python3
Summary: python3 components for the pypi-requests_kerberos package.
Group: Default
Requires: python3-core
Provides: pypi(requests_kerberos)
Requires: pypi(cryptography)
Requires: pypi(pyspnego)
Requires: pypi(requests)

%description python3
python3 components for the pypi-requests_kerberos package.


%prep
%setup -q -n requests-kerberos-0.14.0
cd %{_builddir}/requests-kerberos-0.14.0
pushd ..
cp -a requests-kerberos-0.14.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656404371
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-requests_kerberos
cp %{_builddir}/requests-kerberos-0.14.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-requests_kerberos/f22ca1d5cd93ca45efa642e3b421a6ce754f844a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-requests_kerberos/f22ca1d5cd93ca45efa642e3b421a6ce754f844a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*