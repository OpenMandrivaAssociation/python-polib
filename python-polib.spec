Name:           python-polib
Version:	1.2.0
Release:	1
Summary:        A library to parse and manage gettext catalogs

Group:          Development/Python
License:        MIT
URL:            https://bitbucket.org/izi/polib/
Source0:	https://files.pythonhosted.org/packages/source/p/polib/polib-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:	python

%description
polib allows you to manipulate, create, modify gettext files (pot, po and
mo files). You can load existing files, iterate through it's entries, add,
modify entries, comments or metadata, etc... or create new po files from
scratch.

polib provides a simple and pythonic API, exporting only three convenience
functions 'pofile', 'mofile' and 'detect_encoding', and the 4 core classes:
POFile, MOFile, POEntry and MOEntry for creating new files/entries.

%files
%defattr(-,root,root,-)
%doc LICENSE 
%{py_puresitedir}/*
