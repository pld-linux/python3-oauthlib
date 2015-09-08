# Conditional build:
%bcond_without  python2         # build python 2 module
%bcond_without  python3         # build python 3 module
#
%define 	module	oauthlib
Summary:	A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
Name:		python-%{module}
Version:	1.0.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/o/oauthlib/%{module}-%{version}.tar.gz
# Source0-md5:	02772867bf246b3b37f4ed22786c41f5
URL:		https://pypi.python.org/pypi/oauthlib
%if %{with python2}
BuildRequires:	python-distribute
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-modules >= 3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OAuthLib is a generic utility which implements the logic of OAuth
without assuming a specific HTTP request object. Use it to graft OAuth
support onto your favorite HTTP library. If you're a maintainer of
such a library, write a thin veneer on top of OAuthLib and get OAuth
support for very little effort.

%package -n python3-oauthlib
Summary:	A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
Group:		Development/Languages/Python

%description -n python3-oauthlib
OAuthLib is a generic utility which implements the logic of OAuth
without assuming a specific HTTP request object. Use it to graft OAuth
support onto your favorite HTTP library. If you're a maintainer of
such a library, write a thin veneer on top of OAuthLib and get OAuth
support for very little effort.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build -b py2
%endif

%if %{with python3}
%{__python3} setup.py build -b py3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build -b py2 \
	install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py  \
	build -b py3 \
	install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%{__rm} -rf $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py3_sitescriptdir}}/%{module}/{cacert.pem,packages}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-oauthlib
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
