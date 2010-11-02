
Name:           python-polib
Version:        0.5.4
Release:        %mkrel 2
Summary:        A library to parse and manage gettext catalogs

Group:          Development/Python
License:        MIT
URL:            http://bitbucket.org/izi/polib/
Source0:	    http://bitbucket.org/izi/polib/downloads/polib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE 
%{python_sitelib}/*

