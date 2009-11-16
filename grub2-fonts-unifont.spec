# TODO - find and test other unicode fonts for grub2.

%define	 _enable_debug_packages 0
%define _snap	20080907
%define	_sizes	{12 18 24 32}
%define _fontname unifont
%define _destdir  /grub2/fonts
Summary:	Unifont font for grub2 gfxterm mode
Summary(pl.UTF-8):	Czcionka unifont do trybu graficznego bootloadera grub2
Name:		grub2-fonts-%{_fontname}
Version:	5.1
Release:	1
License:	GNU GPL v.2
Group:		Fonts
Source0:	http://unifoundry.com/%{_fontname}-%{version}.%{_snap}.ttf.gz
# Source0-md5:	708a693e340902779ec9ad13acae279a	
Source1:	simple_convert
URL:		http://unifoundry.com/unifont.html
BuildRequires:	grub2
BuildRequires:	freetype1-tools-ttf2bdf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Unifont font for grub2 gfxterm mode.

%description -l pl.UTF-8
Czcionka unifont do trybu graficznego bootloadera grub2.

%prep
%setup -cT %{name}-%{version}
install %{SOURCE0} .
install %{SOURCE1} .
gzip -d %{_fontname}-%{version}.%{_snap}.ttf.gz
mv %{_fontname}-%{version}.%{_snap}.ttf %{_fontname}.ttf

%build
for i in %{_sizes}; do
	# /usr/bin/ttf2bdf -v -r 75 -p $i -o %{_fontname}$i.bdf -t %{_fontname} %{_fontname}.ttf
	#/sbin/grub-mkfont --output=%{_fontname}$i.pf2 %{_fontname}$i.bdf
	sh simple_convert $i %{_fontname}
done

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}%{_destdir}
#gzip -9 *.pf2
cp *.pf2* $RPM_BUILD_ROOT%{_datadir}%{_destdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "These are (%{_sizes})pt/75dpi fonts.
Copy one somewhere under /boot location and set in grub.cfg.
To get other sizes rebuild package setting desired _sizes."

#%post -l pl.UTF-8
#echo "To są czcionki o wielkościach  (%{_sizes})pt/75dpi.
#Skopiuj którąś do katalogu /boot i wskaż w grub.cfg.
#Żeby uzyskać inne wielkości przebuduj pakiet zmieniając parametr _sizes."

%files
%defattr(644,root,root,755)
%{_datadir}%{_destdir}
