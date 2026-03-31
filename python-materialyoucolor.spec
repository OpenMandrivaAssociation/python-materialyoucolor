%define module materialyoucolor

Name:		python-materialyoucolor
Version:	3.0.2
Release:	1
Summary:	Material You color generation algorithms in pure python!
License:	None
Group:		Development/Python
URL:		https://pypi.org/project/materialyoucolor/
Source0:	https://files.pythonhosted.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pybind11)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Material You color generation algorithms in pure python!

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%files
%doc README.md
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
