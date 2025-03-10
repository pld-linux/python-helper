#
# Conditional build:
%bcond_with	tests	# tests (actually no tests included)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Development library for quickly writing configurable applications and daemons
Summary(pl.UTF-8):	Biblioteka programistyczna do szybkiego pisania konfigurowalnych aplikacji i demonów
Name:		python-helper
Version:	2.4.2
Release:	8
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/helper/
Source0:	https://files.pythonhosted.org/packages/source/h/helper/helper-%{version}.tar.gz
# Source0-md5:	b5646fd7a2e6a73b08d221e9d9e654e4
URL:		https://github.com/gmr/helper
%if %{with python2}
BuildRequires:	python-PyYAML
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if "%{py_ver}" < "2.7"
BuildRequires:	python-argparse
BuildRequires:	python-logutils
%endif
%if %{with tests}
BuildRequires:	python-mock
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%endif
%if %{with python3}
BuildRequires:	python3-PyYAML
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
# TODO: switch to unittest.mock (when tests are included)
BuildRequires:	python3-mock
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Helper is a development library for quickly writing configurable
applications and daemons.

%description -l pl.UTF-8
Helper to biblioteka programistyczna do szybkiego pisania
konfigurowalnych aplikacji i demonów.

%package -n python3-helper
Summary:	Development library for quickly writing configurable applications and daemons
Summary(pl.UTF-8):	Biblioteka programistyczna do szybkiego pisania konfigurowalnych aplikacji i demonów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-helper
Helper is a development library for quickly writing configurable
applications and daemons.

%description -n python3-helper -l pl.UTF-8
Helper to biblioteka programistyczna do szybkiego pisania
konfigurowalnych aplikacji i demonów.

%prep
%setup -q -n helper-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/helper
%{py_sitescriptdir}/helper-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-helper
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/helper
%{py3_sitescriptdir}/helper-%{version}-py*.egg-info
%endif
