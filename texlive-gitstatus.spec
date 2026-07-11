%global tl_name gitstatus
%global tl_revision 64662

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Include Git information in the document as watermark or via variables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gitstatus
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitstatus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitstatus.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitstatus.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
If your LaTeX-document is version-controlled with git, you might
encounter situations, where you want to include some information of your
git-repository into your LaTeX-document- e.g. to keep track on who gave
you feedback on which version of your document. This git-information can
be included on every page by a watermark or (for custom needs) via
provided variables.

