#
# spec file for package python-M2Crypto
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           python-M2Crypto
Version:        0.21.1
Release:        0
Url:            http://chandlerproject.org/bin/view/Projects/MeTooCrypto
Summary:        Crypto and SSL toolkit for Python
License:        MIT and ZPL-2.0 and BSD-3-Clause
Group:          Platfrom Development/Python
Source:         M2Crypto-%{version}.tar.gz
Source1001: 	python-M2Crypto.manifest
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  python-devel
BuildRequires:  python-distribute
BuildRequires:  swig
BuildRequires:  python
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Provides:       python-m2crypto = %{version}
Obsoletes:      python-m2crypto < %{version}

%description
M2Crypto is a crypto and SSL toolkit for Python featuring the
following:

RSA, DSA, DH, HMACs, message digests, symmetric ciphers (including
AES). SSL functionality to implement clients and servers. HTTPS
extensions to Python's httplib, urllib, and xmlrpclib. Unforgeable
HMAC'ing AuthCookies for web session management. FTP/TLS client and
server. S/MIME. ZServerSSL: A HTTPS server for Zope. ZSmime: An S/MIME
messenger for Zope.

It currently lives at
http://wiki.osafoundation.org/bin/view/Projects/MeTooCrypto. The
original M2Crypto homepage is at http://sandbox.rulemaker.net/ngps/m2/.

%prep
%setup -n M2Crypto-%{version}
cp %{SOURCE1001} .

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license LICENCE 
%{python_sitearch}/*

%changelog
