Name:		texlive-gitstatus
Version:	64662
Release:	1
Summary:	Include Git information in the document as watermark or via variables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gitstatus
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitstatus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitstatus.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitstatus.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
If your LaTeX-document is version-controlled with git, you
might encounter situations, where you want to include some
information of your git-repository into your LaTeX-document-
e.g. to keep track on who gave you feedback on which version of
your document. This git-information can be included on every
page by a watermark or (for custom needs) via provided
variables.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gitstatus
%{_texmfdistdir}/tex/latex/gitstatus
%doc %{_texmfdistdir}/doc/latex/gitstatus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
