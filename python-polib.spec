
Name:           python-polib
Version:        0.6.3
Release:        %mkrel 1
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



%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.3-1mdv2011.0
+ Revision: 662536
- update to new version 0.6.3

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.5-1mdv2011.0
+ Revision: 603070
- update to new version 0.5.5

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.4-2mdv2011.0
+ Revision: 592471
- rebuild to get correct auto requries

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.4-1mdv2011.0
+ Revision: 587727
- update to new version 0.5.4

* Wed Sep 29 2010 Michael Scherer <misc@mandriva.org> 0.5.3-1mdv2011.0
+ Revision: 581951
- import python-polib

