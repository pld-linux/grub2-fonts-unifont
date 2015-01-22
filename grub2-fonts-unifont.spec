# TODO - find and test other unicode fonts for grub2.

Summary:	Unifont font for grub2 gfxterm mode
Summary(pl.UTF-8):	Czcionka unifont do trybu graficznego bootloadera grub2
Name:		grub2-fonts-unifont
Version:	7.0.06
Release:	1
License:	GNU GPL v.2
Group:		Fonts
Source0:	http://unifoundry.com/pub/unifont-%{version}/font-builds/unifont-%{version}.ttf
# Source0-md5:	a3f68517ddc92a4a2ea26f07c75ad7a9
URL:		http://unifoundry.com/unifont.html
BuildRequires:	grub2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unifont font for grub2 gfxterm mode.

%description -l pl.UTF-8
Czcionka unifont do trybu graficznego bootloadera grub2.

%prep
%setup -q -cT %{name}-%{version}
install %{SOURCE0} .

%build
/sbin/grub-mkfont --output=unicode.pf2 unifont-%{version}.ttf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/boot/grub/fonts

cp *.pf2 $RPM_BUILD_ROOT/boot/grub/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir /boot/grub/fonts
/boot/grub/fonts/unicode.pf2
