Name:		texlive-bxnewfont
Version:	44173
Release:	2
Summary:	Enhanced \newfont command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxnewfont
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxnewfont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxnewfont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a new command \newfontx. It is similar to
the old (and deprecated) command \newfont in function, but is
more compatible with NFSS. In particular, one can safely change
font size after invoking a font command defined by \newfontx.
The new command will be useful to users who know much of the
old \newfont command, but are unfamiliar with the details of
NFSS.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxnewfont
%doc %{_texmfdistdir}/doc/latex/bxnewfont

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
