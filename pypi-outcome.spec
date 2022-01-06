#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-outcome
Version  : 1.1.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/88/b5/9ccedd89d641dcfa5771f636a8a2e99f9d98b09f511f4f870d382ef2b007/outcome-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/b5/9ccedd89d641dcfa5771f636a8a2e99f9d98b09f511f4f870d382ef2b007/outcome-1.1.0.tar.gz
Summary  : Capture the outcome of Python function calls.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-outcome-license = %{version}-%{release}
Requires: pypi-outcome-python = %{version}-%{release}
Requires: pypi-outcome-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(attrs)

%description
.. image:: https://img.shields.io/badge/chat-join%20now-blue.svg
:target: https://gitter.im/python-trio/general
:alt: Join chatroom

%package license
Summary: license components for the pypi-outcome package.
Group: Default

%description license
license components for the pypi-outcome package.


%package python
Summary: python components for the pypi-outcome package.
Group: Default
Requires: pypi-outcome-python3 = %{version}-%{release}

%description python
python components for the pypi-outcome package.


%package python3
Summary: python3 components for the pypi-outcome package.
Group: Default
Requires: python3-core
Provides: pypi(outcome)
Requires: pypi(attrs)

%description python3
python3 components for the pypi-outcome package.


%prep
%setup -q -n outcome-1.1.0
cd %{_builddir}/outcome-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641500824
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-outcome
cp %{_builddir}/outcome-1.1.0/LICENSE.APACHE2 %{buildroot}/usr/share/package-licenses/pypi-outcome/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/outcome-1.1.0/LICENSE.MIT %{buildroot}/usr/share/package-licenses/pypi-outcome/f8c5fdc67d412f3435473ee8ce595f06d921ca44
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-outcome/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-outcome/f8c5fdc67d412f3435473ee8ce595f06d921ca44

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
