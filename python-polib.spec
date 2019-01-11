Name:           python-polib
Version:        1.0.7
Release:        1
Summary:        A library to parse and manage gettext catalogs

Group:          Development/Python
License:        MIT
URL:            http://bitbucket.org/izi/polib/
Source0:	https://pypi.python.org/packages/source/p/polib/polib-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel

%description
polib allows you to manipulate, create, modify gettext files (pot, po and
mo files). You can load existing files, iterate through it's entries, add,
modify entries, comments or metadata, etc... or create new po files from
scratch.

polib provides a simple and pythonic API, exporting only three convenience
functions 'pofile', 'mofile' and 'detect_encoding', and the 4 core classes:
POFile, MOFile, POEntry and MOEntry for creating new files/entries.

%prep
%setup -q -n polib-%{version}

%build
%py_build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%clean

%files
%doc LICENSE 
%{py_puresitedir}/*
