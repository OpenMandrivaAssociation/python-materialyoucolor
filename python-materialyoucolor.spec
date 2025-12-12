Name:		python-materialyoucolor
Version:	2.0.10
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/m/materialyoucolor/materialyoucolor-%{version}.tar.gz
Summary:	Material You color generation algorithms in pure python!
URL:		https://pypi.org/project/materialyoucolor/
License:	None
Group:		Development/Python
BuildRequires:	pkgconfig(python)
BuildSystem:	python

%description
Material You color generation algorithms in pure python!

%files
%license LICENSE
%doc README.md
%{_libdir}/python%{pyver}/site-packages/materialyoucolor
%{_libdir}/python%{pyver}/site-packages/materialyoucolor-*.*-info
