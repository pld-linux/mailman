Summary:	The GNU Mailing List Management System
Summary(pl):	System Zarz±dzania Listami Pocztowymi GNU
Name:		mailman
Version:	2.0.3
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.gnu.org/gnu/mailman/%{name}-%{version}.tgz
Patch0:		mailman-configure.patch
URL:		http://www.gnu.org/software/mailman/mailman.html
BuildRequires:	autoconf
BuildRequires:	python >= 2.0
Requires:	python >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mailman -- The GNU Mailing List Management System --
is a mailing list management system written mostly in
Python. Features:
o Most standard mailing list features, including: moderation, mail based commands, digests, etc...
o An extensive Web interface, customizable on a per-list basis.
o Web based list administration interface for *all* admin-type tasks
o Automatic Web based hypermail-style archives (using pipermail or other external archiver), including provisions for private archives
o Integrated mail list to newsgroup gatewaying
o Integrated newsgroup to mail list gatewaying (polling-based... if you have access to the nntp server, you should be able to easily do non-polling based news->mail list gatewaying; email viega@list.org,I'd like to help get that going and come up with instructions)
o Smart bounce detection and correction
o Integrated fast bulk mailing
o Smart spam protection
o Extensible logging
o Multiple list owners and moderators are possible
o Optional MIME-compliant digests
o Nice about which machine you subscribed from if you're from the right domain
%description -l pl
Mailman -- System Zarz±dzania Listami Pocztowymi GNU -- zosta³ napisany
g³ównie w Pythonie. Jego mo¿liwo¶ci to:
o Standardowe mo¿liwo¶ci: moderowanie, komendy przesy³ane poczt±, digesty itp.
o Interfejs WWW konfigurowalny dla ka¿dej listy.
o Automatyczny system archiwizowania (z u¿yciem pipermaila lub innego zewnêtrznego archiwizera) w³±czaj±c w to odpowiednie zarz±dzanie prywatnymi archiwami.
o Bramki mail <-> news
o Doskona³y system wykrywania odbiæ i korekcji odbitej poczty.
o System ochrony przed spamem.
o Rozszerzone logowanie.
o Listy mog± byæ w³asno¶ci± wielu osób oraz moderatorów mo¿e byæ kilku.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure \
	--prefix=%{_var}/state/mailman \
	--exec-prefix=%{_libdir}/mailman \
	--with-var-prefix=%{_var}/spool/mailman \
	--with-username=%{name} \
	--with-groupname=%{name} \
	--with-mail-gid=12 \
	--with-cgi-gid=51 \
	--with-cgi-ext=.cgi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_var}/state/mailman \
	exec_prefix=$RPM_BUILD_ROOT%{_libdir}/mailman \
	var_prefix=$RPM_BUILD_ROOT%{_var}/spool/mailman

gzip -9nf BUGS FAQ INSTALL NEWS README* TODO UPGRADING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

# PERMISSIONS ARE WRONG. FIXME
%{_var}/state/mailman
%{_libdir}/mailman
%{_var}/spool/mailman
