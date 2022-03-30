#
# Conditional build:
%bcond_without	tests		# unit tests
%bcond_without	python2		# build python 2 module
%bcond_without	python3		# build python 3 module
#
%define		module	oauthlib
Summary:	A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
Summary(pl.UTF-8):	Ogólna, zgodna ze specyfikacją, pełna implementacja logiki podpisywania żądań OAuth
Name:		python-%{module}
Version:	3.1.0
Release:	5
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/oauthlib/
Source0:	https://files.pythonhosted.org/packages/source/o/oauthlib/%{module}-%{version}.tar.gz
# Source0-md5:	43cb2b5bac983712ee55076b61181cc2
Patch0:		%{name}-mock.patch
URL:		https://pypi.org/project/oauthlib/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-blinker
BuildRequires:	python-cryptography
BuildRequires:	python-mock
BuildRequires:	python-nose
BuildRequires:	python-pyjwt >= 1.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-blinker
BuildRequires:	python3-cryptography
BuildRequires:	python3-nose
BuildRequires:	python3-pyjwt >= 1.0.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OAuthLib is a generic utility which implements the logic of OAuth
without assuming a specific HTTP request object. Use it to graft OAuth
support onto your favorite HTTP library. If you're a maintainer of
such a library, write a thin veneer on top of OAuthLib and get OAuth
support for very little effort.

%description -l pl.UTF-8
OAuthLib to ogólne narzędzie implementujące logikę OAuth bez
zakładania określonych obiektów żądań HTTP. Można go użyć do dołożenia
obsługi OAuth do ulubionej biblioteki HTTP. Będąc utrzymującym taką
bibliotekę wystarczy napisać cienką warstwę powyżej OAuthLib, aby
uzyskać obsługę OAuth niskim kosztem.

%package -n python3-oauthlib
Summary:	A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
Summary(pl.UTF-8):	Ogólna, zgodna ze specyfikacją, pełna implementacja logiki podpisywania żądań OAuth
Group:		Development/Languages/Python

%description -n python3-oauthlib
OAuthLib is a generic utility which implements the logic of OAuth
without assuming a specific HTTP request object. Use it to graft OAuth
support onto your favorite HTTP library. If you're a maintainer of
such a library, write a thin veneer on top of OAuthLib and get OAuth
support for very little effort.

%description -n python3-oauthlib -l pl.UTF-8
OAuthLib to ogólne narzędzie implementujące logikę OAuth bez
zakładania określonych obiektów żądań HTTP. Można go użyć do dołożenia
obsługi OAuth do ulubionej biblioteki HTTP. Będąc utrzymującym taką
bibliotekę wystarczy napisać cienką warstwę powyżej OAuthLib, aby
uzyskać obsługę OAuth niskim kosztem.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif
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
%doc CHANGELOG.rst LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oauthlib
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
